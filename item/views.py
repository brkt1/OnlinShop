from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import  login_required

from item.models import Item
from .form import EditItem, newItem

# Create your views here.
@login_required
def new(request):
    if request.method == 'POST':
        form = newItem(request.POST , request.FILES)
        if form.is_valid():
           item = form.save(commit=False)
           item.created_by  = request.user
           item.save()
           return redirect('item:detail', pk= item.id)
    else:
        form = newItem()
    return render(request, 'new.html', {'form': form})

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = EditItem(request.POST , request.FILES , instance=item)
        form.save()
        return redirect('item:detail', pk= item.id)
    else:
        form = EditItem(instance=item)
    return render(request, 'new.html', {'form': form})