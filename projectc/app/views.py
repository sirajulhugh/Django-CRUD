import os
from django.shortcuts import render,redirect
from app.models import Student

# Create your views here.
def student(request):
    return render(request,"student.html")

def adddetails(request):
    if request.method== 'POST':
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        age=request.POST['age']
        corecourse=request.POST['cc']
        address=request.POST['address']
        date=request.POST['date']
        image=request.FILES.get('image')

        st=Student(firstname=f_name,lastname=l_name,age=age,corecourse=corecourse,address=address,dateofjoin=date,images=image)
        st.save()

    
    return redirect("viewtable")

def viewtable(request):
    std=Student.objects.all()
    return render(request,"viewtable.html",{'student':std})

def student_detail(request, id):
    student=Student.objects.get(id=id)
    return render(request, 'student_detail.html', {'student': student})

def edit(request,id):
    std=Student.objects.get(id=id)
    return render(request,"edit.html",{'student':std})

def editdetails(request,id):
    if request.method=="POST":
        svd=Student.objects.get(id=id)
        svd.firstname=request.POST.get('fname')
        svd.lastname=request.POST.get('lname')
        svd.age=request.POST.get('age')
        svd.corecourse=request.POST.get('cc')
        svd.address=request.POST.get('address')
        svd.dateofjoin=request.POST.get('date')
        new_image=request.FILES.get('image')
        if new_image:
            if svd.images:
                os.remove(svd.images.path)
            svd.images = new_image
        try:
            svd.save()
            print("Product saved successfully")
        except Exception as e:
            print("Error saving product:", e)
        return redirect('viewtable')
    
        
    # return render(request,"edit.html")

def deletedetails(request,id):
    svd=Student.objects.get(id=id)
    svd.delete()
    return redirect('viewtable')

def home(request):
    return render(request,"home.html")

def page1(request):
    return render(request,"page1.html")
    
