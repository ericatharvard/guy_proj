from django.db import models

class Position(models.Model):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    ORIENTATIONS = (
        (NORTH, 'North'),
        (EAST, 'East'),
        (SOUTH, 'South'),
        (WEST, 'West'),
        )

    x = models.IntegerField(blank=False,
                            null=False,
                            default=0)
    y = models.IntegerField(blank=False,
                            null=False,
                            default=0)
    dir = models.PositiveIntegerField(blank=False,
                                      choices=ORIENTATIONS,
                                      default=NORTH)

    def __str__(self):
        return "X: %d, Y: %d, DIR: %s" % (self.x, self.y, self.get_dir_display())

    def get_dir_name(self):
        return self.get_dir_display()

    def get_dir_letter(self):
        return self.get_dir_display()[0].lower()
