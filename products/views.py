from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView

from blog.models import BannerModel
from products.models import ProductModel, CategoryModel, BrandModel


class HomeListView(ListView):
    template_name = 'index.html'
    queryset = ProductModel.objects.order_by('-pk')[:3]
    context_object_name = 'products'

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')[:3]
        context['banner'] = BannerModel.objects.last()
        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ShopListView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        qs = ProductModel.objects.select_related('category', 'brand').prefetch_related('colors', 'sizes').order_by('-pk')

        q = self.request.GET.get('q', '').strip()
        category_id = self.request.GET.get('category', '').strip()
        brand_id = self.request.GET.get('brand', '').strip()
        sort = self.request.GET.get('sort', '').strip()

        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(short_description__icontains=q) |
                Q(long_description__icontains=q) |
                Q(category__name__icontains=q) |
                Q(brand__name__icontains=q)
            )

        if category_id.isdigit():
            qs = qs.filter(category_id=int(category_id))

        if brand_id.isdigit():
            qs = qs.filter(brand_id=int(brand_id))

        if sort == 'a_to_z':
            qs = qs.order_by('name')
        elif sort == 'z_to_a':
            qs = qs.order_by('-name')
        elif sort == 'price_asc':
            qs = qs.order_by('price')
        elif sort == 'price_desc':
            qs = qs.order_by('-price')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('name')
        context['brands'] = BrandModel.objects.order_by('name')
        context['current_q'] = self.request.GET.get('q', '')
        context['current_category'] = self.request.GET.get('category', '')
        context['current_brand'] = self.request.GET.get('brand', '')
        context['current_sort'] = self.request.GET.get('sort', '')

        # Sahifalashda boshqa GET parametrlarni saqlab qolish uchun
        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_string'] = query_params.urlencode()
        return context


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
    return render(request, 'wishlist.html', {'products': products})


@login_required
def wishlist_delete(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user

    if user in product.wishlist.all():
        product.wishlist.remove(user)

    return redirect(request.GET.get('next', '/'))


@login_required
def cart_create(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user

    if user in product.cart.all():
        product.cart.remove(user)
    else:
        product.cart.add(user)

    return redirect(request.GET.get('next', '/'))


@login_required
def cart_list(request):
    products = request.user.cart.order_by('-pk')
    return render(request, 'cart.html', {'products': products})


@login_required
def cart_delete(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    product.cart.remove(request.user)
    return redirect(request.GET.get('next', '/'))