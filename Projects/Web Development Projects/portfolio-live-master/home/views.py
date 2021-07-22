from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Contact

# Create your views here.


# def home(request):
#     context = {'name': 'Saurav', 'course': 'Django'}
#     return render(request, 'home.html', context)


# def about(request):
#     return render(request, 'about.html')


# def projects(request):
#     return render(request, 'projects.html')


def main(request):
    if request.method == "POST":
        # print("This is Post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()

    return render(request, 'main.html')


# def contact(request):
#     if request.method == "POST":
#         # print("This is Post")
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         desc = request.POST['desc']

#         ins = Contact(name=name, email=email, phone=phone, desc=desc)
#         ins.save()
#         print("The data has been saved to DB")

#     return render(request, 'contact.html')
