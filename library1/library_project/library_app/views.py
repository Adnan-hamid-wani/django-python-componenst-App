from django.shortcuts import render

# Create your views here.
def home(request):
    book1 = {'title': 'Book1', 'author1': 'Author1', 'subject': 'fiction'}
    book2 = {'title': 'Book2', 'author2': 'Author2', 'subject': 'fiction'}

    context = {
        'book1': book1,
        'book2': book2,
    }

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def books(request):
    books = [
    {'title': 'Book1', 'author': 'Author1', 'subject': 'fiction'},
    {'title': 'Book2', 'author': 'Author2', 'subject': 'fiction'},
    {'title': 'Book3', 'author': 'Author3', 'subject': 'fiction'},
    {'title': 'Book4', 'author': 'Author4', 'subject': 'fiction'}
        


    ]

    return render(request, 'books.html', {'books': books})


