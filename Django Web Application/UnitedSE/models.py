from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

import urllib.request as rq

import json 

# Create your models here.
class FacebookModel(models.Model):
    pass

    def retrievePosts(self, myword=None):
        urlfirst = 'https://graph.facebook.com/'
        urllast = '/posts/?key=value&access_token=619502538260226|11f24929e4385b59a36f02ab0f35500e'
        
        realurl = urlfirst + myword + urllast 
        
        request = rq.Request(realurl)
        
        response = rq.urlopen(request)
        str = response.read()
        jsn = json.loads(str)
        return jsn['data']
    
# start form model f

class Students(models.Model):
    sname = models.CharField(max_length=100)
    smark = models.IntegerField()

    def myMethod(self):
        pass

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        #fields = ['sname', 'smark']
        fields = '__all__'
    
# end form model f  

# start filmstar form model dw

class Filmstar(models.Model):
    actor = models.CharField(max_length=100)
    rating = models.IntegerField()

    def myMethod(self):
        pass

class FilmstarForm(ModelForm):
    class Meta:
        model = Filmstar
        #fields = ['sname', 'smark']
        fields = '__all__'
    
# end form model dw  

# start submit form model dw

class Cost(models.Model):
    cost = models.FloatField()
    date = models.DateField()
    
    def myMethod(self):
        pass
    
class CostForm(ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'
       

    
# end submit form model dw  
