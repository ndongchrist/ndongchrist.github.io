from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    #Home
    home = models.Home.objects.latest('updated')

    #About
    about = models.About.objects.latest('updated')
    profiles = models.Profile.objects.filter(about = about)

    #Skills
    categories = models.Category.objects.all()

    #Portfolio
    portfolios = models.Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }

    return render(request, 'index.html', context)

def download_file(request):
    # Replace 'path/to/your/file.txt' with the actual path to your file
    file_path = "static/assets/MyResume.pdf"
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="MyResume.pdf"'
        return response
