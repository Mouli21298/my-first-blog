from django.shortcuts import render
from .models import StudentRecords
# Create your views he
def stu_list(request):
	sturec=StudentRecords.objects.all()
	return render(request,'student/stu_list.html',{'sturec':sturec})
