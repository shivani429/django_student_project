from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .models import Student    
from demoapp.forms import StudentForm

       
# Student Functions
def student_list(request):
    student_list = Student.objects.all()
    d = {'student_list': student_list}
    return render(request,'index.html',d)
    
def delete_student(request,id):
    stu = Student.objects.get(id=id)
    stu.delete()
    return redirect('student_list')

def update_student(request, id):
    stu = Student.objects.get(id=id)
    if request.method == 'POST':        
        Name = request.POST.get('name')
        roll_no_=request.POST.get('Roll_no')
        class_no_ = request.POST.get('class_no')
        address = request.POST.get('Address')
        print(Name)
        print(roll_no_)
        print(class_no_)
        print(address)
        stu.Roll_no = roll_no_
        stu.name = Name
        stu.class_no = class_no_
        stu.Address = address
        stu.save()
        return redirect('student_list',)
    else:
    
        d = {'stu': stu}
        return render(request,'update.html',d)

def add_student(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        roll_no_=request.POST.get('Roll_no')
        class_no_ = request.POST.get('class_no')
        address = request.POST.get('Address')
        print(Name)
        print(roll_no_)
        print(class_no_)
        print(address)
        Student.objects.create(Roll_no=roll_no_,name=Name,class_no=class_no_,Address=address)
        return redirect('student_list')
    else:
        form = StudentForm()
        return render(request, 'update.html', {"form": form})


