from django.shortcuts import render
from django.http import HttpResponse
from .models import Testdata
# Create your views here.

def search(request):
    param={}
    if request.method=='POST':
        query= request.POST.get('task')
        product= Testdata.objects.values('doi','id','incitations','year')
        param=querymatch(query,product)
        query=None
    return render(request,'index.html',{'helloworld': param})

def basic(request):
    return render(request,'basic.html')
def querymatch(query,product):
    x={}
    for item in product:
        if query == item['doi']:
            x['id']=(item['id'])
            y=item['incitations'].split('-')[0]
            x['incitation_count']=int(y)
            x['year']=int(item['year'])
            break
    return x
