from django.db import models

class Message(models.Model):
    body = models.TextField(max_length=1024)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.body

    class Meta:
        ordering = ['-posted']
