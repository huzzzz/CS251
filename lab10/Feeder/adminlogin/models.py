from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from polls.models import User

class Student (models.Model):
	MALE = 'Male'
	FEMALE = 'Female'
	OTHER = 'Other'
	GENDER_CHOICES = ((MALE,'Male'),(FEMALE,'Female'),(OTHER,'Other'),)
	roll_number = models.CharField(null=False, blank=False)0
	full_name = models.CharField(max_length=200, blank=False, null=False)	
	gender=models.CharField(max_length = 50, choices = GENDER_CHOICES, null=True)
	dob = models.DateField(null=True)
	email = models.EmailField(max_length=200, blank=False, unique=True)
	password = models.CharField(max_length=20)


	def __str__(self):
		return self.full_name

class Instructor(models.Model):

	user = models.OneToOneField(User,on_delete = models.CASCADE)
	department = models.CharField(max_length= 50)

	def __str__(self):
		return self.user

class FeedbackAns(models.Model):
	ans = models.CharField()

	def __str__(self):
		return self.ans

class FeedbackQuestions(models.Model):
	question= models.CharField()
	answers = models.ForeignKey(FeedbackAns)

	def __str__(self):
		return self.question


class Feedback(models.Model):
	FEEDBACK_NAME_CHOICES = (('MidSem', 'MidSem'),('EndSem', 'EndSem'))
	feedback_name = models.CharField(choices = FEEDBACK_NAME_CHOICES)
	feedback_questions = models.ForeignKey(FeedbackQuestions)
	feedback_submissiondate = models.DateField()
	def __str__(self):
		return self.feedback_name

class Assignment(models.Model):
	assignment=models.Foreignkey(Courses,on_delete=models.CASCADE)
	assignment_submissiondate=models.DateField()
	assignment_description=models.CharField(max_length=200,blank=False,null=False,default="Midsem feedback")
	def __str__(self):
		return self.assignment_description


class Course(models.Model):

	SPRING = 'Spring'
	AUTUMN = 'Autumn'
	SEM_CHOICES = ((SPRING, 'Spring'),(AUTUMN,'Autumn'),)
	Course_code = models.IntegerField(max_length=3)
	Course_slot = models.IntegerField(max_length=2)
	Course_name = models.CharField(max_length=200)
	Course_students = models.ManytoManyField(Student)
	Course_HalfSem = models.BooleanField(default = False)
	Course_Sem = models.CharField(choices = SEM_CHOICES, max_length= 10, default =(SPRING,'Spring'))
	Course_Instructor = models.OneToOneField(Instructor, on_delete = models.CASCADE)
	Course_MidSemDate = models.DateField()
	Course_EndSemDate = models.DateField()
	Course_feedback = models.ForeignKey(Feedback)
	
	def __str__(self):
		return self.name