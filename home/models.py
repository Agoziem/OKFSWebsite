from django.db import models
from ckeditor.fields import RichTextField

class School(models.Model):
	Schoolid=models.IntegerField()
	Schoollogo=models.ImageField(upload_to='assets/Schoollogo', blank=True)
	Schoolname= models.CharField(max_length= 300, blank=True)
	SchoolPhonenumber= models.CharField(max_length= 300, blank=True)
	Schoolmotto= models.CharField(max_length= 300, blank=True)
	Schoollocation= models.CharField(max_length= 300, blank=True)
	SchoolVision= RichTextField(blank=True)
	SchoolMission= RichTextField(blank=True)
	SchoolAbout= RichTextField(blank=True)
	SchoolAimsandObjectives= RichTextField(blank=True)
	Facebookpage= models.CharField(max_length= 300, blank=True)
	Twitterpage= models.CharField(max_length= 300, blank=True)
	Whatsapp= models.CharField(max_length= 300, blank=True)
	Emailaddress= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Schoolname) 
		
class Management(models.Model):
	Profileimage=models.ImageField(upload_to='assets', blank=True)
	Profilename= models.CharField(max_length= 300, blank=True)
	Role= models.CharField(max_length= 300, blank=True)
	Phonenumber= models.CharField(max_length= 300, blank=True)
	Emailaddress= models.CharField(max_length= 300, blank=True)
	Facebookpage= models.CharField(max_length= 300, blank=True)
	Twitterpage= models.CharField(max_length= 300, blank=True)
	Whatsapp= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Profilename)

class TopTeacher(models.Model):
	Profileimage=models.ImageField(upload_to='assets', blank=True)
	Profilename= models.CharField(max_length= 300, blank=True)
	Role= models.CharField(max_length= 300, blank=True)
	Phonenumber= models.CharField(max_length= 300, blank=True)
	Emailaddress= models.CharField(max_length= 300, blank=True)
	Facebookpage= models.CharField(max_length= 300, blank=True)
	Twitterpage= models.CharField(max_length= 300, blank=True)
	Whatsapp= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Profilename)
	
	def TopTeachersimageURL(self):
		try:
			url= self.Profileimage.url
		except:
			url=""
		return url

	
class Subscription(models.Model):
	Email= models.EmailField(blank = True,null=True)
	
	def __str__(self):
		return str(self.Email)
		

class PhotoGallery(models.Model):
	Photo=models.ImageField(upload_to='assets/Photogallery')
	Description= models.CharField(max_length= 300, blank=False)
	
	def __str__(self):
		return str(self.Description)
	
	def imageURL(self):
		try:
			url= self.Photo.url
		except:
			url=""
		return url
		
class UpcomingEvents(models.Model):
	Flier=models.ImageField(upload_to='assets/Eventsflier', blank=True)
	Eventtitle= models.CharField(max_length= 300, blank=True)
	EventTopic= models.CharField(max_length= 300, blank=True)
	Eventspeaker_Chairman= models.CharField(max_length= 300, blank=True)
	Eventdate= models.CharField(max_length= 300, blank=True)
	Eventtime= models.CharField(max_length= 300, blank=True)
	Eventvenue= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Eventtitle)
		
class FAQ(models.Model):
	questionnumber=models.CharField(max_length= 300, blank=True)
	Questions= models.CharField(max_length= 300, blank=True)
	Answer= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Questions)

class Contact(models.Model):
	name = models.CharField(max_length=100)
	message = models.TextField()
	email = models.EmailField()

	def __str__(self):
		return str(self.email)
	
class CarouselItem(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='carousel_images/')
    animation_title = models.CharField(max_length=50, default='fadeInRight')
    animation_tag = models.CharField(max_length=50, default='fadeInLeft')
    animation_cta = models.CharField(max_length=50, default='fadeInBottomLeft')
    cta_link = models.CharField(max_length=255, default='#')
    cta_text = models.CharField(max_length=100, default='Register now')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
	
class SchoolDocument(models.Model):
	title = models.CharField(max_length=255)
	document = models.FileField(upload_to='school_documents/')
	order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['order']

	def __str__(self):
		return self.title