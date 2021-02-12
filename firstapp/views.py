from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Hello</h1>')

# def user_page(request, user_name):
#     return HttpResponse(f'<h1>{user_name}\'s page ')

# def number_page(request, user_name, number):
#     user_name = user_name.upper()
#     return HttpResponse(f'<h1>{user_name}\'s page number = {number}</h1>')

#ここからteplateの操作の記述
def index(request):
    val = 'Good bye'
    return render(request, 'firstapp/index.html', context={'value': val})  #これによりtemplatesのindex.htmlが呼ばれる、contextを指定することでhtmlファイルでその値を使うことができる

def home(request):
    my_name = 'Taro Yamada'
    favorite_fruits = ['Apple', 'Grape', 'Lemon']
    my_info = {
        'name': 'Taro',
        'age': 18
    }
    return render(request, 'home.html', context={
        'my_name': my_name,
        'favorite_fruits': favorite_fruits,
        'my_info':my_info
    })