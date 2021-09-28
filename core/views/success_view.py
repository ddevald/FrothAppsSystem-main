from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def success_view(request):
    # user = request.user
    # POST /user/me , RESPONSE object, avatar

    return render(request, 'web/success.html')
