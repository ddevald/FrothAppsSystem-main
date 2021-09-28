from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Project, Milestone, Expense
import datetime


@login_required(login_url='/web/login')
def projects_page_view(request, pk):
    # user = request.user
    # idN = id.split(':')
    # project_obj = idN[0].objects.all()
    # project_object = Project.objects.all()
    # for projoct in project_object:
    #     if projoct == id
    #         project_obj = projoct
    project = Project.objects.get(id=pk)
    milestone_list = project.milestones.all()
    # milestone_list = Milestone.objects.get(id=pk)
    expense_list = project.invoice.all()
    return render(request, 'web/projects-page.html', {'project_obj': project, 'milestone_list': milestone_list, 'expense_list': expense_list})
