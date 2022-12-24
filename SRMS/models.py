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

# Model for Annual Result
class AnnualResult(models.Model):
	SN= models.CharField(max_length=100, blank=True)
	Name=models.CharField(max_length=200, blank=True,)
	Class=models.CharField(max_length=100, blank=True)
	Subject= models.CharField(max_length=100, blank=True)
	FirstTerm= models.CharField(max_length=100, blank=True)
	SecondTerm= models.CharField(max_length=100, blank=True)
	ThirdTerm= models.CharField(max_length=100, blank=True)
	Total= models.CharField(max_length=100, blank=True)
	Average= models.CharField(max_length=100, blank=True)
	Grade=models.CharField(max_length=100, blank=True)
	SubjectPosition=models.CharField(max_length=100, blank=True)
	Remark=models.CharField(max_length= 100, blank=True)

	def __str__(self):
		return str(self.Name +"-"+ self.Subject+"-"+self.Class)

#Models for Annual Students Details

class AnnualStudent(models.Model):
	Name=models.CharField(max_length=200, blank=True)
	Class=models.CharField(max_length=100, blank=True)
	TotalScore=models.CharField(max_length=100, blank=True)
	Totalnumber=models.CharField(max_length=100, blank=True)
	Average=models.CharField(max_length=100, blank=True)
	Position=models.CharField(max_length=100, blank=True)
	Term=models.CharField(max_length=100, blank=True)
	Academicsession=models.CharField(max_length=100, blank=True)

	def __str__(self):
		return str(self.Name+"-"+self.Class)

	# Annual Students Result

# Jss1 //////////////////////////////////////////
	def createJuniorAnnual1a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1AAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorAnnual1b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1BAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorAnnual1c(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1CAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# Jss2 //////////////////////////////////////////					
	def createJuniorAnnual2a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2AAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorAnnual2b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2BAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorAnnual2c(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2CAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# Jss3 //////////////////////////////////////////
	def createJuniorAnnual3a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss3AAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorAnnual3b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss3BAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# Ss1 //////////////////////////////////////////
	def createSeniorAnnual1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS1Annual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,23),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 10:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 11:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				elif count == 12:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				elif count == 13:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# Ss2 //////////////////////////////////////////				
	def createSeniorAnnual2a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS2ArtAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,21),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				if count == 10:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				if count == 11:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createSeniorAnnual2b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS2ScienceAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,20),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 10:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

# Ss3 //////////////////////////////////////////
	def createSeniorAnnual3a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS3ArtAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createSeniorAnnual3b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS3ScienceAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 2:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 3:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 4:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 5:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 6:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 7:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 8:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 9:
					for count, col in enumerate(range(1,11),start=1):
						char=get_column_letter(col)
							
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTerm=ws[char+str(row)].value
						elif count == 4:
							SecondTerm=ws[char+str(row)].value
						elif count == 5:
							ThirdTerm=ws[char+str(row)].value
						elif count == 6:
							Total=ws[char+str(row)].value
						elif count == 7:
							Average=ws[char+str(row)].value
						elif count == 8:
							Grade=ws[char+str(row)].value
						elif count == 9:
							SubjectPosition=ws[char+str(row)].value
						elif count == 10:
							Remark=ws[char+str(row)].value
					AnnualResult.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTerm=FirstTerm,SecondTerm=SecondTerm,ThirdTerm=ThirdTerm,Total=Total,Average=Average,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				


# Model for Termly Result

class Result(models.Model):
	SN= models.CharField(max_length=100, blank=True)
	Name=models.CharField(max_length=200, blank=True,)
	Class=models.CharField(max_length=100, blank=True)
	Subject= models.CharField(max_length=100, blank=True)
	FirstTest= models.CharField(max_length=100, blank=True)
	SecondTest= models.CharField(max_length=100, blank=True)
	Project= models.CharField(max_length=100, blank=True)
	MidTermTest= models.CharField(max_length=100, blank=True)
	FirstAss= models.CharField(max_length=100, blank=True)
	SecondAss= models.CharField(max_length=100, blank=True)
	CA= models.CharField(max_length=100, blank=True)
	Exam= models.CharField(max_length=100, blank=True)
	Total= models.CharField(max_length=100, blank=True)
	Grade=models.CharField(max_length=100, blank=True)
	SubjectPosition=models.CharField(max_length=100, blank=True)
	Remark=models.CharField(max_length= 100, blank=True)
	
	
					
	def __str__(self):
		return str(self.Name +"-"+ self.Subject+"-"+self.Class)

# Model for the Classes
		
class Class(models.Model):
	Class=models.CharField(max_length=10, blank=True)
	
	def __str__(self):
		return str(self.Class)

# Model for the Newsletter Section & Assignments

class Newsletter(models.Model):
	newsletter= RichTextField(blank=True,null=True)

