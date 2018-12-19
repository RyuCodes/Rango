from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Category, Page

# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    #most viewed pages
    most_viewed = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = most_viewed

    # .url can be added to model even if not explicitly defined in model (like pk?)
    for category in category_list:
        category.url = category.name.replace(' ', '_')

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html')

def category(request, category_name_url):
    # replace underscores with spaces. Assumes url uses underscores
    category_name = category_name_url.replace("_"," ")
    context_dict = {'category_name': category_name}

    # May want to use get_object_or_404, but don't want page to throw exception

    try:
        category = Category.objects.get(name=category_name)

        # Find all associated pages
        pages = Page.objects.filter(category=category)

        # Add category and pages to context_dict pass to urls.py and templates
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        #Don't do anything
        pass

    # can pass through anything back tot he templates in a dict format
    return render(request, 'rango/category.html', context_dict)
