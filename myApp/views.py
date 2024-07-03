from django.shortcuts import render
from myApp.models import student

# Create your views here.
def myView(request):
    s=student.objects.all()
    print(type(s))
    d={'stud':s}
    return render(request,'myApp/1.html',d).
