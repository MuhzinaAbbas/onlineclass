from django.shortcuts import redirect,render
from django.contrib import messages
from classapp.models import student,user

# Create your views here.
def home(request):
     if 'Email' in request.session:
        exist_user=request.session['Email']
        user=student.objects.get(Email=exist_user)
        print(exist_user)
        return render(request,"home.html",{'exist_user':exist_user,'user':user})
     return render(request,"home.html")
def register(request):
    if request.method=='POST':
        nam=request.POST['Name']
        emi=request.POST['Email']
        pas=request.POST['Password']
        add=request.POST['Address']
        num=request.POST['Number']
        crs=request.POST['Course']
        img=request.FILES.get('stdimage') 
        student.objects.create(Name=nam,Email=emi,Password=pas,Address=add,Number=num,Course=crs,stdimage=img)
        return redirect('login')
    return render(request,'register.html') 
def login(request):
    if request.method=='POST':
        emi=request.POST['Email']
        pas=request.POST['Password']
        users=student.objects.filter(Email=emi,Password=pas)
        if users:
            request.session['Email']=emi
            print(request.session['Email'])
            return redirect('/')
        else:
            messages.error(request,"invalid")
    return render(request,'login.html')
def logout(request):
    del request.session['Email']
    return redirect('/')

def enquiry(request):
    detail=student.objects.all()
    return render(request,'enquiry.html',{'detail':detail})
def view(request,id):
    detail=student.objects.get(id=id)
    return render(request,"view.html",{'detail':detail})
def delete(request,id):
    detail=student.objects.get(id=id)
    detail.delete()
    return redirect('enq')
def update(request,id):
    detail=student.objects.get(id=id)
    if request.method=="POST":
            nam=request.POST['Name']
            emi=request.POST['Email']
            pas=request.POST['Password']
            add=request.POST['Address']
            num=request.POST['Number']
            crs=request.POST['Course']
            img=request.FILES.get['stdimage']
            detail.Name=nam
            detail.Email=emi
            detail.Password=pas
            detail.Address=add
            detail.Number=num
            detail.Course=crs
            detail.stdimage=img
            detail.save()
    return render(request,"update.html",{'detail':detail})
def contact(request):
    if request.method=='POST':
        nam=request.POST['C_Name']
        emi=request.POST['Email']
        pas=request.POST['Password']
        crs=request.POST['Course']
        msg=request.POST['Message']
        user.objects.create(C_Name=nam,Email=emi,Password=pas,Course=crs,Message=msg)
        return redirect('/')
    return render(request,'contact.html') 


def course(request):
    return render(request,'course.html')
def index1(request):
    return render(request,'index1.html')
def about(request):
    return render(request,'about.html')
def admin(request):
    return render(request,'admin.html')