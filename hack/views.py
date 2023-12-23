from django.shortcuts import render

#python manage.py tailwind start

# Create your views here.

def home(request):
    context = {}
    return render(request,'hack/home.html',context)

def base(request):
    context = {}
    #return render(request,'hack/base.html',context)
    pass
def about(request):
    context = {}
    return render(request,'hack/about.html',context)

def tools(request):
    context = {}
    return render(request,'hack/tools.html',context)

def specific_tool(request):
    
    pass
