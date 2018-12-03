from django.db import models
from django.utils import timezone
# Create your models here.

class StudenData(models.Model):
	files=models.FileField(upload_to='pic_folder/')

	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def __str__(self):
		return self.file



class Student(models.Model):
	st_id=models.CharField(max_length=255)
	st_name=models.CharField(max_length=255)
	st_add=models.TextField()
	st_st=models.CharField(max_length=255)
	st_per=models.PositiveIntegerField()


	def __str__(self):
		return self.st_name