import inspect
from collections.abc import Callable
from functools import partial

from allocation.adapters import orm, redis_eventpublisher
from allocation.adapters.notifications import (
    AbstractNotifications,
    EmailNotifications,
)
from allocation.service_layer import handlers, messagebus, unit_of_work


def bootstrap(
    uow: unit_of_work.AbstractUnitOfWork,
    start_orm: bool = True,
    notifications: AbstractNotifications | None = None,
    publish: Callable = redis_eventpublisher.publish,
) -> messagebus.MessageBus:
    if notifications is None:
        notifications = EmailNotifications()

    if start_orm:
        orm.start_mappers()

    dependencies = {"uow": uow, "notifications": notifications, "publish": publish}
    injected_event_handlers = {
        event_type: [inject_dependencies(handler, dependencies) for handler in event_handlers]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies: dict[str, object]):
    params = inspect.signature(handler).parameters
    deps = {name: dependency for name, dependency in dependencies.items() if name in params}
    return partial(handler, **deps)