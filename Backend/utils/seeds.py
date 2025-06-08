from django.core.management import call_command
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User


def run_dataseed(usernames: list[str]) -> tuple[User, ...]:
    """Limpa o banco, popula os dados de seed e retorna os usuários solicitados.
        usernames: Lista de nomes de usuário para retornar após popular o banco.
        Returns: Tupla com objetos User correspondentes aos usernames informados.
    """
    call_command('flush', verbosity=0, interactive=False)
    _seeds()

    users = list(User.objects.filter(username__in=usernames))
    if len(users) != len(usernames):
        missing = set(usernames) - {u.username for u in users}
        raise ValueError(f"Usuários não encontrados no seed: {missing}")
    return tuple(users)
    
def _seeds():
    """Executa todas as seeds"""
    _user_seed()

def _user_seed():
    """Cria usuários padrão para testes."""
    User.objects.create_user(id=1, username='admin', password='adminpass', is_staff=True)
    User.objects.create_user(id=2, username='user', password='userpass')