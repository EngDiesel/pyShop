from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import category

# Create your views here.
def home(request):
    categories = category.objects.all()
    context = {'categories': categories}
    template = 'home.html'

    return render(request, template, context)


def about(request):
    categories = category.objects.all()
    context = {'categories': categories}    
    template = 'about.html'

    return render(request, template, context)


@login_required
def user_profile(request):
    categories = category.objects.all()
    context = {'categories': categories}
    user = request.user
    context = {'user': user}
    template = 'profile.html'

    return render(request, template, context)
