from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import Sqtable_cont,Products
from app.forms import Htform



# Create your views here.
@login_required(login_url='/login')
def productview(request):
    pd=Products.objects.all()
    return render(request,'app/products.html',{'pd':pd})


def contact(request):
    form=Htform()
    if request.method == "POST":
        form=Htform(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return redirect('/contact')
        return render(request,'app/contact.html')
    return render(request,'app/contact.html',{'form':form})


@login_required(login_url='/login')
def home(request):
    return render(request,'app/home.html')


@login_required(login_url='/login')
def index(request):
    return render(request,'app/index.html')

def loginhandle(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        myuser = authenticate(username=email,password=password)
        if myuser is not None:
            login(request, myuser)
            messages.info(request,"login succsess!!")
            return render(request,'app/home.html')
        else:
            messages.warning(request,"incorrect credentials!")
            return redirect('/login')
    return render(request, 'app/login.html')

def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        conform_password=request.POST['password1']
        if password!=conform_password:
            messages.warning(request,"passwords not matched!")
            
            return render(request,'app/signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,"user already exists!!")
                return render(request,'app/signup.html')

        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
        user.save()
        return redirect('/login')


        messages.success(request,"account created sucessfully")
    return render(request,'app/signup.html')

def logoutview(request):
    logout(request)
    messages.warning(request,"logout succsess!!")
    return redirect('/login')
    return render(request,'app/logout.html')
