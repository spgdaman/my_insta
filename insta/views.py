from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Category,Location,Image

def main(request):
    all_images = Image.objects.all()
    return render(request, 'index.html',{"all_images":all_images})

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"pics":searched_category})
    else:
        message = "Oops...seems you did not search a correct term"
        return render(request,'search.html',{"message":message})

def show_image(request,image_id):
    try:
        image = Image.objects.filter(id=image_id)
    except DoesNotExist:
        raise Http404
    return render(request,'show_image.html', {"images":image})

def show_post_category(request,category_id):
    category = Category.objects.filter(id=category_id)
    posts = Image.objects.filter(image_category=category_id)
    # posts = Image.objects.filter(image_category=category.id)

    return render(request, 'showpostcategory.html', {"posts":posts,"category": category})

def show_locations(request):
    locations = Location.objects.all()

    return render(request,'showlocations.html', {"locations":locations})

def display_location(request,location_id):
    locations = Location.objects.filter(id=location_id)
    posts = Image.objects.filter(image_location=location_id)

    return render(request, 'display_location.html', {"locations":locations,"posts":posts})