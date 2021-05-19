from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from Club.models import Club
# Create your models here.

class CustUserManager(BaseUserManager):
    def create_user(self, userName, email, name, year, roll, department, mobileNumber, club, password = None):
        if not userName:
            raise ValueError('User must have a username')
        if not email:
            raise ValueError('User must have an email')
        
        user = self.model(userName = userName, email = self.normalize_email(email), name = name, year = year, roll = roll, department = department, mobileNumber = mobileNumber,club=club)
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_convener(self, userName, email, name, year, roll, department, mobileNumber, club, password = None):
        user = self.create_user(userName, email, name, year, roll, department, mobileNumber,club, password)

        user.is_convener = True
        user.save(using = self._db)

        return user

    def create_superuser(self, userName, email, name, year, roll, department, mobileNumber, club, password = None):
        user = self.create_user(userName, email, name, year, roll, department, mobileNumber,club, password)

        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    YEAR = (
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year')
    )
    userName         = models.CharField(verbose_name = "Username", max_length = 27, unique = True)
    email            = models.CharField(verbose_name = 'Email Address', max_length = 27, unique = True)
    name             = models.CharField(verbose_name = 'First Name',max_length = 27)
    year             = models.IntegerField(verbose_name = 'Year', choices = YEAR, default = 2)
    roll             = models.CharField(verbose_name = 'Roll Number', max_length = 10)
    department       = models.CharField(verbose_name = 'Department', max_length = 20)
    mobileNumber     = models.CharField(verbose_name = 'Mobile Number',max_length = 27 ,unique = True)
    club             = models.ForeignKey(Club, default = None, on_delete = models.SET_NULL ,related_name = 'Club_Member', null = True, blank = True)
    is_convener      = models.BooleanField(default = False)
    is_active        = models.BooleanField(default = True)
    is_admin         = models.BooleanField(default = False)

    objects = CustUserManager()

    USERNAME_FIELD  = 'userName'
    REQUIRED_FIELDS = ['email', 'name', 'roll', 'year', 'department', 'mobileNumber', ]

    def __str__(self):
        return self.userName

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    def is_head(self):
        return self.is_convener