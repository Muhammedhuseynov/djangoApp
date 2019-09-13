from django.shortcuts import render, redirect
from .forms import UserForm, UserUpdate,ProfileUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            name = forms.cleaned_data.get('username')
            messages.success(request,f'GOSHULDYN: {name} . \n LOGININI YAZYP GIRIBER!')
            return redirect('login')
    else:
        forms = UserForm()        
    context = {
        'form':forms
    }
    return render(request,'register.html',context)
@login_required
def profile(request):
    if request.method == 'POST':
        up_user = UserUpdate(request.POST,instance=request.user)
        up_profile = ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)
        if up_user.is_valid() and up_profile.is_valid():
            up_user.save()
            up_profile.save()
            
    else:
        up_user = UserUpdate(instance=request.user)
        up_profile = ProfileUpdate(instance=request.user.profile)
    context = {
        'up_user':up_user,
        'up_profile':up_profile 
    }
    return render(request,'profile.html',context)