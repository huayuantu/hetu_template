import logging

import redis

from allocation import config
from allocation.domain import events

logger = logging.getLogger(__name__)

settings = config.AllocationSettings()
r = redis.Redis.from_url(str(settings.REDIS_URL))


def publish(channel, event: events.Event):
    logging.info("publishing: channel=%s, event=%s", channel, event)
    r.publish(channel, event.model_dump_json())
