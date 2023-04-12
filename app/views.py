from django.shortcuts import render

# Create your views here.

from app.models import *

def display_student(request):
    LOS=Student.objects.all()
    d={'std':LOS}

    return render(request,'display_student.html',context=d)


def display_studentdetails(request):
    LOD=Studentdetails.objects.all()

    Studentdetails.objects.filter(rollno='18jn1a0599').update(address='podalkur')

    Studentdetails.objects.all().update(address='podalkur')

    d={'details':Studentdetails.objects.all()}

    return render(request, 'display_studentdetails.html',d)


def display_teacher(request):
    LOT=Teacherdetails.objects.all()
    d={'teacher':LOT}

    return render(request,'display_teacher.html',d)

def update(request):

    Studentdetails.objects.all().update(address='nellore')

    
    student = Student.objects.get_or_create(slno='7', rollno='18jn1a0401', sname='peter')[0]
    student.save()

    Studentdetails.objects.update_or_create(rollno=student,
        defaults={
            'contactnumber': 1234567890,
            'address': 'Nellore',
            'teachername': 'kajhfmk'
        }
    )

    

    d={'details':Studentdetails.objects.all()}
    return render(request,'display_studentdetails.html',d)
