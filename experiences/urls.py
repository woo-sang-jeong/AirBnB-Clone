from django.urls import path
from .views import Perks, PerkDetail, Experiences, ExperienceDetail


urlpatterns = [
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkDetail.as_view()),
    path("", Experiences.as_view()),
    path("<int:pk>", ExperienceDetail.as_view()),
]
