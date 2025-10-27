from rest_framework import serializers

from tasks.models import Task
from tasks.models import Topic
from tags.models import Tag
from tags.serializers import TagSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'description', 'is_done', 'created_at', 'finished_at']
        read_only_fields = ['id', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    topics  = TopicSerializer(many=True)
    
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, write_only=True)


    class Meta:
        model = Task
        fields = ['id', 'owner', 'title', 'description', 'tags', 'topics', 'created_at', 'finished_at']   
        read_only_fields = ['id', 'created_at'] 

    def to_representation(self, instance):
        """Modifica a saída para retornar os objetos de tags"""
        rep = super().to_representation(instance)
        rep['tags'] = TagSerializer(instance.tags.all(), many=True).data
        return rep


    def create(self, data):
        """ Usado para salvar no banco os dados de tags e topics do relaciomaneto"""
        topics_data = data.pop('topics', [])
        tags = data.pop('tags', [])
        task = Task.objects.create(**data)
        task.tags.set(tags)
        for topic_data in topics_data:
            Topic.objects.create(task=task, **topic_data)
        return task
    
    def update(self, instance, data):
        """ Usado para atualizar no banco os dados de tags e topics do relaciomaneto"""
        topics_data = data.pop('topics', None)
        tags_data = data.pop('tags', None)

        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()

        if tags_data is not None:
            instance.tags.set(tags_data)

        if topics_data is not None:
            instance.topics.all().delete()
            for topic_data in topics_data:
                Topic.objects.create(task=instance, **topic_data)

        return instance


