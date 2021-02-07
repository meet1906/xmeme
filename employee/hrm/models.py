from django.db import models

# Create your models here.
class Users(models.Model):
	employee_id = models.CharField(max_length=20,unique=True)
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	ranking = models.FloatField()

	def upload_photo(self,filename):
		path = '/home/meet/python-restapis-learn/employee/hrm/photo/()'.format(filename)
		return path

	photo = models.ImageField(upload_to=upload_photo,null=True,blank=True)

	def upload_file(self,filename):
		path = '/home/meet/python-restapis-learn/employee/hrm/file/()'.format(filename)
		return path

	resume = models.ImageField(upload_to=upload_file,null=True,blank=True)
