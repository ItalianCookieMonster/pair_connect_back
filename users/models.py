from django.db import models
from skills.models import Stack, Level, ProgLanguage
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """Manager personalizado para manejar usuarios con email como USERNAME_FIELD."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El campo email debe ser proporcionado')
        email = self.normalize_email(email)

        # Extraer y eliminar 'username' de extra_fields
        username = extra_fields.pop('username', None)
        if not username:
            raise ValueError('El campo username debe ser proporcionado')

        # Crear instancia del usuario sin duplicar 'username'
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Crea y guarda un usuario regular."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Crea y guarda un superusuario."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True)
    photo = CloudinaryField('image', null=True, blank=True)
    stack = models.ForeignKey(Stack, on_delete=models.SET_NULL, null=True, blank=True)
    prog_language = models.ForeignKey(ProgLanguage, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    linkedin_link = models.URLField(max_length=255, null=True, blank=True)
    github_link = models.URLField(max_length=255, null=True, blank=True)
    discord_link = models.URLField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} {self.email}"
