from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from .models import Product



# Create your views here.

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        #confirming delete
        obj.delete()
    context = {
        "object": obj
    }
    return render(request, "products/products_delete.html")

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/products_create.html", context)

def dynamic_lookup_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        "object": obj
    }
    return render(request, "products/products_detail.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/products_list.html", context)
