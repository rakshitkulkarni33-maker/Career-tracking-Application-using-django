from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Application
from .forms import ApplicationForm,SignupForm
def home(request):
    return redirect("dashboard") if request.user.is_authenticated else render(request,"tracker/home.html")
def signup(request):
    if request.user.is_authenticated:return redirect("dashboard")
    form=SignupForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        user=form.save();login(request,user);messages.success(request,"Welcome to CareerNest!");return redirect("dashboard")
    return render(request,"tracker/auth.html",{"form":form,"mode":"signup"})
def login_view(request):
    if request.user.is_authenticated:return redirect("dashboard")
    if request.method=="POST":
        user=authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        if user:
            login(request,user);return redirect("dashboard")
        messages.error(request,"Username or password is incorrect.")
    return render(request,"tracker/auth.html",{"mode":"login"})
def logout_view(request):
    logout(request);return redirect("login")
@login_required
def dashboard(request):
    apps=Application.objects.filter(user=request.user)
    counts={s:apps.filter(status=s).count() for s,_ in Application.STATUS_CHOICES}
    upcoming=apps.filter(interview_date__isnull=False).order_by("interview_date")[:5]
    recent=apps.order_by("-created_at")[:5]
    return render(request,"tracker/dashboard.html",{"counts":counts,"total":apps.count(),"upcoming":upcoming,"recent":recent})
@login_required
def application_list(request):
    apps=Application.objects.filter(user=request.user)
    q=request.GET.get("q","");status=request.GET.get("status","")
    if q:apps=apps.filter(Q(company__icontains=q)|Q(role__icontains=q)|Q(location__icontains=q))
    if status:apps=apps.filter(status=status)
    return render(request,"tracker/applications.html",{"apps":apps,"q":q,"status":status,"choices":Application.STATUS_CHOICES})
@login_required
def application_create(request):
    form=ApplicationForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        obj=form.save(commit=False);obj.user=request.user;obj.save();messages.success(request,"Application added.");return redirect("applications")
    return render(request,"tracker/form.html",{"form":form,"heading":"Add opportunity"})
@login_required
def application_edit(request,pk):
    obj=get_object_or_404(Application,pk=pk,user=request.user);form=ApplicationForm(request.POST or None,instance=obj)
    if request.method=="POST" and form.is_valid():form.save();messages.success(request,"Application updated.");return redirect("applications")
    return render(request,"tracker/form.html",{"form":form,"heading":"Edit opportunity"})
@login_required
def application_delete(request,pk):
    obj=get_object_or_404(Application,pk=pk,user=request.user)
    if request.method=="POST":obj.delete();messages.success(request,"Application deleted.");return redirect("applications")
    return render(request,"tracker/delete.html",{"obj":obj})
