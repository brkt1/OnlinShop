from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from chat.models import Chat, Message
from .forms import SignUpForm
from item.models import Category , Item


# Create your views here.

def  index(request):
    product = Item.objects.filter(is_sold =False)
    categories = Category.objects.all()
    query =  request.GET.get('query','')
    categoryButton = request.GET.get('category','')
    if categoryButton:
        product = product.filter(category_id=categoryButton)
    elif query:
        q_name = Q(name__icontains=query)
        q_description = Q(description__icontains=query)
        product = product.filter(q_name | q_description)
    return render(request, 'index.html', {'products' : product , 'categories':categories ,'category_id':categoryButton})

def detail(request, pk):
    product = get_object_or_404(Item, pk=pk)  
    related_items = Item.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)
    return render(request, 'detail.html', {"product": product, "related": related_items})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('item:index')  # Redirect to your home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view (request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user  = form.save()
            login(request, user)
            return redirect('item:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form })

@login_required
def delet_item(request , pk):
    item = get_object_or_404(Item, pk=pk,  created_by=request.user)
    item.delete()
    return  redirect('dashbordapp:dashboard')

@login_required
def seller_chats(request):
    # Fetch all chats where the current logged-in user is the seller
    chats = Chat.objects.filter(seller=request.user)
    
    return render(request, 'seller_chats.html', {'chats': chats})

@login_required
def chat_detail(request, chat_id):
    # Get the chat object
    chat = get_object_or_404(Chat, id=chat_id)
    
    # Ensure that the logged-in user is either the buyer or the seller in this chat
    if request.user != chat.buyer and request.user != chat.seller:
        return HttpResponseForbidden("You are not authorized to view this chat.")
    
    # If the user submits a message (POST request)
    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            # Create a new message in the chat
            Message.objects.create(
                chat=chat,
                sender=request.user,
                content=message_content
            )

    # Fetch all messages for the chat
    messages = chat.messages.all().order_by('timestamp')
    
    return render(request, 'chat/chat_detail.html', {
        'chat': chat,
        'messages': messages,
    })
