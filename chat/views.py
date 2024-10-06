from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from item.models import Item 
from .models import Chat , Message


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Item

@login_required
def start_chat(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # Get or create a chat between the buyer (logged-in user) and the seller (item owner)
    chat, created = Chat.objects.get_or_create(
        buyer=request.user,
        seller=item.created_by,
        item=item
    )
    # Redirect to the chat detail page
    return redirect('chat:chat_detail', chat_id=chat.id)


@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)

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
    
    # Render the chat page with the chat and messages
    return render(request, 'chat_detail.html', {
        'chat': chat,
        'messages': messages,
    })
