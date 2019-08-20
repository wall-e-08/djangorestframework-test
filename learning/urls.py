from django.urls import path
from .views import (newspaper_list, newspaper_detail,
                    NewspaperListOne, NewspaperDetailOne,
                    NewspaperListTwo, NewspaperDetailTwo,
                    NewspaperListThree, NewspaperDetailThree,
                    UserView)

urlpatterns = [
    path('newspaper/', newspaper_list),
    path('newspaper/<int:pk>', newspaper_detail),

    path('newspaper1/', NewspaperListOne.as_view()),
    path('newspaper1/<int:pk>', NewspaperDetailOne.as_view()),

    path('newspaper2/', NewspaperListTwo.as_view()),
    path('newspaper2/<int:pk>', NewspaperDetailTwo.as_view()),
    
    path('newspaper3/', NewspaperListThree.as_view()),
    path('newspaper3/<int:pk>', NewspaperDetailThree.as_view()),
    
    path('users/', UserView.as_view())
]
