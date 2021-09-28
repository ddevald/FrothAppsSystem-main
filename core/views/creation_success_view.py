from django.shortcuts import render


def creation_success(request):
    return render(request, 'web/project-success.html')