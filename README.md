# Game Leaderboard System

This is a Django-based Game Leaderboard system that allows users to:

- Manage contestants and games.
- Assign scores to contestants in different games.
- View leaderboards at global and game-specific levels.
- Calculate and display game popularity based on multiple metrics.
- Automatically update game popularity every 5 minutes.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/game-leaderboard.git
cd game-leaderboard
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations leaderboard
python manage.py migrate
```

### 5. Create a Superuser (for Admin Access)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Access the app at: `http://127.0.0.1:8000/`

---

## Step-by-Step Guide to Test Features

Follow these steps in the Django shell (`python manage.py shell`) to test the leaderboard system.

### 1. Create 5 or More Games

```python
from leaderboard.models import Game

g1 = Game.objects.create(title="Battle Royale")
g2 = Game.objects.create(title="Chess Masters")
g3 = Game.objects.create(title="Speed Racer")
g4 = Game.objects.create(title="Puzzle Mania")
g5 = Game.objects.create(title="Space Wars")
```

### 2. Add Multiple Contestants

```python
from leaderboard.models import Contestant

c1 = Contestant.objects.create(name="Alice")
c2 = Contestant.objects.create(name="Bob")
c3 = Contestant.objects.create(name="Charlie")
c4 = Contestant.objects.create(name="David")
c5 = Contestant.objects.create(name="Eve")
```

### 3. Add Contestants to Games at Different Timestamps

```python
from leaderboard.models import GameSession
from django.utils.timezone import now, timedelta

session1 = GameSession.objects.create(game=g1, contestant=c1, start_time=now() - timedelta(minutes=30))
session2 = GameSession.objects.create(game=g1, contestant=c2, start_time=now() - timedelta(minutes=20))
session3 = GameSession.objects.create(game=g2, contestant=c3, start_time=now() - timedelta(minutes=25))
session4 = GameSession.objects.create(game=g2, contestant=c4, start_time=now() - timedelta(minutes=10))
session5 = GameSession.objects.create(game=g3, contestant=c5, start_time=now() - timedelta(minutes=15))
```

### 4. Assign Scores to Contestants in Different Games

```python
from leaderboard.models import Score

Score.objects.create(game_session=session1, points=100)
Score.objects.create(game_session=session2, points=120)
Score.objects.create(game_session=session3, points=80)
Score.objects.create(game_session=session4, points=140)
Score.objects.create(game_session=session5, points=110)
```

### 5. Get the Leaderboard at Game and Global Level

#### Game-Specific Leaderboard

Visit: `http://127.0.0.1:8000/leaderboard/game/<game_id>/`

Example (for game ID 1):

```bash
http://127.0.0.1:8000/leaderboard/game/1/
```

#### Global Leaderboard

Visit: `http://127.0.0.1:8000/leaderboard/global/`

### 6. Get the Game Popularity Index

#### First Call

Visit: `http://127.0.0.1:8000/popularity/`

#### Wait 6 Minutes, Then Call Again

Visit: `http://127.0.0.1:8000/popularity/`

The second call should show different results because the popularity index updates every 5 minutes.

---

## Features

✅ Manage games and contestants.
✅ Assign scores to contestants.
✅ Game & global leaderboards.
✅ Game popularity index auto-refreshes every 5 minutes.
✅ Bootstrap UI for an improved interface.

---

## Future Improvements

- Add user authentication.
- Implement WebSockets for real-time updates.
- Enhance API support with Django REST Framework.

---

## License

MIT License
