# cards/views.py

from django.views.generic import (
    ListView,
    CreateView,
)

from .models import Card

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")
    
class CardCreateView(CreateView)