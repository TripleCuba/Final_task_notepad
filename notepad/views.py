from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Note, Category
from .forms import AddNoteForm, AddCategoryForm, CreateUserForm, UpdateCategoryForm, UpdateNoteForm
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse('home'))
    return render(request, 'registration/sign_up.html', context={'form': form})


# validated
@login_required(login_url='/registration/login')
def notes(request):
    data = Note.objects.filter(category__user=request.user.id).all()
    categories = Category.objects.filter(user=request.user.id).all()
    form = AddNoteForm()
    if request.method == 'POST':
        note = AddNoteForm(request.POST, request.FILES)
        note.save()
        return redirect(reverse('notes'))

    context = {
        'data': data,
        'form': form,
        'categories': categories,
    }
    return render(request, 'notes.html', context=context)


# validated
@login_required(login_url='/registration/login')
def note(request, note_id):
    data = Note.objects.filter(id=note_id).first()
    if data and data.category.user.id == request.user.id:

        context = {
            'data': data
        }
        return render(request, 'note.html', context=context)
    else:
        return redirect(reverse('notes'))


# validated
@login_required(login_url='/registration/login')
def update_note(request, note_id):
    note = Note.objects.filter(id=note_id).first()
    if note and note.category.user.id == request.user.id:
        if request.method == 'POST':
            form = UpdateNoteForm(request.POST, request.FILES, instance=note)
            form.save()
            return redirect('note', note_id=note_id)
        else:
            form = UpdateNoteForm(initial={
                'title': note.title,
                'note_text': note.note_text,
                'note_image': note.note_image,
                'category': note.category
            })
        context = {
            'form': form
        }
        return render(request, 'update_note.html', context=context)
    else:
        return redirect(reverse('notes'))


# validated
@login_required(login_url='/registration/login')
def delete_note(request, note_id):
    data = Note.objects.filter(id=note_id).first()
    if data and data.category.user.id == request.user.id:
        data.delete()
        return redirect(reverse('notes'))
    else:
        return redirect(reverse('notes'))


# validated
@login_required(login_url='/registration/login')
def categories(request):
    data = Category.objects.filter(user=request.user.id).all()
    form = AddCategoryForm()
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['user'] = request.user.id

        form = AddCategoryForm(request_data, request.FILES)
        form.save()
        return redirect(categories)
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'categories.html', context=context)


# validated
@login_required(login_url='/registration/login')
def notes_by_category(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    if category and category.user.id == request.user.id:
        form = AddNoteForm()
        if request.method == 'POST':
            request_data = request.POST.copy()
            request_data['category'] = category_id
            note = AddNoteForm(request_data, request.FILES)
            note.save()
            return redirect('notes_by_category', category_id=category_id)
        data = Note.objects.filter(category=category_id).all()
        category = Category.objects.filter(id=category_id).first()
        context = {
            'data': data,
            'form': form,
            'category': category,
        }
        return render(request, 'notes.html', context=context)
    else:
        return redirect(reverse('categories'))


# validated
@login_required(login_url='/registration/login')
def update_category(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    if category and category.user.id == request.user.id:
        if request.method == 'POST':
            form = UpdateCategoryForm(request.POST, request.FILES, instance=category)
            form.save()
            return redirect('notes_by_category', category_id=category_id)
        else:
            form = UpdateCategoryForm(
                initial={
                    'category_title': category.category_title,
                    'description': category.description,
                    'category_image': category.category_image,
                }
            )
        context = {
            'form': form
        }
        return render(request, 'update_category.html', context=context)
    else:
        return redirect(reverse('categories'))


@login_required(login_url='/registration/login')
def delete_category(request, id):
    data = Category.objects.filter(id=id).first()
    if data and data.user.id == request.user.id:
        data.delete()
        return redirect(reverse('categories'))
    else:
        return redirect(reverse('categories'))


@login_required(login_url='/registration/login')
def search(request):
    query = request.GET.get('query')
    results = Note.objects.filter(
        category__user=request.user.id and
        Q(title__icontains=query) |
        Q(note_text__icontains=query) |
        Q(category__category_title__icontains=query) |
        Q(category__description__icontains=query)
    )
    results_length = len(results)
    context = {
        'query': query,
        'results': results,
        'results_length': results_length,
    }
    return render(request, 'search_results.html', context=context)
