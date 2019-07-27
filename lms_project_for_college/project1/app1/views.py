from django.shortcuts import render
#from .models import Students
# from .forms import StudentFrom
# Create your views here.


# from django.shortcuts import render, redirect
def home(request):
    return render(request,'app1/home.html')

def e_lib(request):
    return render(request,'app1/e_lib.html')


def login(request):
    return render(request,'app1/login.html')

def about(request):
    return render(request,'app1/about.html')

# def studentLogin(request):
#     if request.method=='POST':
#         username=request.POST['First_Name']
#         password=request.POST['']
#
# #         =request.POST['']
# #         Date_of_birth =request.POST['Date_of_Birth']
# #
# #
# # =request.POST['']
# # =request.POST['']
# # =request.POST['']
# # =request.POST['']
# # =request.POST['']
# # =request.POST['']
# #
#
#     return render(request,'studentLogin.html')
#
#
#
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})



# def student_login(request):
#      return render(request,'student_login.html')
#     if request.session.get('mycustomer',None)
#         return redirect('dashboard')
#     if request.method=='POST':
#         email=request.POST['email']
#         password=request.POST['password']
#
#
#         user_auth=Customer.objects.filter(email=email,password=password)
#         if user_auth.exits():
#             request.session['']=email
#             return redirect('dashboard')
#         else:
#             message.warning(request,'your Email id or password nor correct')
#
# def student_logout(request):
#     logout(request)
#     return redirect



# def students_list(request):
#     students=Students.objects.all()
#     context={
#         'students':students,
#     }
#     return render(request,'student/index.html',context)

# def students_add(request):
#     form = StudentFrom(request.POST or None)
#     if form.is_valid():
#         form.save()
#         print("form submited")
#     context = {
#         'form': form,
#     }
#     return render(request,'student/new_students.html',context)

#
# def home(request):
#     return render(request,'home.html')