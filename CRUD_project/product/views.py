from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse

def products(request):
    if request.method == 'POST':
        data = request.POST

        product_image = request.FILES.get('product_image')
        product_name = data.get('product_name')
        product_description = data.get('product_description')

        Product.objects.create(
            product_image=product_image,
            product_name=product_name,
            product_description=product_description,
        )
        return redirect('add')
    
    queryset = Product.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            product_name__icontains=request.GET.get('search'))

    context = {'products': queryset}

    return render(request, 'products.html', context)

def delete_product(request, id):
    queryset = Product.objects.get(id=id)
    queryset.delete()
    return redirect('add')

def update_product(request, id):
    queryset = Product.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        product_image = request.FILES.get('product_image')
        product_name = data.get('product_name')
        product_description = data.get('product_description')

        queryset.product_name = product_name
        queryset.product_description = product_description

        if product_image:
            queryset.product_image = product_image

        queryset.save()
        return redirect('add')

    context = {'product': queryset}
    return render(request, 'update_product.html', context)
