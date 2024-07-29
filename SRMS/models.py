from django.db import models
from openpyxl import Workbook,load_workbook
import boto3
import io
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from openpyxl.utils import get_column_letter
import os
import random
from ckeditor.fields import RichTextField



class AcademicSession(models.Model):
	session = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return str(self.session)

class Term(models.Model):
	academicsession = models.ForeignKey(AcademicSession,on_delete=models.CASCADE , blank = True)
	term = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return f'{self.term} ({self.academicsession.session})'

# Model for the Classes
class Class(models.Model):
	Class=models.CharField(max_length=120, blank=True)
	
	def __str__(self):
		return str(self.Class)
	
class Subject(models.Model):
	subject_code = models.CharField(max_length=100)
	subject_name = models.CharField(max_length=100)
	
	def __str__(self):
		return str(self.subject_name)
	
class Subjectallocation(models.Model):
	classname=models.ForeignKey(Class, on_delete=models.CASCADE , blank = True,null=True)
	subjects=models.ManyToManyField(Subject)

	def __str__(self):
		return f"subjects allocated for {self.classname}"

# Model for the Newsletter Section & Assignments
class Newsletter(models.Model):
	Term = models.CharField(max_length=100, blank=True)
	newsletterConstruct= RichTextField(blank=True,null=True)
	newsletterFile=models.FileField(upload_to = 'media/Newsletter' ,blank = True)

	def __str__(self):
		return f"Newsletter for {self.Term}"
	
	@property
	def NewsletterURL(self):
		try:
			url= self.newsletterFile.url
		except:
			url=""
		return url

class Assignments(models.Model):
	Class= models.ForeignKey(Class, related_name='classes' , on_delete=models.CASCADE , blank = True,null=True)
	subject=models.CharField(max_length=200, blank=True)
	file=models.FileField(upload_to = 'media' ,blank = True)

	def __str__(self):
		return str(self.subject)


# Model for the Excel Files 
class Excelfiles(models.Model):
	Excel= models.FileField(upload_to = 'media' ,blank = True)
	
	def __str__(self):
		return str(self.Excel)	



class Students_Pin_and_ID(models.Model):
	SN=models.CharField(max_length=100, blank=True,null=True)
	student_Photo=models.ImageField(upload_to="assets/Students",blank=True,null=True)
	student_name=models.CharField(max_length=100, blank=True, default="No name",null=True)
	Sex=models.CharField(max_length=100, blank=True,null=True)
	student_id=models.CharField(max_length=100, blank=True,null=True)
	student_pin=models.CharField(max_length=100, blank=True,null=True)
	student_class=models.ForeignKey(Class,on_delete=models.CASCADE,default=1,null=True)
	student_password=models.CharField(max_length=100, blank=True,null=True,default="No password")


	def __str__(self):
		return str(self.student_name)

	def save(self, *args, **kwargs):
		if self.id:  # if object exists in database
			super().save(*args, **kwargs)
		else:
			while not self.student_id:
        	# Split the full_name field value into a list of names 
				names = self.student_name.split()
				# Remove extra spaces from each name in the list	
				names = [name.upper().strip() for name in names]
				# Join the names back together with a single space in between
				self.student_name = ' '.join(names)
				random_pin = str(random.randint(1000, 9999))
				random_14_digit = str(random.randint(10**13, 10**14 - 1))
				student_id = f"okfs/{random_pin}"
				object_with_similar_student_id = Students_Pin_and_ID.objects.filter(student_id=student_id,student_pin=random_14_digit)
				if not object_with_similar_student_id:
					self.student_id = student_id
					self.student_pin = random_14_digit
			super().save(*args, **kwargs)


# Model for the Termly Students data

class Student_Result_Data(models.Model):
	Student_name=models.ForeignKey(Students_Pin_and_ID,on_delete=models.CASCADE)
	TotalScore=models.CharField(max_length=100, blank=True, default="-")
	Totalnumber=models.CharField(max_length=100, blank=True, default="-")
	Average=models.CharField(max_length=100, blank=True, default="-")
	Position=models.CharField(max_length=100, blank=True, default="-")
	Remark=models.CharField(max_length=100, blank=True,null=True , default="-")
	Term=models.ForeignKey(Term,on_delete=models.CASCADE,blank=True,null=True)
	Academicsession=models.ForeignKey(AcademicSession,on_delete=models.CASCADE,blank=True,null=True)
	published=models.BooleanField(default=False)

	def __str__(self):
		return str(self.Student_name.student_name)

# Model for Termly Results from the teachers

class Result(models.Model):
	students_result_summary = models.ForeignKey(Student_Result_Data,on_delete=models.CASCADE,blank=True,null=True)
	Subject= models.ForeignKey(Subject,on_delete=models.CASCADE)
	FirstTest= models.CharField(max_length=100, blank=True,default="-")
	SecondTest= models.CharField(max_length=100, blank=True,default="-")
	Project= models.CharField(max_length=100, blank=True  ,default="-")
	MidTermTest= models.CharField(max_length=100, blank=True ,default="-")
	FirstAss= models.CharField(max_length=100, blank=True ,default="-")
	SecondAss= models.CharField(max_length=100, blank=True ,default="-")
	CA= models.CharField(max_length=100, blank=True ,default="-")
	Exam= models.CharField(max_length=100, blank=True ,default="-")
	Total= models.CharField(max_length=100, blank=True ,default="-")
	Grade=models.CharField(max_length=100, blank=True ,default="-")
	SubjectPosition=models.CharField(max_length=100, blank=True ,default="-")
	Remark=models.CharField(max_length= 100, blank=True ,default="-")
	published=models.BooleanField(default=False)

	def __str__(self):
		return str(self.students_result_summary.Student_name.student_name +"-"+ self.Subject.subject_name)

#Models for Annual Students Details
class AnnualStudent(models.Model):
	Student_name=models.ForeignKey(Students_Pin_and_ID,on_delete=models.CASCADE)
	academicsession=models.ForeignKey(AcademicSession,on_delete=models.CASCADE,blank=True,null=True)
	TotalScore=models.CharField(max_length=100, blank=True)
	Totalnumber=models.CharField(max_length=100, blank=True)
	Average=models.CharField(max_length=100, blank=True)
	Position=models.CharField(max_length=100, blank=True)
	published=models.BooleanField(default=False)
	Remark=models.CharField(max_length=100, blank=True,null=True)
	Verdict=models.CharField(max_length=100, blank=True,null=True)

	def __str__(self):
		return str(self.Student_name.student_name)

# 
# Model for Annual Result
class AnnualResult(models.Model):
	Student_name=models.ForeignKey(AnnualStudent,on_delete=models.CASCADE,blank=True,null=True)
	Subject= models.ForeignKey(Subject,on_delete=models.CASCADE)
	FirstTermTotal= models.CharField(max_length=100, blank=True,null=True,default="-")
	SecondTermTotal= models.CharField(max_length=100, blank=True,null=True,default="-")
	ThirdTermTotal= models.CharField(max_length=100, blank=True,null=True,default="-")
	Total= models.CharField(max_length=100, blank=True,null=True,default="-")
	Average= models.CharField(max_length=100, blank=True,null=True,default="-")
	Grade=models.CharField(max_length=100, blank=True,null=True,default="-")
	SubjectPosition=models.CharField(max_length=100, blank=True,null=True,default="-")
	Remark=models.CharField(max_length= 100, blank=True,null=True, default="-")
	published=models.BooleanField(default=False)

	def __str__(self):
		return str(self.Student_name.Student_name.student_name +"-"+ self.Subject.subject_name)



		