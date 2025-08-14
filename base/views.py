from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm, UserUpdateForm

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()  # Use email instead of username
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)  # Use email to fetch the user
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, 'base/login_register.html', {'page': page})

        user = authenticate(request, email=email, password=password)  # Authenticate using email

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password is incorrect')

    return render(request, 'base/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()  # Use email instead of username
            user.save()
            login(request, user)
            return redirect('home')           
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = get_object_or_404(Room, id=pk)  
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)

def userProfile(request, pk):
    user = get_object_or_404(User, id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        
        if topic_name:
            topic, created = Topic.objects.get_or_create(name=topic_name)
        else:
            messages.error(request, "Topic name is required")
            return redirect('create-room')

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )

        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = get_object_or_404(Room, id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        messages.error(request, "You are not allowed to update this room!")
        return redirect('home')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        messages.success(request, "Room updated successfully!")
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = get_object_or_404(Room, id=pk)

    if request.user != room.host:
        messages.error(request, "You are not allowed to delete this room!")
        return redirect('home')

    if request.method == 'POST':
        room.delete()
        messages.success(request, "Room deleted successfully!")
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = get_object_or_404(Message, id=pk)

    if request.user != message.user:
        messages.error(request, "You are not allowed to delete this message!")
        return redirect('home')

    if request.method == 'POST':
        message.delete()
        messages.success(request, "Message deleted successfully!")
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': message})

@login_required(login_url='login')
def updateUser(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=request.user.pk)
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'base/update_user.html', {'form': form})

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)  # Fetch topics based on search query
    context = {'topics': topics}  # Pass topics to the template
    return render(request, 'base/topics.html', context)

def activityPage(request):
    room_messages = Message.objects.all()
    context = {'room_messages': room_messages}
    return render(request, 'base/activity.html', context)