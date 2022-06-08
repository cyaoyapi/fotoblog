"""
Module to define views for app 'blog'.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    """View to show home page."""
    return render(request, 'blog/home.html', context={})
