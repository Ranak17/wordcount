from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    
     return render(request,"htmlfile.html")

def count(request):
    data=request.GET["fulltextarea"]
    b=len(data.replace(" ",""))
    c=data.split()
    e={}
    for i in c:
        if i in e:
            e[i]+=1
        else:
            e[i]=1
    return render(request,"count.html",{"key":b,"fulltext":data,"dict":e.items()})
