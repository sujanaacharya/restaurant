from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def home(request):
    return HttpResponse("welcome to myrestaurant")
def aboutus(request):
    return HttpResponse(" <b>food sansar</b>")    
def coursedetail(request,courseid):
    return HttpResponse(courseid)
def learning(request):
    data={
        'title':'homy page',
        'sub':'science',
        'grade':'d',
        'clist':['php','java','py'],
        'sdet':[
            {'name':'ram','phone':123},
            {'name':'shyam','phone':567},
            {'name':'shym','phone':5678},
            {'name':'shya','phone':5679}

        ],
        'cclist':[0,1,2,3,4,5]
    }
    return render(request,'learn.html',data)





