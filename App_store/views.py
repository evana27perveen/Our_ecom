
from django.shortcuts import render, HttpResponseRedirect, reverse

from App_login.models import CustomUser
from App_order.models import CartModel
from .models import ProductModel, SubCategoryModel
from .forms import SubCategoryForm, ProductForm


# Create your views here.
def home(request):
    cart = CartModel.objects.filter(customer=request.user).count()
    products = ProductModel.objects.all()


    content = {
        'cart': cart,
        'products': products
    }
    return render(request, 'App_store/home.html', context=content)


def store(request):
    products = ProductModel.objects.filter(status=True)
    sub_categories = SubCategoryModel.objects.filter(status=True)

    content = {
        'products': products,
        'sub_categories': sub_categories,
    }
    return render(request, 'App_store/store.html', context=content)


def add_to_cart(request):
    pk = request.POST.get('pk')
    quantity = request.POST.get('quantity')
    size = request.POST.get('size')
    color = request.POST.get('color')
    product = ProductModel.objects.get(id=pk)
    try:
        cart = CartModel.objects.get(customer=request.user, order=product, status=False, size=size, color=color)
        cart.quantity += quantity
        cart.save()
    except:
        cart = CartModel(customer=request.user, order=product, quantity=quantity, size=size, color=color, status=False)
        cart.save()
    return HttpResponseRedirect(reverse('App_store:home'))


def cart_sys(request):
    cart = CartModel.objects.filter(customer=request.user)

    content = {
        'cart': cart,
    }
    return render(request, 'App_store/cart.html', context=content)
