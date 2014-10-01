from django.http import Http404
from django.shortcuts import render, redirect

from guy.models import Guy
from command.models import Command
from guy_proj.settings import TURN_INCR, MOVE_INCR

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
    return render(request, 'guy/display.html', lu)

def handle_command(request, guy_id, command):
    try:
        guy = Guy.objects.get(pk=guy_id)
    except Guy.DoesNotExist:
        raise Http404

    try:
        c = Command(action=command, 
                    guy=guy,
                    issued_by=request.user)
        c.save()
    except:
        raise
    
    if command in TURN_INCR.keys():
        try:
            guy.turn(command)
        except:
            raise
    
    if command in MOVE_INCR.keys():
        try:
            guy.move(command)
        except:
            raise
    
    """
    c = Command()
    c_opts = [k for k, v in c.COMMANDS]
    if command not in c_opts:
        raise Http404
    """
        
    return redirect('guy:display', guy_id=guy_id)
