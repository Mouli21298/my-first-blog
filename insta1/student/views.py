from django.shortcuts import render

# Create your views he
def stu_list(request):
	return render(request,'student/stu_list.html')
