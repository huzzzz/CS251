from django.contrib.auth.models import User
from django import forms
from adminlogin.models import Student, Course, Feedback, FeedbackQuestions

class StudentForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Student
		fields = ('full_name', 'roll_number', 'email', 'password')

# class InstructorForm(forms.ModelForm):

# 	class Meta:
# 		model = Instructor
# 		fields =('department',)

class CourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('Course_name','Course_code','Course_slot', 'Course_Sem', 'Course_Instructor', 'Course_MidSemDate', 'Course_EndSemDate')	

class FeedbackForm(forms.ModelForm):

	class Meta:
		model = Feedback
		fields = ('feedback_name', 'feedback_questions',)

class FeedbackQuestions(forms.ModelForm):

	class Meta:
		model = FeedbackQuestions
		fields = ('question',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')