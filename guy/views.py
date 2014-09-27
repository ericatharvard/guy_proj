from django.http import Http404
from django.shortcuts import render

from guy.models import Guy

def index(request):
    #guys = Guy.objects.all()
    guys = Guy.objects.filter(owner=request.user.id)
    lu = {'guys': guys}
    return render(request, 'guy/index.html', lu)

def display(request, guy_id):
    try:
        guy = Guy.objects.get(pk=guy_id)
    except Guy.DoesNotExist:
        raise Http404
    lu = { 'guy': guy }
    return render(request, 'guy/detail.html', lu)
