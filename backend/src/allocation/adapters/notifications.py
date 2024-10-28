import abc
import smtplib

from allocation import config


class AbstractNotifications(abc.ABC):
    @abc.abstractmethod
    def send(self, destination, message):
        raise NotImplementedError


settings = config.AllocationSettings()


class EmailNotifications(AbstractNotifications):
    def __init__(self, smtp_host=settings.SMTP_HOST, port=settings.SMTP_PORT):
        self.server = smtplib.SMTP(smtp_host, port=port)
        self.server.noop()

    def send(self, destination, message):
        msg = f"Subject: allocation service notification\n{message}"
        self.server.sendmail(
            from_addr="allocations@example.com",
            to_addrs=[destination],
            msg=msg,
        )
