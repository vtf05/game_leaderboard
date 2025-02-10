from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.db.models import Sum, Count, Max
from .models import Contestant, Game, GameSession, Score
from datetime import timedelta

def home(request):
    games = Game.objects.all()
    return render(request, 'leaderboard/home.html', {'games': games})

def game_leaderboard(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    scores = Score.objects.filter(game_session__game=game)\
        .values('game_session__contestant__name')\
        .annotate(total_score=Sum('points'))\
        .order_by('-total_score')
    
    return render(request, 'leaderboard/game_leaderboard.html', {'game': game, 'scores': scores})

def global_leaderboard(request):
    scores = Score.objects.values('game_session__contestant__name')\
        .annotate(total_score=Sum('points'))\
        .order_by('-total_score')
    
    return render(request, 'leaderboard/global_leaderboard.html', {'scores': scores})

def game_popularity(request):
    games = Game.objects.all()
    popularity_scores = []

    for game in games:
        yesterday = now().date() - timedelta(days=1)
        w1 = GameSession.objects.filter(game=game, start_time__date=yesterday).values('contestant').distinct().count()
        w2 = GameSession.objects.filter(game=game, end_time=None).count()
        w3 = game.upvotes
        w4 = GameSession.objects.filter(game=game, start_time__date=yesterday).aggregate(Max('end_time'))['end_time__max']
        w5 = GameSession.objects.filter(game=game, start_time__date=yesterday).count()

        max_w1 = GameSession.objects.filter(start_time__date=yesterday).values('contestant').distinct().count() or 1
        max_w2 = GameSession.objects.filter(end_time=None).count() or 1
        max_w3 = Game.objects.aggregate(Max('upvotes'))['upvotes__max'] or 1
        max_w4 = GameSession.objects.filter(start_time__date=yesterday).aggregate(Max('end_time'))['end_time__max'] or 1
        max_w5 = GameSession.objects.filter(start_time__date=yesterday).count() or 1

        score = (0.3 * (w1 / max_w1) +
                 0.2 * (w2 / max_w2) +
                 0.25 * (w3 / max_w3) +
                 0.15 * (w4 / max_w4 if w4 else 0) +
                 0.1 * (w5 / max_w5))

        popularity_scores.append({"game": game.title, "popularity_score": score})

    return render(request, 'leaderboard/game_popularity.html', {'popularity_scores': popularity_scores})
