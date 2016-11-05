from django.shortcuts import render, redirect
from adminlogin.forms import StudentForm, CourseForm, FeedbackForm,UserForm
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect, HttpResponse

def main_page(request):
    form=UserForm()
    return render(request,'login.html', {'form':form})
    # return redirect('admin_poll');

def check(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:                       
                if user.is_active:
                    if user.is_superuser:
                        print("here2")
                        login(request, user)
                        return render(request, 'this.html', {})
                    else:
                        print("her2")
                        return HttpResponse('Wrong')
                else:
                    print("he2")
                    return HttpResponse('Wrong')
                return HttpResponse('*Please enter valid Details')                
    else:
        form = UserForm()
    return render(request, 'login.html',  {'form':form})
    # return render(request, 'this.html', {})
    # return redirect('admin_poll');

def adminPage(request):
    return render(request,'adminpage.html')

def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if forms.is_valid():
            user=form.save(COMMIT = FALSE)
            registered = True
        else:    
            form = CourseForm()
    form = CourseForm()
    return render(request, 'course.html', {'form': form, 'registered': registered})

# def addinstructor(request):
# 	if request.user.is_authenticated:
#        	if request.user.is_staff:
#             instructor_registered=0
#             if request.method == 'POST':
#                 user=UserForm(request.POST)
#                 if user.is_valid():
#                     newuser=register.save(commit=False)
#                     newuser.set_password(register.cleaned_data['password'])
#                     newuser.username=newuser.email
#                     newuser.save()
#                     instructor_registered=1
#                 else:
#                      return render(request,'add_instructor.html',{'register':register,'registerprofile':registerprofile,'instructor_registered':instructor_registered})
#             register=UserForm()
#             registerprofile=UserProfileForm()
#             return render(request,'add_instructor.html',{'register':register,'registerprofile':registerprofile,'instructor_registered':instructor_registered})
#         else:
#             return HttpResponse('Instructor logged in site under construction')    
#     else:
#         return HttpResponseRedirect("")   

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

def adminlogout(request):
    logout(request)
    return HttpResponseRedirect('/')
    