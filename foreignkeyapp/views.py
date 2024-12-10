from django.shortcuts import render, redirect
from .models import Course, Student

def home(request):
    return render(request, 'home.html')

def add_course(request):
    if request.method == "POST":
        course_name = request.POST['course']
        fee = request.POST['fee']
        Course.objects.create(course_name=course_name, fee=fee)
        return redirect('home')
    return render(request, 'add_course.html')

def add_student(request):
    courses = Course.objects.all()
    if request.method == "POST":
        student_name = request.POST['sname']
        student_address = request.POST['address']
        student_age = request.POST['age']
        joining_date = request.POST['jdate']
        course = Course.objects.get(id=request.POST['sel'])
        Student.objects.create(
            student_name=student_name,
            student_address=student_address,
            student_age=student_age,
            joining_date=joining_date,
            course=course
        )
        return redirect('show_details')
    return render(request, 'add_student.html', {'courses': courses})

def show_details(request):
    students = Student.objects.all()
    courses = Course.objects.all() 
    return render(request, 'show_details.html', {'students': students, 'courses': courses})

def editpage(request, id):
    student = Student.objects.get(id=id)  
    courses = Course.objects.all() 

    if request.method == 'POST':
        student.student_name = request.POST['name']
        student.student_address = request.POST['address']
        student.student_age = request.POST['age']
        student.joining_date = request.POST['jdate']
        student.course = Course.objects.get(id=request.POST['sel'])
        student.save()  
        return redirect('show_details')

    return render(request, 'edit_student.html', {'student': student, 'courses': courses})  


def delete(request, id):
    student = Student.objects.get(id=id) 
    student.delete()
    return redirect('show_details')
