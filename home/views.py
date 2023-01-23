from django.shortcuts import render
from home.models import Home


def home(request):
    banner_image = request.FILES.get('banner')
    ext = str(banner_image).split(".")[-1]
    image_name = f'new_name.{ext}'
    home = Home.objects.create(title='test', banner=banner_image)
    home.banner = banner_image
    home.banner.name = image_name
    home.save()
    return render(request, 'home.html')
