from django.http import HttpResponse


# Function View
def welcome(request):
    name = request.GET['name']
    return HttpResponse(f"<h1 style='color:blue'>{name}, Welcome To Django</h1>")
