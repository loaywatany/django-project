from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
   # return HttpResponse("<h1>Hello World</h1>") #string of html code
    return render(request, "home.html", {})


def contact_view(request, *arg, **kwargs):
    return render(request, "contact.html", {}) #string html code


def about_view(request, *arg, **kwargs):
    my_context = {
        "title" : "abc this is about us",
        "this_is_true": True,
        "my_number" : 123,
        "my_list" : [123, 4242, 123123],
        "my_html": "<h1>Hello world</h1>"
    }

    return render(request, "about.html", my_context) #string html code
