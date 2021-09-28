from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Project
import datetime


@login_required(login_url='/web/login')
def projects_view(request):
    # user = request.user
    Project_list = Project.objects.all()
    return render(request, 'web/projects.html', {'Project_list': Project_list,})

# def calculateDueDay(x):
#     today = datetime.date.today()
#     remainingDays = x - today
#
#     return render(request, 'web/projects.html', {'remainingDays': remainingDays,})
