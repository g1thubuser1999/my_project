from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from contacts.forms import ContactModelForm

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactModelForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('contacts:contact')
#
#     else:
#         form = ContactModelForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'contact.html', context)


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("contacts:contact")
