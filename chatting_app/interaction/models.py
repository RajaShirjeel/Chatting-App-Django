from django.db import models

from user.models import CustomUser

# Create your models here.
class Chat(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    message = models.CharField(max_length = 1000)
    receive_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['receive_time']

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.receive_time}"
    
    