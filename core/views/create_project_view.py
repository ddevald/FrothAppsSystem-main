from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views import View
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from core.forms import ProjectForm, MilestoneForm
from .creation_success_view import creation_success
from core.models import ProjectType
from djmoney.money import Money 

class create_project_view(View):
    @method_decorator(login_required)
    def get(self, request):
        users = get_user_model().objects.all().filter(is_staff=False)
        token = Token.objects.get_or_create(user=request.user)
        projectTypes = ProjectType.objects.all()
        context = {"users": users, "token": token[0], "projectTypes": projectTypes}
        return render(request, 'web/create_project.html', context)

    def post(self, request):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            data = {'amount': request.POST.getlist('milestone_amount'), 'name': request.POST.getlist('milestone_name')}
            for amount, name in zip(data['amount'], data['name']):
                data = {'project': project.id, 'amount': amount, 'name': name}
                milestone_form = MilestoneForm(data)
                if milestone_form.is_valid():
                    milestone_form.save()
                    context = {"project": project}
                    response = render(request, 'web/project-success.html', context=context)
                    return response
                else:
                    print(milestone_form.errors)
        context = {"errors": form.errors}
        return render(request, 'web/create_project.html')
