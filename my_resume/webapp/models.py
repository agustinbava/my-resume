from django.db import models

class About(models.Model):
    header = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    title_description = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    
    def __str__(self, *args, **kwargs):
        return f"{self.id}, {self.title}"
    
    def __unicode__(self, *args, **kwargs):
        return f"{self.id}, {self.title}"