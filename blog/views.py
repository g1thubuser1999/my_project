# from django.views.generic import TemplateView, ListView
#
# from products.models import CategoryModel, ProductModel
#
#
#
# class HomeListView(ListView):
#     template_name = 'index.html'
#     queryset = ProductModel.objects.order_by('-pk')[:3]
#     context_object_name = 'products'
#
#     def get_context_data(self, *, object_list=..., **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = CategoryModel.objects.order_by('-pk')[:3]
#
#         return context
#
# class AboutView(TemplateView):
#     template_name = 'about.html'
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
#
# class ShopView(TemplateView):
#     template_name = 'shop.html'
#
# class DetailView(TemplateView):
#     template_name = 'shop-single.html'