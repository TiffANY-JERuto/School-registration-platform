from django.shortcuts import render
from django.shortcuts import redirect
from .forms import StudentForm
from .models import Student
from django.http import HttpResponseBadRequest
# Create your views here.
def add_student(request):
	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()

		else:
			return HttpResponseBadRequest()
		# return redirect("list_students")		
	else:
	    form=StudentForm()	
	return render(request,"add_student.html",{"form":form})

def list_students(request):
	students=Student.objects.all()
	return render(request,"list_students.html",{"students":students})

def student_detail(request,pk):
	student=Student.objects.get(pk=pk)
	return render(request,"student_detail.html",{"student":student})

def edit_student(request,pk):
	student=Student.objects.get(pk=pk)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
		return redirect("list_students")
	else:
		form=StudentForm(instance=student)
	return render(request,"edit_student.html",{"form":form})	




	