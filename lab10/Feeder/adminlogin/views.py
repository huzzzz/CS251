from django.shortcuts import render
from adminlogin.forms import StudentForm, InstructorForm, CourseForm, FeedbackForm

def main_page(request):
    return render(request, 'register.html', {})

def addinstr(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if forms.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            form = InstructorForm()
    form = InstructorForm()
    return render(request, 'addinstr.html', {'form': form, 'registered': registered})

def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if forms.is_valid():
            user=form.save(COMMIT = FALSE)
            registered = True
        else:    
            form = CourseForm()
    form = CourseForm()
    return render(request, 'addcourse.html', {'form': form, 'registered': registered})

def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if forms.is_valid():
            user=form.save()
            user.save()
        else:    
            form = StudentForm()
    form = StudentForm()
    return render(request, 'addstudent.html', {'form': form, 'registered': registered})

def logout(request):
    logout()
    return render(request,'polls/', {})

