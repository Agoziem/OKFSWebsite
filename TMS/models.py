from django.db import models

class Teacher(models.Model):
	Name= models.CharField(max_length= 200, blank=True)
	Phone_number= models.CharField(max_length= 200, blank=True)
	Email= models.EmailField(max_length= 200, blank=True)
	Role= models.CharField(max_length= 200, blank=True)
	Subject=models.CharField(max_length= 200, blank=True)
	Class_assigned=models.CharField(max_length= 200, blank=True)
	Facebook_link=models.CharField(max_length= 200, blank=True)
	Twitter_link=models.CharField(max_length= 200, blank=True)
	Instagram_link=models.CharField(max_length= 200, blank=True)
	Headshot=models.ImageField(upload_to='assets', blank=True)
	
	def __str__(self):
		return str(self.Name)
