from django.shortcuts import render
from polls.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def adminlogin(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('adminlogin/adminPage')
    # else: 
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:                       
                if user.is_active:
                    if user.is_superuser:
                        # print("here2")
                        login(request, user)
                        return HttpResponseRedirect('/adminlogin/adminPage')
                    else:
                        # print("her2")
                        return HttpResponseRedirect('/polls/main_page/')
                else:
                    # print("he2")
                    return HttpResponse('Wrong')
                return HttpResponse('*Please enter valid Details')                
    else:
        form = UserForm()
    return render(request, 'login.html',  {'form':form})

def register(request):
    registered = False 
    if request.method == 'POST':
        form = UserForm(request.POST)   
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:    
            form = UserForm()
    form = UserForm()
    return render(request, 'register.html', {'form': form, 'registered': registered})

def mainpage(request):
    return render(request, 'mainpage.html', {})