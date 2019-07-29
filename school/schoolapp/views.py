from django.shortcuts import render
from .forms import RegistrationFrom
from .forms import loginform
from  .models import Registrationdata
from .models import login_page
from  django.http.response import HttpResponse


# Create your views here.

def home_view(request):
    return render(request,'home.html')
def contact_view(request):
    return render(request,'contact.html')
def course_view(request):
    return render(request,'course.html')
def about_view(request):
    return render(request,'about.html')
def notifications_view(request):
    return render(request,'notifications.html')
def Registrations_view(request):
    if request.method=="POST":
        form=RegistrationFrom(request.POST)
        if form.is_valid():
            firstname=request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            Email = request.POST.get('Email')
            username = request.POST.get('username')
            password = request.POST.get('password')

            mobile = request.POST.get('mobile')

            data=Registrationdata(firstname=firstname,
                                lastname=lastname,
                                Email=Email,username=username,password=password,
                                mobile=mobile)
            data.save()
            form=RegistrationFrom()
            return render(request,'registrations.html',{'form':form})
        else:
            return  HttpResponse("invaild user data")
    else:
        form=RegistrationFrom()
        return render(request,'registrations.html',{'form':form})



def login_view(request):
    if request.method == "POST":
        lform = loginform(request.POST)
        if lform.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            uname =Registrationdata.objects.filter(username=username)
            pwd = Registrationdata.objects.filter(password=password)
            if uname and pwd:
                return HttpResponse("login is successful")

            else:
                lform = loginform()
                return render(request, 'loginpro.html', {'lform': lform})



            lform = loginform()
            return render(request,'login.html', {'lform': lform})
        else:
              return HttpResponse("invaild user data")
    else:
        lform = loginform()
        return render(request,'login.html', {'lform': lform})

