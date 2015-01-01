from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
    for_you = models.BooleanField(default=True, verbose_name="Is this purchase for you?  If so, check this box.") #This field was added, and migrated with south in Lecture 31
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    
    
    # auto_now_add is for when the timestamp is created
    # auto_now is for when the timestamp is updated/changed
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) # So timestamp will always only give us the date/time of creation
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) # So updated will always only give us the date/time of last edit
    
    
    def __unicode__(self):
        return smart_unicode(self.email)