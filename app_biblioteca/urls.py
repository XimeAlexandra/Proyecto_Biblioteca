from app_biblioteca import views
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import dashboard


urlpatterns = [
    path(r'', views.main, name='main'), # lendings
    path(r'lendings_book/<int:bookid>/',views.lendings_book,name='lendings_book'), # préstamos desde libro
    path(r'lendings_reader/<int:readerid>/',views.lendings_reader,name='lendings_reader'), # préstamos desde lector
    path('delete_lending/', views.delete_lending, name='delete_lending'),

    path('login/', views.login, name='login'),
    path('registro/', views.registro_usuario, name='registro'),
    path('valida_user/', views.valida_user, name='valida_user'),

    path('books/', views.books_view, name='books'),
    path('delete_book/', views.delete_book, name='delete_book'),

    path('readers/', views.readers_view, name='readers'),
    path('delete_reader/', views.delete_reader, name='delete_reader'),

    path('editorials/', views.editorials_view, name='editorials'),
    path(r'books_editorial/<int:editorialid>/',views.books_editorial,name='books_editorial'), # libros desde editorial
    path('delete_editorial/', views.delete_editorial, name='delete_editorial'),

    path('genres/', views.genres_view, name='genres'),
    path(r'books_genre/<int:genreid>/',views.books_genre,name='books_genre'), # libros desde género
    path('delete_genre/', views.delete_genre, name='delete_genre'),

    path('languages/', views.languages_view, name='languages'),
    path(r'books_language/<int:languageid>/',views.books_language,name='books_language'), # libros desde idiomas
    path('delete_language/', views.delete_language, name='delete_language'),

    # crear y editar libros, lectores y préstamos
    path('createBook/', views.createBook, name = 'create_book'),
    path('editBook/<int:id>', views.editBook, name = 'edit_book'),

    path('createReader/', views.createReader, name = 'create_reader'),
    path('editReader/<int:id>', views.editReader, name = 'edit_reader'),

    path('createLending/', views.createLending, name = 'create_lending'),
    path('editLending/<int:id>', views.editLending, name = 'edit_lending'),

    path('createLanguage/', views.createLanguage, name='create_language'),
    path('editLanguage/<int:id>', views.editLanguage, name = 'edit_language'),

    path('createEditorial/', views.createEditorial, name='create_editorial'),
    path('editEditorial/<int:id>', views.editEditorial, name = 'edit_editorial'),

    path('createGenre/', views.createGenre, name='create_genre'),
    path('editGenre/<int:id>', views.editGenre, name = 'edit_genre'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('dashboard/', dashboard, name='dashboard'),
]