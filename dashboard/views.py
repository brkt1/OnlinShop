from django.shortcuts import redirect, render
from item.models import Item
from django.contrib.auth.decorators import  login_required
from django.shortcuts import get_object_or_404
from main.views import index


# Create your views here.

@login_required
 
def dashboard(request):

    items = Item.objects.filter(created_by = request.user)
    return render (request, 'dashboard.html',{'items':items})
    
@login_required
def  edit_item(request , pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.save()


