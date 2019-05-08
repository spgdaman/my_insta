from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Location,Image,User

def main(request):
    return render(request, 'index.html')

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"pics":searched_category})
    else:
        message = "Oops...seems you did not search a correct term"
        return render(request,'search.html',{"message":message})