from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Nbook
from .forms import NbookForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def note_list(request):
    notes = Nbook.objects.filter(user=request.user)
    return render(request, 'Notes/note_list.html', {'notes': notes})

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

    return render(request, 'Notes/create_note.html', {'form': form})





@login_required
def note_detail(request, pk):
    note = get_object_or_404(Nbook, pk=pk, user=request.user)
    return render(request, 'Notes/note_detail.html', {'note': note})




@login_required
def note_edit(request, pk):
    note = get_object_or_404(Nbook, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NbookForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('Notes/note_detail', pk=note.pk)
    else:
        form = NbookForm(instance=note)
    return render(request, 'Notes/note_edit.html', {'form': form, 'note': note})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Nbook, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'Notes/note_delete.html', {'note': note})
