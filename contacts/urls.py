from django.urls import path

from contacts.views import ContactCreateView

app_name = 'contacts'

urlpatterns = [
    path('', ContactCreateView.as_view, name='contact'),
]