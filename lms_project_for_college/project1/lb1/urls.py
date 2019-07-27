from django.urls import path
from . import views
urlpatterns = [
        # path('login/',views.login,name="login"),
    path('addbook/', views.CreateBookView.as_view(), name="addbook"),
    path('books/',views.BookListView.as_view() ,name="book_list"),
    path('',views.home1,name="home1"),
    path('total_books/', views.total_books, name='total_books'),

    path('showbook/',views.showbook,name="showbook"),
    path('showstudent/',views.showstudent,name="showstudent"),
    path('addstudent/', views.CreateStudentView.as_view(), name="addstudent"),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view()),
    path('delete/', views.BookListViewDelete.as_view(), name='delete'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('delete_students/', views.StudentListViewDelete.as_view(), name='delete_student'),
    path('delete_students/<int:pk>/', views.StudentDetailViewDelete.as_view())




]
