from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, redirect, render, get_object_or_404


from goods.utils import q_search
from .models import Products, Comment
from .forms import CommentForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

def catalog(request, category_id=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_id == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__id=category_id))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "category_id": category_id
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)

    context = {"product": product}

    return render(request, "goods/product.html", context)


@login_required(login_url="login")
def save_comment(request, product_id):
    product = Products.objects.get(id=product_id)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product =product
        comment.author = request.user
        comment.save()
        messages.success(request, "Комментарии успешно добавлено !")
        return redirect('goods/catalog.html', product_id=product_id)

