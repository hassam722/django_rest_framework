from django.urls import path,include
from .views import carlist_detail_view,carlist_view,ShowRoom_list_view,Review_list_view,Review_detail_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('reviews',Review_list_view,basename="review_list_view")

urlpatterns = [

    path('list/', carlist_view,name='car_list_view'),
    path('<int:pk>/', carlist_detail_view,name='car_detail_view'),
    path('showroom/', ShowRoom_list_view.as_view(),name='showroom_list_view'),
    path('reviews/',Review_list_view.as_view(),name = 'review_list_view'),
    path('reviews/<int:pk>/',Review_detail_view.as_view(),name ='review_detail_view'),
    # path("",include(router.urls))
    
]
