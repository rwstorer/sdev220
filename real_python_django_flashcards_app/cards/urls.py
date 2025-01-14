from django.urls import path
# Removed: from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
#        TemplateView.as_view(template_name="cards/base.html"),
#        name="home"
    ),
]