class Assignments(models.Model):
	Class= models.ForeignKey(Class, related_name='classes' , on_delete=models.CASCADE , blank = True,null=True)
	subject=models.CharField(max_length=200, blank=True)
	file=models.FileField(upload_to = 'media' ,blank = True)

	def __str__(self):
		return str(self.subject)

# Model for the Termly Students data

class Student(models.Model):
	Name=models.CharField(max_length=200, blank=True)
	Class=models.CharField(max_length=100, blank=True)
	TotalScore=models.CharField(max_length=100, blank=True)
	Totalnumber=models.CharField(max_length=100, blank=True)
	Average=models.CharField(max_length=100, blank=True)
	Position=models.CharField(max_length=100, blank=True)
	Term=models.CharField(max_length=100, blank=True)
	Academicsession=models.CharField(max_length=100, blank=True)
	
	
	
	def __str__(self):
		return str(self.Name+"-"+self.Class)

	# Termly Students Result

# Jss1 //////////////////////////////////////////
	def createJuniorResult1a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1ATermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorResult1b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1BTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorResult1c(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1CTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# Jss2 //////////////////////////////////////////					
	def createJuniorResult2a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2ATermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorResult2b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2BTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createJuniorResult2c(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2CTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# Jss3 //////////////////////////////////////////
	def createJuniorResult3a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss3ATermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)				
	def createJuniorResult3b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss3BTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)				
# Ss1 //////////////////////////////////////////
	def createSeniorResult1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS1Termly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,23),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
					
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 10:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				
				elif count == 11:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				elif count == 12:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				elif count == 13:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# Ss2 //////////////////////////////////////////				
	def createSeniorResult2a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS2ArtTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,21),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 10:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 11:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createSeniorResult2b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS2ScienceTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,20),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 10:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
# Ss3 //////////////////////////////////////////
	def createSeniorResult3a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS3ArtTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
	def createSeniorResult3b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS3ScienceTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			for count, row in enumerate(range(10,19),start=1):
				if count == 1:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 2:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 3:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 4:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 5:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 6:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 7:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 8:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)
				if count == 9:
					for count, col in enumerate(range(1,15),start=1):
						char=get_column_letter(col)
						
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							Subject=ws[char+str(row)].value
						elif count == 3:
							FirstTest=ws[char+str(row)].value
						elif count == 4:
							SecondTest=ws[char+str(row)].value
						elif count == 5:
							Project=ws[char+str(row)].value
						elif count == 6:
							MidTermTest=ws[char+str(row)].value
						elif count == 7:
							FirstAss=ws[char+str(row)].value
						elif count == 8:
							SecondAss=ws[char+str(row)].value
						elif count == 9:
							CA=ws[char+str(row)].value
						elif count == 10:
							Exam=ws[char+str(row)].value
						elif count == 11:
							Total=ws[char+str(row)].value
						elif count == 12:
							Grade=ws[char+str(row)].value
						elif count == 13:
							SubjectPosition=ws[char+str(row)].value
						elif count == 14:
							Remark=ws[char+str(row)].value
					Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition,Remark=Remark)

				



	# Model for the Excel Files 

class Excelfiles(models.Model):
	Excel= models.FileField(upload_to = 'media' ,blank = True)
	
	def __str__(self):
		return str(self.Excel)
	
	# Termly Students Data
