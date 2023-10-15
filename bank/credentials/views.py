from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from credentials.models import District,Branch
from .forms import DistrictBranchForm
from .forms import BranchForm
from django.http import JsonResponse
from .forms import BankAccountApplicationForm
app_name='credentials'

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('credentials:register')
            else:
                 user=User.objects.create_user(username=username,password=password)
                 user.save();
                 return redirect('credentials:login')
        else:
            messages.info(request,"Password not match")
            return redirect('credentials:register')
        return redirect('/')

    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('credentials:all_districts')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('credentials:login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def all_districts(request):
    districts = District.objects.all()
    branches = Branch.objects.none()
    if request.method == 'POST':
        selected_district_id = request.POST.get('district')
        if selected_district_id:
            branches = Branch.objects.filter(district_id=selected_district_id)
    return render(request, 'account1.html', {'districts': districts, 'branches': branches})
def accountsubmission(request):
    return render(request, 'accountsubmission.html')
def back(request):
    return render(request, 'home.html')
def district_branch_view(request):
    form = DistrictBranchForm()
    return render(request, 'credentials/account.html', {'form': form})
def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district=district_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)
def all_branches(request):
    branches = Branch.objects.all()
    return render(request, 'navbar.html', {'branches': branches})
def district_wikipedia(request):
    return render(request, 'district_wikipedia.html')


def apply_for_bank_account(request):
    if request.method == 'POST':
        form = BankAccountApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accountsubmission')  # Redirect to a success page
    else:
        form = BankAccountApplicationForm()

    return render(request, 'account.html', {'form': form})

