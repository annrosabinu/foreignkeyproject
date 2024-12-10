from django.contrib import admin
from foreignkeyapp.models import Course,Student
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)