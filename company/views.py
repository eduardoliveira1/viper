# from django.shortcuts import render, redirect 
# from games.models import Game
# from company.models import Company
# from user.models import User

# # Create your views here.
# def company_dashboard(request):
#     user_id = request.session.get('user_id')
#     if not user_id:
#         return redirect('login')
    
#     user = User.objects.get(id=user_id)
#     companies = Company.objects.filter(owner=user)
#     games = Game.objects.filter(company__in=companies)

#     context = {
#         'companies': companies,
#         'user': user,
#         'games': games
#     }

#     return render(request, 'company/dashboard.html', context)
