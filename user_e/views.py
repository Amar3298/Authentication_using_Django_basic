from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
def index(request):
    return render(request,'user_e/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'registration/registration.html',context)

def logout_user(request):
    logout(request)
    return redirect("index")