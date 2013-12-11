from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from daddy_app.forms import AuthenticateForm, UserCreateForm, NoteForm
from daddy_app.models import Note




def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        note_form = NoteForm()
        user = request.user
        notes_self = Note.objects.filter(user=user.id)
        notes_buddies = Note.objects.filter(user__userprofile__in=user.profile.follows.all)
        notes = notes_self | notes_buddies

        return render(request,
                      'buddies.html',
                      {'note_form': note_form, 'user': user,
                       'notes': notes,
                       'next_url': '/', })
    else:
        # User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()

        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')

 
@login_required
def public(request, note_form=None):
    note_form = note_form or NoteForm()
    notes = Note.objects.reverse()[:10]
    return render(request,
                  'public.html',
                  {'note_form': note_form, 'next_url': '/notes',
                   'notes': notes, 'username': request.user.username})


@login_required
def submit(request):
    if request.method == "POST":
        note_form = NoteForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect(next_url)
        else:
            return public(request, note_form)
    return redirect('/')