from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
@login_required
def index(request):
    journal_types = JournalType.objects.all()
    return render(request, "index.html",{'journal_types':journal_types})
@login_required
def journal_list(request, journal_type_id):
    journal_type = JournalType.objects.get(id = journal_type_id)
    entries = Journal.objects.filter(journal_type = journal_type)
    return render(request, "journal_list.html",{'entries':entries, 'journal_type':journal_type})
@login_required
def journal_detail(request, id):
    journal = get_object_or_404(Journal, id=id)
    return render(request, 'journal/journal_detail.html', {'journal': journal})

@login_required
def new_journal(request, journal_type_id):
    journal_type = JournalType.objects.get(id = journal_type_id)
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal=form.save(commit=False)
            journal.journal_type = journal_type
            journal.save()
            return redirect('journal_list',journal_type_id = journal_type_id)
    else:
        form = JournalForm()
    return render(request,"new_journal.html",{'form':form,'journal_type':journal_type})

@login_required
def edit_journal(request, id):
    journal = get_object_or_404(Journal, id=id)
    if request.method == "POST":
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            form.save()
            return redirect('journal_detail',id=journal.id)
    else:
        form = JournalForm(instance=journal)
    return render(request, 'edit_journal.html', {'form': form})

@login_required
def delete_journal(request, id):
    journal = get_object_or_404(Journal, id=id)
    if request.method == "POST":
        journal.delete()
        return redirect("index")
    return redirect(request,'delete_journal.html',{'journal':journal})
@login_required
def new_journal_type(request):
    if request.method == 'POST':
        form = JournalTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JournalTypeForm()
    return render(request, 'journal/new_journal_type.html', {'form': form})


@login_required
def edit_journal_type(request, id):
    journal_type = get_object_or_404(JournalType, id=id)
    if request.method == "POST":
        form = JournalTypeForm(request.POST,instance=journal_type)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = JournalTypeForm(instance=journal_type)
    return render(request, 'edit_journal_type.html', {'form': form})

@login_required
def delete_journal_type(request, id):
    journal_type = get_object_or_404(JournalType, id=id)
    if request.method == "POST":
        journal_type.delete()
        return redirect("index")
    return redirect(request,'delete_journal_type.html',{'journal_type':journal_type})