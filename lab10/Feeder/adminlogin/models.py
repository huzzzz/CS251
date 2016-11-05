from django.db import models
from datetime import datetime
from polls.models import User

class Student (models.Model):
	roll_number = models.CharField(max_length=20, null=False, blank=False)
	full_name = models.CharField(max_length=200, blank=False, null=False)	
	email = models.EmailField(max_length=200, blank=False, unique=True)
	password = models.CharField(max_length=20)


	def __str__(self):
		return self.full_name

# class Instructor(models.Model):

# 	user = models.OneToOneField(User,on_delete = models.CASCADE)
# 	department = models.CharField(max_length= 50, blank=True)

# 	def __str__(self):
# 		return self.user

class FeedbackAns(models.Model):
	ans = models.CharField(max_length=200)

	def __str__(self):
		return self.ans

class FeedbackQuestions(models.Model):
	question= models.CharField(max_length=200, null=False)
	answers = models.ForeignKey(FeedbackAns)

	def __str__(self):
		return self.question


class Course(models.Model):

	SPRING = 'Spring'
	AUTUMN = 'Autumn'
	SEM_CHOICES = ((SPRING, 'Spring'),(AUTUMN,'Autumn'),)
	Course_code = models.IntegerField()
	Course_slot = models.IntegerField()
	Course_name = models.CharField(max_length=200)
	Course_students = models.ManyToManyField(Student)
	Course_Sem = models.CharField(choices = SEM_CHOICES, max_length= 10)
	Course_Instructor = models.OneToOneField(User, on_delete = models.CASCADE)
	Course_MidSemDate = models.DateField()
	Course_EndSemDate = models.DateField()
	
	def __str__(self):
		return self.name

class Feedback(models.Model):
	FEEDBACK_NAME_CHOICES = (('MidSem', 'MidSem'),('EndSem', 'EndSem'))
	feedback_name = models.CharField(max_length= 200, choices = FEEDBACK_NAME_CHOICES)
	feedback_course = models.ForeignKey(Course, on_delete= models.CASCADE)
	feedback_questions = models.ForeignKey(FeedbackQuestions)
	feedback_submissiondate = models.DateField()
	def __str__(self):
		return self.feedback_name

class Assignment(models.Model):
	assignment = models.ForeignKey(Course, on_delete= models.CASCADE)
	assignment_submissiondate=models.DateField()
	assignment_description=models.CharField(max_length=200,blank=False,null=False,default="Midsem feedback")
	def __str__(self):
		return self.assignment_description


