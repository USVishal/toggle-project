from django.shortcuts import render,redirect,HttpResponse
from appschool.models import tbl_staff,tbl_students,tbl_teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def loginpage(request):
    return render(request,"loginpage.html")
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')

    data=authenticate(username=username,password=password)
    if data is not None and data.is_staff==0:      
         return render(request,"hr.html")
    elif data  is not None and data.is_staff == 1:
        return render(request,"teacherstaff.html")
    else:
        return HttpResponse ("User does not exist")
    

def newaccount(request):
    return render(request,"createaccount.html")

def create(request):
     if request.method == 'POST':
        p1=User()
        p1.first_name=request.POST.get('firstname')
        p1.last_name=request.POST.get('lastname') 
        p1.email=request.POST.get('email')
        p1.is_staff=request.POST.get('status')
        p1.username=request.POST.get('username')
        password=request.POST.get('password')
        p1.set_password(password)
        p1.save()
        return render(request,"loginpage.html")




def addteacher(request):
    return render(request,"addteacher.html")
def addstudents(request):
    return render(request,"addstudents.html")
def addstaff(request):
    return render(request,"addstaff.html")

def staff(request):
    p1=tbl_staff()
    p1.St_id=request.POST.get('St_id')
    p1.Name=request.POST.get('Name')    
    p1.Department=request.POST.get('Department')
    p1.Experience=request.POST.get('Experience')
    p1.Phone=request.POST.get('Phone')
    p1.Email=request.POST.get('Email')
    p1.Salary=request.POST.get('Salary')
    p1.save()
    return render(request,"addstaff.html")
def teacher1(request):
    p2=tbl_teacher()
    p2.T_id=request.POST.get('T_id')
    p2.Name=request.POST.get('Name')
    p2.Joining_Date=request.POST.get('Joining_Date')
    p2.Phone=request.POST.get('Phone')
    p2.Email=request.POST.get('Email')
    p2.Address=request.POST.get('Address')
    p2.Salary=request.POST.get('Salary')
    p2.Subject=request.POST.get('Subject')
    p2.save()
    return render(request,"addteacher.html")
def student(request):
    p3=tbl_students()
    p3.S_id=request.POST.get('S_id')
    p3.Name=request.POST.get('Name')
    p3.Student_class=request.POST.get('Student_class')
    p3.Marks=request.POST.get('Marks')
    p3.Status=request.POST.get('Status')
    p3.Parent_Name=request.POST.get('Parent_Name')
    p3.Contact_Number=request.POST.get('Contact_Number')
    p3.save()
    return render(request,"addstudents.html")

def  viewstaff(request):
    t1=tbl_staff.objects.all()
    return render(request,'viewstaff.html',{'data':t1})
def  viewteacher(request):
    t2=tbl_teacher.objects.all()
    return render(request,'viewteacher.html',{'data':t2})
def  viewstudent(request):
    t3=tbl_students.objects.all()
    return render(request,'viewstudent.html',{'data':t3})

def updatestaff(request,id):
    u1=tbl_staff.objects.get(id=id)
    return render(request,'updatestaff.html',{'data':u1})
def updateteacher(request,id):
    u2=tbl_teacher.objects.get(id=id)
    return render(request,'updateteacher.html',{'data':u2})
def updatestudent(request,id):
    u3=tbl_students.objects.get(id=id)
    return render(request,'updatestudent.html',{'data':u3})

def updatestaff1(request,id):
    p1=tbl_staff.objects.get(id=id)
    p1.St_id=request.POST.get('St_id')
    p1.Name=request.POST.get('Name')    
    p1.Department=request.POST.get('Department')
    p1.Experience=request.POST.get('Experience')
    p1.Phone=request.POST.get('Phone')
    p1.Email=request.POST.get('Email')
    p1.Salary=request.POST.get('Salary')
    p1.save()
    return redirect('/viewstaff/')
def updateteacher1(request,id):
    p2=tbl_teacher.objects.get(id=id)
    p2.T_id=request.POST.get('T_id')
    p2.Name=request.POST.get('Name')
    p2.Joining_Date=request.POST.get('Joining_Date')
    p2.Phone=request.POST.get('Phone')
    p2.Email=request.POST.get('Email')
    p2.Address=request.POST.get('Address')
    p2.Salary=request.POST.get('Salary')
    p2.Subject=request.POST.get('Subject')
    p2.save()
    return redirect('/viewteacher/')
def updatestudent1(request,id):
    p3=tbl_students.objects.get(id=id)
    p3.S_id=request.POST.get('S_id')
    p3.Name=request.POST.get('Name')
    p3.Student_class=request.POST.get('Student_class')
    p3.Marks=request.POST.get('Marks')
    p3.Status=request.POST.get('Status')
    p3.Parent_Name=request.POST.get('Parent_Name')
    p3.Contact_Number=request.POST.get('Contact_Number')
    p3.save()
    return redirect('/viewstudent/')

def deletestaff(request,id):
    d1=tbl_staff.objects.get(id=id)
    d1.delete()
    return redirect('/viewstaff')

def deleteteacher(request,id):
    d1=tbl_teacher.objects.get(id=id)
    d1.delete()
    return redirect('/viewteacher')

def deletestudent(request,id):
    d1=tbl_students.objects.get(id=id)
    d1.delete()
    return redirect('/viewstudent')

