from django.urls import path
from .views import (NewspaperListOne, NewspaperDetailOne,
                    NewspaperListTwo, NewspaperDetailTwo)

urlpatterns = [
    path('newspaper1/', NewspaperListOne.as_view()),
    path('newspaper1/<int:pk>', NewspaperDetailOne.as_view()),
    path('newspaper2/', NewspaperListTwo.as_view()),
    path('newspaper2/<int:pk>', NewspaperDetailTwo.as_view()),
]