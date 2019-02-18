from django.shortcuts import render
from .models import accounts
# Create your views here.
def login(request):
	all_accounts = accounts.objects.all()
	return render(request,'cp1/login.html',{'accounts' : all_accounts})

def signup_submission(request):
	email = request.POST["email"]
	username = request.POST["username"]
	password = request.POST["pwd"]

	account = accounts(email=email,password=password,name=username)
	account.save()
	return render(request,'cp1/login.html')
