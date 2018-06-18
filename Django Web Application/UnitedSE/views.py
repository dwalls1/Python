from django.shortcuts import render
from .models import FacebookModel
from .models import Students
from .models import StudentsForm

#imports for methods dw
from .models import Filmstar
from .models import FilmstarForm
#end of imports for methods dw

#imports submit methods dw
from .models import Cost
from .models import CostForm
#end of submit imports for methods dw
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    
    fb = FacebookModel()
    
    context = {
               'page': {'title': 'United Social Engine', 
                        'content': 'doing something',
                        'comments': fb.retrievePosts(),
                        },
               }
    return render(request,'UnitedSE/index.html',context)

def retrivePosts(request, myword ):
    fb = FacebookModel()
    
    mycomments = fb.retrievePosts(myword)
    
    context = {
               'page': {'title': 'United Social Engine', 
                        'content': 'doing something',
                        'comments': mycomments ,
                        },
               }
    return render(request,'UnitedSE/index.html',context)

# start of name view dw
def students(request):
    
    myform = StudentsForm()
    
    context = {
               'page': {'title': 'this is a students page', 
                        'content': 'doing something ',
                        'myforms' : myform,
                        },
               }
    return render(request, 'UnitedSE/index.html',  context)
# end of name view dw

# start of filmstar view dw
def filmstar(request):
    
    newform = FilmstarForm()
    
    context = {
               'page': {'title': 'Actors Rating Page', 
                        'content': 'Film ',
                        'newforms' : newform,
                        },
               }
    return render(request, 'UnitedSE/index.html',  context)
# end of filmstar view dw


# start of submit view dw
def costView(request):
    if request.method == 'POST':
        
        form = CostForm(request.POST)
        
        if form.is_valid():
            date = request.POST.get('date', '')
            cost = request.POST.get('cost', '')
            cost_obj = Cost(date = date, cost = cost)
            cost_obj.save()
            
            allcost = Cost.objects.all()
            
           
            
            return render(request, 'UnitedSE/cost.html', {
                   'form': form,
                   'allcost': allcost, 
                   })
        else:
             #return HttpResponseRedirect(reverse('cost'))
             return render(request, 'UnitedSE/cost.html', {
                   'form': form,
                   'error': 'Invalid form, please correct', 
                   })
    else:
        form = CostForm()
            
        return render(request, 'UnitedSE/cost.html', {
                   'form': form,
                   })
            
 
# end of submit view dw
