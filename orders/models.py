from django.db.models.deletion import PROTECT
from animals.models import Wish
from django.db import models

class Order(models.Model):
    NEW = 'New'
    PEND = 'Pending'
    COMP = 'Complete'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (PEND, 'Pending'),
        (COMP, 'Complete')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wish = models.ForeignKey(Wish, on_delete=PROTECT)
    status = models.CharField(max_length=72, choices=STATUS_CHOICES, default=NEW)

    def __str__(self):
        return f'{self.status} Order | ID: {self.id}'