# Jss1 //////////////////////////////////////////
	def createJuniorStudent1a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1ATermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent1b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1BTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent1c(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1CTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Jss2 //////////////////////////////////////////
	def createJuniorStudent2a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2ATermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent2b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2BTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent2c(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2CTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Jss3 //////////////////////////////////////////
	def createJuniorStudent3a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss3ATermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent3b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss3BTermly.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Ss1 //////////////////////////////////////////
	def createSeniorStudents1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS1Termly.xlsx')
		seniorClassExcel=[obj]
		for count,file in enumerate(seniorClassExcel,start=1):
			if count == 1:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K24'].value
					Average=ws['H24'].value
					TotalScore=ws['E24'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Ss2 //////////////////////////////////////////
	def createSeniorStudents2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS2ArtTermly.xlsx')
		obj2= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS2ScienceTermly.xlsx')
		seniorClassExcel=[obj,obj2]
		for count,file in enumerate(seniorClassExcel,start=1):
			if count == 1:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K22'].value
					Average=ws['H22'].value
					TotalScore=ws['E22'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Ss3 //////////////////////////////////////////	
	def createSeniorStudents3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS3ArtTermly.xlsx')
		obj2= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS3ScienceTermly.xlsx')
		seniorClassExcel=[obj,obj2]
		for count,file in enumerate(seniorClassExcel,start=1):
			if count == 1:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)

	# Annual Students Data 
# Jss1 //////////////////////////////////////////
	def createJuniorStudentAnnual1a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1AAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['P20'].value
			Average=ws['M20'].value
			TotalScore=ws['J20'].value
			Totalnumber=ws['k6'].value
			Term=ws['M6'].value
			Academicsession=ws['P6'].value
			AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudentAnnual1b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1BAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['P20'].value
			Average=ws['M20'].value
			TotalScore=ws['J20'].value
			Totalnumber=ws['k6'].value
			Term=ws['M6'].value
			Academicsession=ws['P6'].value
			AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudentAnnual1c(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss1CAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['P20'].value
			Average=ws['M20'].value
			TotalScore=ws['J20'].value
			Totalnumber=ws['k6'].value
			Term=ws['M6'].value
			Academicsession=ws['P6'].value
			AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Jss2 //////////////////////////////////////////
	def createJuniorStudentAnnual2a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2AAnnual1.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudentAnnual2b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2BAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudentAnnual2c(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss2CAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Jss3 //////////////////////////////////////////
	def createJuniorStudentAnnual3a(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss3AAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudentAnnual3b(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Jss3BAnnual.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			Name=str(ws['B4'].value).upper().strip()
			Class=ws['B6'].value
			Position=ws['K20'].value
			Average=ws['H20'].value
			TotalScore=ws['E20'].value
			Totalnumber=ws['F6'].value
			Term=ws['H6'].value
			Academicsession=ws['K6'].value
			AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# SS1 //////////////////////////////////////////
	def createSeniorStudentsAnnual1(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS1Annual.xlsx')
		seniorClassExcel=[obj]
		for count,file in enumerate(seniorClassExcel,start=1):
			if count == 1:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K24'].value
					Average=ws['H24'].value
					TotalScore=ws['E24'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Ss2 //////////////////////////////////////////	
	def createSeniorStudentsAnnual2(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS2AnnualArt.xlsx')
		obj2= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS2AnnualScience.xlsx')
		seniorClassExcel=[obj,obj2]
		for count,file in enumerate(seniorClassExcel,start=1):
			if count == 1:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K22'].value
					Average=ws['H22'].value
					TotalScore=ws['E22'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
# Ss3 //////////////////////////////////////////
	def createSeniorStudentsAnnual3(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS3AnnualArt.xlsx')
		obj2= s3.get_object(Bucket='okfswebbucket', Key='media/media/SS3AnnualScience.xlsx')
		seniorClassExcel=[obj,obj2]
		for count,file in enumerate(seniorClassExcel,start=1):
			if count == 1:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				binary_data = file['Body'].read()
				wb = load_workbook(io.BytesIO(binary_data))
				for sheet in wb:
					ws=wb[sheet.title]
					Name=str(ws['B4'].value).upper().strip()
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					AnnualStudent.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)


# function for Reading  Pins ////////////////////////////////////
	def readPin(self,*args,**kwargs) -> None:
		s3 = boto3.client('s3')
		obj= s3.get_object(Bucket='okfswebbucket', Key='media/media/Students_details_Main_2.xlsx') 
		binary_data = obj['Body'].read()
		wb = load_workbook(io.BytesIO(binary_data))
		for sheet in wb:
			ws=wb[sheet.title]
			for count, row in enumerate(range(6,59),start=1):
				if count == 1:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)

				if count == 2:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 3:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 4:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 5:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 6:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 7:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 8:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 9:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 10:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 11:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 12:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 13:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 14:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 15:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 16:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 17:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 18:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 19:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 20:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 21:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 22:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 23:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Result.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 24:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 25:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 26:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 27:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 28:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 29:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 30:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 31:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 32:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 33:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 34:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 35:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 36:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 37:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 38:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 39:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 40:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 41:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 42:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 43:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 44:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 45:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 46:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 47:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 48:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 49:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)
				if count == 50:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)   

				if count == 51:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)

				if count == 52:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)

				if count == 53:
					for count, col in enumerate(range(1,6),start=1):
						char=get_column_letter(col)	
						if count == 1:
							SN=ws[char+str(row)].value
						elif count == 2:
							student_name=ws[char+str(row)].value
						elif count == 3:
							student_pin=ws[char+str(row)].value
						elif count == 4:
							student_id=ws[char+str(row)].value
						elif count == 5:
							student_class=ws[char+str(row)].value
					Students_Pin_and_ID.objects.create(SN=SN,student_name=student_name,student_id=student_id,student_pin=student_pin,student_class=student_class)

# Model for the Pins		
class Students_Pin_and_ID(models.Model):
	SN=models.CharField(max_length=100, blank=True)
	student_name=models.CharField(max_length=100, blank=True, default="No name")
	student_id=models.CharField(max_length=100, blank=True,null=True)
	student_pin= models.BigIntegerField(blank=True,null=True)
	student_class=models.CharField(max_length=100, blank=True,null=True,default="No class")

	def __str__(self):
		return str(self.student_name)

	
		