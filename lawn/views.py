from django.shortcuts import render

# Create your views here.
def index(request):
    # return render(request, "index.html") your mistake
    return render(request, "lawn/index.html")

# create registration view here
    # return render(request, "lawn/registration.html")
