from django.shortcuts import render

# Create your views here.
def sample(request):
    #creating dictionary to store some valuse and display by html
    return render(request, 'emallapp/index.html') 
