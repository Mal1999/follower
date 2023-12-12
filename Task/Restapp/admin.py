from django.contrib import admin
from . models import User
from . models import Student
from . models import Department
from . models import Course
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)