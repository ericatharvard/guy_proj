from django.db import models
from django.contrib.auth.models import User
from guy.models import Guy

class Command(models.Model):
    STAY = 's'
    FORWARD = 'f'
    BACK = 'b'
    LEFT = 'l'
    RIGHT = 'r'
    COMMANDS = (
        (STAY, "Stay"),
        (FORWARD, "Go Forward"),
        (BACK, "Back Up"),
        (LEFT, "Turn Left"),
        (RIGHT, "Turn Right"),
        )

    action = models.CharField(max_length=1,
                            choices=COMMANDS,
                            default=STAY)
    guy = models.ForeignKey(Guy, null=True)
    issued_by = models.ForeignKey(User, null=True)
    time_issued = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_issued']

    def __str__(self):
        return "%s, %s" % (self.action, self.guy)
