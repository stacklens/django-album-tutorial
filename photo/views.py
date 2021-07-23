from django.http import HttpResponse

def home(request):
    title = '<h1>Hello World</h1>'
    return HttpResponse(title)