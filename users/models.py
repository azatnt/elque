from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, phone, name, role, password=None):
        if not phone:
            raise ValueError("The Phone field must be set")
        user = self.model(phone=phone, name=name, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, name, role, password=None):
        user = self.create_user(phone, name, role, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Names(models.TextChoices):
        RECTOR = "rector", "Ректор"
        SECRETARY = "secretary", "Секретарша"
        CLIENT = "client", "Клиент"

    role = models.CharField("Роль", max_length=256, choices=Names.choices)
    phone = PhoneNumberField("Моб. телефон", unique=True)
    name = models.CharField("Наименование", max_length=256)

    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Статус персонала", default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'role']

    class Meta:
        verbose_name = "Учетная запись"
        verbose_name_plural = "Учетные записи"

    def __str__(self):
        return f"{str(self.pk)} ({self.phone})"
