from django.contrib.auth.models import User
from django import forms
from adminlogin.models import Student, Course, Instructor, Feedback, FeedbackQuestions

class StudentForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Student
		fields = ('full_name', 'roll_number', 'department', 'email', 'password', 'gender', 'dob')

class InstructorForm(forms.ModelForm):

	class Meta:
		model = Instructor
		fields =('department',)

class CourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('name','code','slot','HalfSem', 'Sem', 'Course_Instructor', 'MidSemDate', 'EndSemDate')	

class FeedbackForm(forms.ModelForm):

	class Meta:
		model = Feedback
		fields = ('feedback_name', 'questions',)

class FeedbackQuestions(forms.ModelForm):

	class Meta:
		model = FeedbackQuestions
		fields = ('question')
