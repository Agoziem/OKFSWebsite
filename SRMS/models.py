from django.db import models
import secrets
from openpyxl import Workbook,load_workbook
from openpyxl.utils import get_column_letter
import os
import random



class Result(models.Model):
	SN= models.CharField(max_length=100, blank=True)
	Name=models.CharField(max_length=200, blank=True)
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
		return str(self.Name +"-"+ self.Subject)
		
class Class(models.Model):
	Class=models.CharField(max_length=10, blank=True)
	
	def __str__(self):
		return str(self.Class)

class Newsletter(models.Model):
	Picture= models.ImageField(upload_to = 'assets' ,blank = True)
	
class Student(models.Model):
	Name=models.CharField(max_length=200, blank=True)
	Class=models.CharField(max_length=100, blank=True)
	Position=models.CharField(max_length=100, blank=True)
	Average=models.CharField(max_length=100, blank=True)
	Term=models.CharField(max_length=100, blank=True)
	Academicsession=models.CharField(max_length=100, blank=True)
	
	
	def __str__(self):
		return str(self.Name+"-"+self.Class)
	
	def createJuniorResult(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss1Aa.xlsx','Jss1Ba.xlsx','Jss1Ca.xlsx','Jss2Aa.xlsx','Jss2Ba.xlsx','Jss3a.xlsx']
		for file in juniorClassExcel:
			filename = file
			filepath = BASE_DIR + '/media/media/' + filename
			wb=load_workbook(filepath)
			for sheet in wb:
				ws=wb[sheet.title]
				Name=ws['B4'].value
				Class=ws['B6'].value
				for count, row in enumerate(range(10,21),start=1):
					if count == 1:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 2:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 3:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 4:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 5:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 6:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 7:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 8:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 9:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 10:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 11:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
						
	def createSeniorResult(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		SeniorClassExcel=['Ss1a.xlsx','Ss2b.xlsx']
		for file in SeniorClassExcel:
			filename = file
			filepath = BASE_DIR + '/media/media/' + filename
			wb=load_workbook(filepath)
			for sheet in wb:
				ws=wb[sheet.title]
				Name=ws['B4'].value
				Class=ws['B6'].value
				for count, row in enumerate(range(10,24),start=1):
					if count == 1:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 2:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 3:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 4:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 5:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 6:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 7:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 8:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 9:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 10:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
					elif count == 11:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					elif count == 12:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					elif count == 13:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					elif count == 14:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					elif count == 15:
						for count, col in enumerate(range(1,14),start=1):
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
							#elif count == 14:
								#Remark=ws[char+str(row)].value
						Result.objects.create(SN=SN,Name=Name,Class=Class,Subject=Subject,FirstTest=FirstTest,SecondTest=SecondTest,Project=Project,MidTermTest=MidTermTest,FirstAss=FirstAss,SecondAss=SecondAss,CA=CA,Exam=Exam,Total=Total,Grade=Grade,SubjectPosition=SubjectPosition)
					
	
class Excelfiles(models.Model):
	Excel= models.FileField(upload_to = 'media' ,blank = True)
	
	def __str__(self):
		return str(self.Excel)
		
	def createJuniorStudents(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss1Aa.xlsx','Jss1Ba.xlsx','Jss1Ca.xlsx','Jss2Aa.xlsx','Jss2Ba.xlsx','Jss3a.xlsx']
		for count,file in enumerate(juniorClassExcel,start=1):
			if count == 1:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K22'].value
					Average=ws['H22'].value
					
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K22'].value
					Average=ws['H22'].value
					
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,Term=Term,Academicsession=Academicsession)
			elif count == 3:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K22'].value
					Average=ws['H22'].value
					
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,Term=Term,Academicsession=Academicsession)
			elif count == 4:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K22'].value
					Average=ws['H22'].value
					
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,Term=Term,Academicsession=Academicsession)
			elif count == 5:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K22'].value
					Average=ws['H22'].value
					
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,Term=Term,Academicsession=Academicsession)
			elif count == 6:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K22'].value
					Average=ws['H22'].value
					
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,Term=Term,Academicsession=Academicsession)
					
	def createSeniorStudents(self,*args,**kwargs) -> None:
			BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			seniorClassExcel=['Ss1a.xlsx','Ss2b.xlsx']
			for count,file in enumerate(seniorClassExcel,start=1):
				if count == 1:
					filename = file
					filepath = BASE_DIR + '/media/media/' + filename
					wb=load_workbook(filepath)
					for sheet in wb:
						ws=wb[sheet.title]
						Name=ws['B4'].value
						Class=ws['B6'].value
						Position=ws['K26'].value
						Average=ws['H26'].value
						Term=ws['H6'].value
						Academicsession=ws['K6'].value
						Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,Term=Term,Academicsession=Academicsession)
				elif count == 2:
					filename = file
					filepath = BASE_DIR + '/media/media/' + filename
					wb=load_workbook(filepath)
					for sheet in wb:
						ws=wb[sheet.title]
						Name=ws['B4'].value
						Class=ws['B6'].value
						Position=ws['K26'].value
						Average=ws['H26'].value
						Term=ws['H6'].value
						Academicsession=ws['K6'].value
						Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,Term=Term,Academicsession=Academicsession)
	


class Pin(models.Model):
	student=models.CharField(max_length=100, blank=True)
	pin= models.BigIntegerField(blank=False)
	
	def generatePin(self,*args,**kwargs):
		i=0
		while i <= 300:
			StudentPin= str(random.randint(0, 99999999999999)).rjust(14, '0')
			pin=StudentPin
			Pin.objects.create(pin=pin)
			i=i+1
			
	def __str__(self):
		return str(self.student)
		
	