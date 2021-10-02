from django.shortcuts import render
# HttpResponse
# from home.models import contacts


# Create your views here.
def home(request):
    return render(request, 'home.html')


# def contact(request):
#     # if request.method == "POST":
#     #     first = request.POST.get('first')
#     #     last = request.POST.get('last')
#     #     contact = contacts(first=first, last=last)
#     #     contact.save()

#     return render(request, 'contact.html')
