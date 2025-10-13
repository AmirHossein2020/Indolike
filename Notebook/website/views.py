from django.shortcuts import render, redirect
from .forms import NbookForm
from .models import Nbook
# Create your views here.

def home(request):
    return render(request, 'home.html')

def note_list(request):
    notes = Nbook.objects.filter(user=request.user)
    return render(request, 'note_list.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NbookForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')  
    else:
        form = NbookForm()

    return render(request, 'create_note.html', {'form': form})

