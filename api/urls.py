from django.urls import path, include
from .views import signup, login_view
from rest_framework.routers import DefaultRouter
from .views import MiniTestViewSet, check_username_availability,  get_minitest_by_test_number, MiniTestInfoListView, QuizDataUpdateView, QuizDataRetrieveView

router = DefaultRouter()
router.register(r'minitests', MiniTestViewSet)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('check-username/<str:username>/', check_username_availability, name='check_username_availability'),
    path('minitests/<int:test_number>/', get_minitest_by_test_number, name='get_minitest_by_test_number'),
    path('minitests/<str:class_name>/<str:subject>/', MiniTestInfoListView.as_view(), name='mini-test-list'),
    path('', include(router.urls)),
    path('userdata/<str:username>/update_quiz_data/', QuizDataUpdateView.as_view(), name='update_quiz_data'),
    path('userdata/<str:username>/quiz_data/', QuizDataRetrieveView.as_view(), name='quiz_data'),
    # Add more URL patterns as needed
]

