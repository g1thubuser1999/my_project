from django.shortcuts import render
from .models import AboutModel


def about_view(request):
    about = AboutModel.objects.first()

    print("LANGUAGE:", request.LANGUAGE_CODE)
    print("TITLE:", about.title if about else None)
    print("TITLE_UZ:", about.title_uz if about else None)

    context = {
        'about': about,
    }

    return render(request, 'about.html', context)