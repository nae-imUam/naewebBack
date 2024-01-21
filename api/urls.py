from django.urls import path, include
from .views import signup, login_view
from rest_framework.routers import DefaultRouter
from .views import MiniTestViewSet, check_username_availability#,  get_minitest_by_test_number

router = DefaultRouter()
router.register(r'minitests', MiniTestViewSet)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('check-username/<str:username>/', check_username_availability, name='check_username_availability'),
    #path('minitests/<int:test_number>/', get_minitest_by_test_number, name='get_minitest_by_test_number'),
    path('', include(router.urls)),
    # Add more URL patterns as needed
]

