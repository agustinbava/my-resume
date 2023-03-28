from django.db import models
from django.utils.timezone import now

class About(models.Model):
    header = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    title_description = models.TextField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False, default='')
    phone = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    degree = models.CharField(max_length=50, default='')
    birthday = models.DateField(default=now)
    text_description = models.TextField(max_length=25000, default='')
    
    def __str__(self, *args, **kwargs):
        return f"{self.id}, {self.title}"
    
    def __unicode__(self, *args, **kwargs):
        return f"{self.id}, {self.title}"
    
    
class Contact(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=500, blank=True, null=False)
    message = models.TextField(max_length=15000, blank=False, null=False)
    
    def __str__(self):
        return self.email + ' ' + self.subject
    

class Resume(models.Model):
    title_description = models.TextField(null=False, blank=False)
    summary = models.TextField(max_length=25000, default='')
    city = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    degree = models.CharField(max_length=50, default='')
    birthday = models.DateField(default=now)
    text_description = models.TextField(max_length=25000, default='')
    
    def __str__(self, *args, **kwargs):
        return f"{self.id}, {self.title}"
    
    def __unicode__(self, *args, **kwargs):
        return f"{self.id}, {self.title}"
    

class Skills(models.Model):
    title_description = models.TextField(blank=False)
    skills = models.JSONField(null=True, blank=True)
    
    def __str__(self, *args, **kwargs):
        return f"{self.id}, {self.title}"
    
    def __unicode__(self, *args, **kwargs):
        return f"{self.id}, {self.title}"
    
