from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    courses = models.ForeignKey('Course', on_delete=models.CASCADE)
    purpose = models.CharField(max_length=50,choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
    materials_provide = models.CharField(max_length=50,
        choices=[('notebook', 'Debit Note Book'), ('pen', 'Pen'), ('exam-papers', 'Exam-papers')])

class Material(models.Model):
        name = models.CharField(max_length=50)

class Department(models.Model):
    name = models.CharField(max_length=50)



class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)


