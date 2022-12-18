from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app1.html')
def page11(request):
    return render(request,'page1.html')
def page22(request):
    return render(request,'page2.html')
def page33(request):
    return render(request,'page3.html')
def page44(request):
    return render(request,'page4.html')
def page55(request):
    return render(request,'page5.html')

