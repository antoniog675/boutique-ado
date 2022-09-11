from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """A view to return the bag page"""
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a specified quantity of products into the bag"""
