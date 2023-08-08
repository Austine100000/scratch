from django.shortcuts import render, redirect
from home.models import Member


# Create your views here.
def signup(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        username=request.POST['username'], password=request.POST['password'],
                        email=request.POST['email'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'signup.html')


def login(request):
    return render(request, 'signin.html')


def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'],
                                        )
            return render(request, 'homepage.html', {'member': member})
        else:
            return render(request, 'signin.html')
