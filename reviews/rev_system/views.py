from django.shortcuts import render
from django.shortcuts import redirect
from rev_system.models import Product, Review



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def add_review(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        author = request.POST['author']
        text = request.POST['text']
        rating = request.POST['rating']
        review = Review(product=product, author=author, text=text, rating=rating)
        review.save()
        return redirect('product_detail',id=product_id)
    
def index(request):
    return render(request, 'index.html')

