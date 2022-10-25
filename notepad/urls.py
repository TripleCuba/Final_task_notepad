from django.urls import path
from .views import index, notes, categories, sign_up, note, update_note, delete_note, notes_by_category, \
    delete_category, update_category, search

urlpatterns = [
    path('', index, name='home'),
    path('notes/', notes, name='notes'),
    path('notes/<category_id>', notes_by_category, name='notes_by_category'),
    path('note/<note_id>', note, name='note'),
    path('update_note/<note_id>', update_note, name='update_note'),
    path('delete_note/<note_id>', delete_note, name='delete_note'),
    path('categories', categories, name='categories'),
    path('update_category/<category_id>', update_category, name='update_category'),
    path('delete_category/<id>', delete_category, name='delete_category'),
    path('registration/sign_up/', sign_up, name='sign_up'),
    path('search', search, name='search'),
]
