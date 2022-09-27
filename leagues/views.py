from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker


def index(request):
    context = {
        "leagues": League.objects.all(),
        "teams": Team.objects.all(),
        "coopers": Player.objects.filter(last_name__exact='Cooper').exclude(first_name__exact='Jousha'),
        # 'players': Player.objects.all(),
        'joushas': Player.objects.filter(first_name__exact='Joshua'),
        'alexander': Player.objects.filter(first_name__exact='Alexander').filter(last_name__exact='Wyatt'),
    }
    return render(request, "leagues/index.html", context)


def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)

    return redirect("index")
