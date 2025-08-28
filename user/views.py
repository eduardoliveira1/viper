from django.shortcuts import render, redirect
from user.models import User, find_user_by_id, create_user
from games.models import Game
from django.contrib import messages
from company.models import Company

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        possibleUser = User.objects.filter(username=username).first()

        if possibleUser and possibleUser.password == password:
            possibleUser.online = True
            possibleUser.save()
            request.session['user_id'] = possibleUser.id
            messages.success(request, "Login successful!")
            return redirect('game_list')
        
        elif not possibleUser:
            messages.error(request, "User not found. Please sign up.")
            print("User not found. Please sign up.")
        else:
            messages.error(request, "Login failed. Please check your username and password.")

        print("POST data:", username, password)


    return render(request, 'user/login.html')

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        confirmationPassword = request.POST.get('confirmationPassword')

        if password != confirmationPassword:
            messages.error(request, "Passwords do not match. Please try again.")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please use a different email.")

        else:
            newUser = create_user(username, firstName, lastName, email, password)
            request.session['user_id'] = newUser.id
            messages.success(request, "Sign up successful! Welcome!")
            return redirect('game_list')
    return render(request, 'user/signUp.html')

def profile_info(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user = find_user_by_id(user_id)
    if not user:
        messages.error(request, "User not found!")
        return redirect('login')

    if request.method == 'POST':
        if 'cancelBtn' in request.POST:
            return redirect('profile_info')  

        elif 'submitBtn' in request.POST:
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.username = request.POST.get('username', user.username)
            user.email = request.POST.get('email', user.email)
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
            user.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_info')     

    # company = Company.objects.filter(owner=user).first()
    
    context = {
        'user': user,
        # 'company': company,
    }
    return render(request, 'user/profile_info.html', context)

def logout(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = find_user_by_id(user_id)
        user.logout()
        del request.session['user_id']
        messages.success(request, "Logged out successfully!")
    return redirect('login')

def purchased_games(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user = User.objects.filter(id=user_id).first()
    purchased_games = user.purchased_games.all()  
    company = Company.objects.filter(owner=user).first()

    context = {
        'purchased_games': purchased_games,
        'company': company,
        'user': user,
    }
    return render(request, 'user/purchased_games.html', context)

def buyGame(request, id_game):
    user_id = request.session.get('user_id')

    user = User.objects.get(id=user_id)

    game = Game.objects.get(id=id_game)

    if not user:
        messages.error(request, 'You need to be logged to buy a game!')
    
    user.buyGame(game)
    messages.success(request, 'The game was purchased successfully!')
    return redirect('game_detail', id=game.id)

def delete_account(request):
    user_id = request.session.get('user_id')

    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.delete_account()
        
        if 'user_id' in request.session:
            del request.session['user_id']
        messages.success(request, "Your account has been deleted successfully.")
    return redirect('signup')
