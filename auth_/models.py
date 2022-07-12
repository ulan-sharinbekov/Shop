from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, UserManager
from city.models import City

#
# # Create your models here.
#
class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    # USER_ROLES = (
    #     (1, 'Admin'),
    #     (2, 'Customer'),
    # )
    username = models.CharField(max_length=255, null=False, unique=True)
    first_name = models.CharField(max_length=255, null=True, default='')
    last_name = models.CharField(max_length=255, null=True, default='')
    email = models.EmailField( verbose_name='email address', max_length=255, unique=True)
    mobile = models.CharField(max_length=12, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # role = models.IntegerField(choices=USER_ROLES, default=2)
    INN = models.IntegerField(unique=True, verbose_name='Identification number', null=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True


    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.username)
        return full_name


    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.first_name


class MyUser(MyAbstractUser):
    USER_ROLES = (
        (1, 'Admin'),
        (2, 'Customer'),
    )

    role = models.IntegerField(choices=USER_ROLES, default=2)

class ProfileManager(models.Manager):
    pass


class Profile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='profiles', null=True, blank=True)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    objects = ProfileManager()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f'Name: {self.user.first_name}. Email: {self.user.email}'
