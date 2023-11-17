from django.shortcuts import render

# Create your views here.




def condition(request):
    d={'a':20, 'b':30,'c':50}
    return render(request,'if.html',d)
