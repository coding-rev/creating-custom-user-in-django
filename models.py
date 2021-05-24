from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField

# create a new user
# create a super user
class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address.')
		if not username:
			raise ValueError('Users mush have a username.')

		user = self.model(
			email = self.normalize_email(email),
			username = username,
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email = self.normalize_email(email),
			username = username,
			password = password
		)
		user.is_admin 		= True
		user.is_superuser	= True
		user.is_staff 		= True

		user.save(using=self._db)
		return user


class Users(AbstractBaseUser):
	username 				= models.CharField(max_length=30, unique=True)
	profile_image 			= models.ImageField(blank=True, null=True)
	companies_name 			= models.CharField(max_length=200) 
	email 					= models.EmailField(unique=True)
	country 				= CountryField(multiple=False)
	date_joined 			= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last joined', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active 				= models.BooleanField(default=True)
	is_staff 				= models.BooleanField(default=False)
	is_superuser 			= models.BooleanField(default=False)
	hide_email 				= models.BooleanField(default=True)
		
	objects = MyAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	class Meta:
		verbose_name_plural = "Users"

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perm(self, app_label):
		return True



	

	
# Countries package DOC
# >>> person = Person(name='Chris', country='NZ')
# >>> person.country
# Country(code='NZ')
# >>> person.country.name
# 'New Zealand'
# >>> person.country.flag
# '/static/flags/nz.gif'