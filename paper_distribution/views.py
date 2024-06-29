from django.shortcuts import render, redirect
# from .forms import NewExamForm
from .models import Exams

# Create your views here. 
def new_exam(request):
	if request.method == 'POST':
		print(request.POST)
		print(request.FILES)
		data = request.POST
		exam = Exams.objects.create(
            name = data.get("name"),
            schedule = data.get("schedule"),
            examiner = data.get("examiner"),
            invigilator = data.get("invigilator"),
            file = request.FILES.get('file')
        )
		exam.save()
		
	# context['form'] = form
	return render(request, "new_exam.html")