from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from.models import *
from django.views.generic import CreateView, DetailView, ListView, DeleteView
# Create your views here.
from django.urls import reverse_lazy


def home1(request):
    return render(request,'lb1/home.html')

# def addbook(request):
#     # addbook = lb1.addbook.objects.all()
#     return render(request,'lb1/addbook.html')

class CreateBookView(CreateView):
	fields = ['name', 'author_name', 'publication']
	model = Book
	template_name = 'lb1/create_book.html'



def showbook(request):
    showbooks = Addbook.objects.all()
    return render(request,'lb1/showbook.html',{'showbooks':showbooks})

def showstudent(request):
    showstudents = Addstudent.objects.all()
    return render(request,'lb1/showstudents.html',{'showstudents':showstudents})


class CreateStudentView(CreateView):
	fields = [

		'name',
		'book',
		'semester',
		'student_id',
		'father_name',
		'mobile_no',
		'aadhar',
		'address',
		'Pin_code',
	]
	model = Student
	template_name = 'lb1/create_student.html'
# def addstudent(request):
    # return render(request,'lb1/addstudent.html')

# def book_details(request):
#     return render(request,'lb1/book_details.html')
class BookListView(ListView):
	model = Book
	template_name = 'lb1/book_list.html'
	context_object_name = 'booklist'

class BookDetailView(DetailView):
	model = Book
	template_name = 'lb1/book_details.html'
	context_object_name = 'book_details'


def total_books(request):
	books = Book.objects.all()
	count = len(books)
	data = {'books': books, 'count': count}
	return render(request, 'lb1/total_books.html', context=data)


class BookDeleteView(DeleteView):
	model = Book
	template_name = 'lb1/book_delete.html'
	success_url = reverse_lazy('home1')

class BookListViewDelete(ListView):
	model = Book
	template_name = 'lb1/delete.html'
	context_object_name = 'booklist'

class StudentListView(ListView):
	model = Student
	template_name = 'lb1/student_list.html'
	context_object_name = 'student_list'

class StudentDetailView(DetailView):
	model =Student
	template_name = 'lb1/student_detail.html'
	context_object_name = 'student_detail'

class StudentListViewDelete(ListView):
	model = Student
	template_name = 'lb1/student_delete_list.html'
	context_object_name = 'student_list'

class StudentDetailViewDelete(DeleteView):
	model =Student
	template_name = 'lb1/student_delete.html'
	success_url = reverse_lazy('home1')


