from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TeacherForm
from .models import Teacher
from django.http import HttpResponseBadRequest
# Create your views here.
def add_teacher(request):
    if request.method=="POST":
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponseBadRequest()
        # return redirect("list_teachers")
    else:
        form=TeacherForm()
    return render(request,"add_teacher.html",{"form":form})                                             
    # return render(request,"add_teacher.html",{"form":form}),
def list_teachers(request):
    teachers=Teacher.objects.all()
    return render(request,"list_teachers.html",{"teachers":teachers})

def teacher_detail(request,pk):
    teacher=Teacher.objects.get(pk=pk)
    return render(request,"teacher_detail.html",{"teacher":teacher})

def edit_teacher(request,pk):
    teacher=Teacher.objects.get(pk=pk)
    if request.method == "POST":
        form=TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
        return redirect("list_teachers")            
    else:
        form=TeacherForm(instance=teacher)
    return render(request,"edit_teacher.html",{"form":form})    