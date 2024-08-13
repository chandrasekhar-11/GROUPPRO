from django.shortcuts import render,redirect
from app.models import Player
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
def playersea(request,no,name):
    obj=Player.objects.get(id=no)
    obj.name=name
    obj.save()
    return render(request,'player.html',{'player':obj})

def playersear(request):
    if request.method == "POST":
        pid=request.POST.get('pid')
        name = request.POST.get('name')
        team = request.POST.get('team')
        position = request.POST.get('position')
        age = request.POST.get('age')
        nationality = request.POST.get('nationality')
        if Player.objects.filter(id=pid):
            obj=Player.objects.get(id=pid)
            obj.name=name
            obj.team=team
            obj.position=position
            obj.age=age
            obj.nationality=nationality
            obj.save()
            
            players = Player.objects.all()
            return render(request, 'player.html', {'players': players})

        """if pid:
           Player.objects.filter(id=pid).update(
                name=name,
                team=team,
                position=position,
                age=age,
                nationality=nationality
            ) 
        else:
            player = Player(name=name, team=team, position=position, age=age, nationality=nationality)
            player.save()"""
        
    players = Player.objects.all()
    return render(request, 'player.html', {'players': players})

def usersView(request):
    result=User.objects.all()
    return render(request, 'users.html', {'res':result})

def loginViews(request):
    c=False
    res=True
    if request.method=="POST":
        usern=request.POST.get('powerstar')
        passw=request.POST.get('superstar')
        c=User.objects.filter(username=usern).exists()
        print(c)
    return render(request,'login.html',{'res':c})

    
def loginPage(request):
    if request.method == "POST":
        usern = request.POST.get('powerstar')
        passw = request.POST.get('superstar')
        user = authenticate(request, username=usern, password=passw)
        if user is not None:
            login(request, user)
            return redirect('postsPage')  # Redirect to the posts page after successful login
        else:
            return render(request, 'index.html', {'res': False})  # Invalid login
    return render(request, 'index.html', {'res': True})

def aboutPage(request):
    return render(request,'about.html')

def contactPage(request):
    return render(request,'contact.html')

@login_required(login_url="loginPage")
def postsPage(request):
    return render(request,'posts.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

from django.contrib.auth import authenticate, login






    

