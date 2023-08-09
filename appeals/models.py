from django.db import models

from users.models import User


class Appeal(models.Model):
    class Topics(models.TextChoices):
        """Available topics of appeal."""

        RECTOR = "rector", "Ректор"
        PRO_RECTOR = "pro_rector", "Проректор"

    class Statuses(models.TextChoices):
        """Available statuses of appeal."""

        WAITING = "waiting", "Ожидание"
        COME_IN = "come_in", "Заходите"
        REJECT = "reject", "Отказ"

    topic = models.CharField("Роль", max_length=256, choices=Topics.choices)
    status = models.CharField("Статус", max_length=256, choices=Statuses.choices, default=Statuses.WAITING)
    description = models.TextField("Описание запроса", max_length=1024)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Учетная запись", related_name="appeals")
    is_completed = models.BooleanField("Выполнена", default=False)

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"

    def __str__(self):
        return f"{str(self.pk)}"
