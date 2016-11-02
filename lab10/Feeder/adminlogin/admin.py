from django.contrib import admin
from adminlogin.models import Student, Instructor, FeedbackAns, FeedbackQuestions, Feedback, Assignment, Course

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(FeedbackQuestions)
admin.site.register(Feedback)
admin.site.register(FeedbackAns)
# Register your models here.
