from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import MaxValueValidator, MinValueValidator

class UserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, height, weight, password=None):
        #メールアドレスの登録を必須
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            date_of_birth=date_of_birth,
            height=height,
            weight=weight,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, height, weight, password):
        user = self.create_user(
            email,
            username,
            password=password,
            date_of_birth=date_of_birth,
            height=height,
            weight=weight,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )

    date_of_birth = models.DateField()

    height = models.DecimalField(
        # 少数第一位まで
        decimal_places=1,
        # 許容値()
        max_digits=4,
        # django のフォームからの投稿が空であることを許容する
        blank=True,
        # DBの中身がからであることを許容する
        null=True,
        # マイナスは入れないように制限する
        validators=[MinValueValidator(0), MaxValueValidator(999.9)],
    )

    weight = models.DecimalField(
        # 少数第2位まで
        decimal_places=2,
        # 許容値
        max_digits=5,
        # django のフォームからの投稿が空であることを許容する
        blank=True,
        # DBの中身がからであることを許容する
        null=True,
        # マイナスは入れないように制限する
        validators=[MinValueValidator(0), MaxValueValidator(999.99)],
    ) 

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth', 'height', 'weight']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin