from django.db import models
from django.contrib.auth.models import User
from position.models import Position
from guy_proj.settings import TURN_INCR, MOVE_INCR

class Guy(models.Model):
    name = models.CharField(blank=False,
                            null=False,
                            max_length=20)
    owner = models.ForeignKey(User,
                              blank=True,
                              null=True)
    position = models.OneToOneField(Position,
                                    blank=True,
                                    null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.name, self.position)

    @classmethod
    def create(cls, name, x=0, y=0, dir=0, owner=None):
        p = Position(x=x, y=y, dir=dir)
        p.save()
        guy = cls(name=name, position=p, owner=owner)
        return guy

    def save(self, *args, **kwargs):
        """
        If not set, start Guy at 0,0 facing North
        """
        if not self.position:
            p = Position(x=0, y=0, dir=0)
            p.save()
            self.position = p
        super(Guy, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        If guy has a position associated, delete it
        """
        if self.position:
            p = self.position
            p.delete()
        super(Guy, self).delete(*args, **kwargs)

    def turn(self, lor='r'):
        """
        Reorient Guy using numbered cardinal directions
        """
        try:
            i = TURN_INCR[lor]
        except KeyError:
            raise

        self.position.dir = (self.position.dir + i) % 4
        self.position.save()
        return self.position.get_dir_display()

    def move(self, fob='f'):
        """
        Move Guy one space using 1 as forward and -1 as backward
        """
        try:
            i = MOVE_INCR[fob]
        except KeyError:
            raise

        if self.position.dir % 2 == 0:
            if self.position.dir < 2:
                self.position.y += i
            else:
                self.position.y -= i
        else:
            if self.position.dir < 2:
                self.position.x += i
            else:
                self.position.x -= i
        self.position.save()
        return self.position
