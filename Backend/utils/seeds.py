from django.contrib.auth.models import User

class DataSeeder:
    def __init__(self):
        self._user_seed()
    
    def get_users(self, *args: str) -> tuple[User, ...]:
        users = list(User.objects.filter(username__in=args))
        if len(users) != len(args):
            missing = set(args) - {u.username for u in users}
            raise ValueError(f"Usuários não encontrados no seed: {missing}")
        return tuple(users)

    def _user_seed(self):
        User.objects.create_user(id=1, username='admin', password='adminpass', is_staff=True)
        User.objects.create_user(id=2, username='user', password='userpass')