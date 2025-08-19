from django.contrib.auth.models import User

from tags.models import Tag
from tasks.models import Topic, Task

class DataSeeder:
    def __init__(self):
        self._user_seed()
        self._tag_seed()
        self._task_seed()
        self._topic_seed()
    
    def get_users(self, *args: str) -> tuple[User, ...]:
        users = list(User.objects.filter(username__in=args))
        if len(users) != len(args):
            missing = set(args) - {u.username for u in users}
            raise ValueError(f"Usuários não encontrados no seed: {missing}")
        return tuple(users)

    def _user_seed(self):
        User.objects.create_user(id=1,
                                 username='admin',
                                 password='adminpass',
                                 is_staff=True)
        User.objects.create_user(id=2,
                                 username='user',
                                 password='userpass')
    
    def _tag_seed(self):
        Tag.objects.create(id=1,
                           name='red',
                           color='#FF0000')
        Tag.objects.create(id=2,
                           name='black',
                           color='#000000')

    def _task_seed(self):
        user = User.objects.get(id=1)
        tag1 = Tag.objects.get(id=1)
        tag2 = Tag.objects.get(id=2)

        task = Task.objects.create( id=1,
                                   owner=user,
                                   title='test',
                                   description='is a test')
        task.tags.add(tag1, tag2)

        Task.objects.create(id=2,
                            owner=user,
                            title='test2',
                            description='is a test')

    def _topic_seed(self):
        task = Task.objects.get(id=1)
        Topic.objects.create(task=task,
                             description='test task 1',
                             is_done=False)
        
        Topic.objects.create(task=task,
                             description='test task 2')
