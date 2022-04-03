from django.db import models

class Subject(models.Model):
	Sub= models.CharField(max_length= 200, blank=True)
	Icon=models.ImageField(upload_to='assets', blank=True)
	
	def __str__(self):
		return str(self.Sub)
	
class Ebook(models.Model):
	Ebookcategory= models.ForeignKey(Subject, related_name='Subject' , on_delete=models.CASCADE , blank = True,null=True)
	Ebookimage=models.ImageField(upload_to='assets', blank=True)
	EbookTitle= models.CharField(max_length= 300, blank=True)
	Ebookdescription= models.CharField(max_length= 400, blank=True)
	Ebookauthor= models.CharField(max_length= 300, blank=True)
	Ebook= models.FileField(upload_to = 'media' ,blank = True)
	date_published=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.EbookTitle)
