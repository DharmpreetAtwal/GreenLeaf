from django.db import models

from admin_dash.models import User


# Create your models here.
class Ticket(models.Model):
    ticket_status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    ticket_text = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)