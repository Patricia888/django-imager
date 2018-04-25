from django.shortcuts import render


def home_view(request):
    """Routes user back to the generic home page."""
    return render(request, 'generic/home.html')
