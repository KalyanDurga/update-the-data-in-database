from django.db import models

# Create your models here.

class Student(models.Model):
    slno=models.IntegerField()
    rollno=models.CharField(max_length=15,primary_key=True)
    sname=models.CharField(max_length=25)

    def __str__(self):
        return self.rollno
    

class Studentdetails(models.Model):
    rollno=models.ForeignKey(Student,on_delete=models.CASCADE)
    address=models.CharField(max_length=30)
    contactnumber=models.CharField(max_length=15)
    teachername=models.CharField(max_length=20)

    def __str__(self):
        return str(self.teachername)
    
class Teacherdetails(models.Model):
    teacherid=models.IntegerField()
    teachername=models.ForeignKey(Studentdetails,on_delete=models.CASCADE)
    subject=models.CharField(max_length=15,unique=True)
    
    def __str__(self):
        return str(self.teachername)

    
    

