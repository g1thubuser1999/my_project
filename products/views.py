from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView

from blog.models import BannerModel
from products.models import ProductModel, CategoryModel
from django.utils.translation import gettext_lazy as _


class HomeListView(ListView):
    template_name = 'index.html'
    queryset = ProductModel.objects.order_by('-pk')[:3]
    context_object_name = 'products'

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')[:3]
        context['banner'] = BannerModel.objects.last

        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ShopListView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(Q(title__icontains=q) |
                           Q(description__icontains=q))

        return qs


class ShopTemplateView(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.order_by('-pk')
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'shop-single.html'
    model = ProductModel
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().category.products.order_by('-pk').exclude(
            pk=self.get_object().pk)[:10]

        return context


@login_required
def wishlist_create(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user

    if user in product.wishlist.all():
        product.wishlist.remove(user)
    else:
        product.wishlist.add(user)

    return redirect(request.GET.get('next', '/'))


@login_required
def wishlist_list(request):
    products = request.user.wishlist.order_by('-pk')

    context = {
        'products': products
    }

    return render(request, 'wishlist.html', context)


@login_required
def wishlist_delete(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user

    if user in product.wishlist.all():
        product.wishlist.add(user)
    else:
        product.wishlist.remove(user)

    return redirect(request.GET.get('next', '/'))


@login_required
def cart_create(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user

    if user in product.wishlist.all():
        product.cart.remove(user)
    else:
        product.cart.add(user)

    return redirect(request.GET.get('next', '/'))


@login_required
def cart_list(request):
    products = request.user.cart.order_by('-pk')

    context = {
        'products': products
    }

    return render(request, 'cart.html', context)


@login_required
def cart_delete(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user

    if user in product.cart.all():
        product.cart.add(user)
    else:
        product.cart.remove(user)

    return redirect(request.GET.get('next', '/'))
