from django.db import models
import secrets
from openpyxl import Workbook,load_workbook
from openpyxl.utils import get_column_letter
import os
import random
from ckeditor.fields import RichTextField



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
		
class Class(models.Model):
	Class=models.CharField(max_length=10, blank=True)
	
	def __str__(self):
		return str(self.Class)

class Newsletter(models.Model):
	newsletter= RichTextField(blank=True,null=True)
	
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
	
	def createJuniorResult1a(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss1A_Result_Sheet_Final.xlsx']
		for file in juniorClassExcel:
			filename = file
			filepath = BASE_DIR + '/media/media/' + filename
			wb=load_workbook(filepath)
			for sheet in wb:
				ws=wb[sheet.title]
				Name=ws['B4'].value
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
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss1B_Result_Sheet_Final_2a.xlsx']
		for file in juniorClassExcel:
			filename = file
			filepath = BASE_DIR + '/media/media/' + filename
			wb=load_workbook(filepath)
			for sheet in wb:
				ws=wb[sheet.title]
				Name=ws['B4'].value
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
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss1C_Result_Sheet_Final.xlsx']
		for file in juniorClassExcel:
			filename = file
			filepath = BASE_DIR + '/media/media/' + filename
			wb=load_workbook(filepath)
			for sheet in wb:
				ws=wb[sheet.title]
				Name=ws['B4'].value
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
						
	def createJuniorResult2a(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss2A_Result_sheet_Final_1.xlsx']
		for file in juniorClassExcel:
			filename = file
			filepath = BASE_DIR + '/media/media/' + filename
			wb=load_workbook(filepath)
			for sheet in wb:
				ws=wb[sheet.title]
				Name=ws['B4'].value
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
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss2B_Result_Sheet_1.xlsx']
		for file in juniorClassExcel:
			filename = file
			filepath = BASE_DIR + '/media/media/' + filename
			wb=load_workbook(filepath)
			for sheet in wb:
				ws=wb[sheet.title]
				Name=ws['B4'].value
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

	def createJuniorResult3(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss3_Result_Sheet-Final_2.xlsx']
		for file in juniorClassExcel:
			filename = file
			filepath = BASE_DIR + '/media/media/' + filename
			wb=load_workbook(filepath)
			for sheet in wb:
				ws=wb[sheet.title]
				Name=ws['B4'].value
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
	
	def createSeniorResult1(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		SeniorClassExcel='Ss1_Result_sheet-Final2.xlsx'
		filename = SeniorClassExcel
		filepath = BASE_DIR + '/media/media/' + filename
		wb=load_workbook(filepath)
		for sheet in wb:
			ws=wb[sheet.title]
			Name=ws['B4'].value
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
					
	def createSeniorResult2(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		SeniorClassExcel='Ss2_Result_sheet-Final2a.xlsx'
		filename = SeniorClassExcel
		filepath = BASE_DIR + '/media/media/' + filename
		wb=load_workbook(filepath)
		for sheet in wb:
			ws=wb[sheet.title]
			Name=ws['B4'].value
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
				
				
class Excelfiles(models.Model):
	Excel= models.FileField(upload_to = 'media' ,blank = True)
	
	def __str__(self):
		return str(self.Excel)
		
	def createJuniorStudent1a(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss1A_Result_Sheet_Final.xlsx']
		for count,file in enumerate(juniorClassExcel,start=1):
			if count == 1:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 3:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 4:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 5:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 6:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent1b(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss1B_Result_Sheet_Final_2a.xlsx']
		for count,file in enumerate(juniorClassExcel,start=1):
			if count == 1:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 3:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 4:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 5:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 6:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent1c(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss1C_Result_Sheet_Final.xlsx']
		for count,file in enumerate(juniorClassExcel,start=1):
			if count == 1:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 3:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 4:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 5:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 6:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent2a(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss2A_Result_sheet_Final_1.xlsx']
		for count,file in enumerate(juniorClassExcel,start=1):
			if count == 1:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 3:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 4:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 5:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 6:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent2b(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss2B_Result_Sheet_1.xlsx']
		for count,file in enumerate(juniorClassExcel,start=1):
			if count == 1:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 3:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 4:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 5:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 6:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
	def createJuniorStudent3(self,*args,**kwargs) -> None:
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		juniorClassExcel=['Jss3_Result_Sheet-Final_2.xlsx']
		for count,file in enumerate(juniorClassExcel,start=1):
			if count == 1:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 2:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 3:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 4:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 5:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
			elif count == 6:
				filename = file
				filepath = BASE_DIR + '/media/media/' + filename
				wb=load_workbook(filepath)
				for sheet in wb:
					ws=wb[sheet.title]
					Name=ws['B4'].value
					Class=ws['B6'].value
					Position=ws['K20'].value
					Average=ws['H20'].value
					TotalScore=ws['E20'].value
					Totalnumber=ws['F6'].value
					Term=ws['H6'].value
					Academicsession=ws['K6'].value
					Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)								
	def createSeniorStudents(self,*args,**kwargs) -> None:
			BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			seniorClassExcel=['Ss1_Result_sheet-Final2.xlsx','Ss2_Result_sheet-Final2a.xlsx']
			for count,file in enumerate(seniorClassExcel,start=1):
				if count == 1:
					filename = file
					filepath = BASE_DIR + '/media/media/' + filename
					wb=load_workbook(filepath)
					for sheet in wb:
						ws=wb[sheet.title]
						Name=ws['B4'].value
						Class=ws['B6'].value
						Position=ws['K24'].value
						Average=ws['H24'].value
						TotalScore=ws['E24'].value
						Totalnumber=ws['F6'].value
						Term=ws['H6'].value
						Academicsession=ws['K6'].value
						Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
				elif count == 2:
					filename = file
					filepath = BASE_DIR + '/media/media/' + filename
					wb=load_workbook(filepath)
					for sheet in wb:
						ws=wb[sheet.title]
						Name=ws['B4'].value
						Class=ws['B6'].value
						Position=ws['K24'].value
						Average=ws['H24'].value
						TotalScore=ws['E24'].value
						Totalnumber=ws['F6'].value
						Term=ws['H6'].value
						Academicsession=ws['K6'].value
						Student.objects.create(Name=Name,Class=Class,Position=Position,Average=Average,TotalScore=TotalScore,Totalnumber=Totalnumber,Term=Term,Academicsession=Academicsession)
						

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
		
		