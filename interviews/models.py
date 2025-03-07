import uuid

from django.db import models


class Chat(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=150, editable=False)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='chats')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
            self.title = f'Chat {self.job.title} - {self.uuid}'
        super().save(*args, **kwargs)


class Message(models.Model):
    ROLE_CHOICES = (
        ('system', 'Sistema'),
        ('user', 'Candidato'),
        ('assistant', 'Entrevistador'),
    )
    chat = models.ForeignKey(
        'interviews.Chat', on_delete=models.CASCADE, related_name='messages'
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.role} - {self.chat.title}'
