from django.shortcuts import render

# Create your views here.
def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/product_page.html', {'products': products})