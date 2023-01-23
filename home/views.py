from django.shortcuts import render
from home.models import Home


def home(request):
    if request.method == 'POST':
        banner_image = request.FILES.get('banner')
        title = request.POST.get('title')
        ext = str(banner_image).split(".")[-1]
        image_name = f'new_name.{ext}'
        home = Home.objects.create(title=title)
        home.banner = banner_image
        home.banner.name = image_name
        home.save()
    samples = Home.objects.all()
    return render(request, 'home.html', {'samples':samples})
