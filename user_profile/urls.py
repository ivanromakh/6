from django.conf.urls import url
import views

urlpatterns = [
    url(r'^user/',
        views.UserProfileDetail.as_view(),
        name='user_profile_detail'),
    url(r'^user/update/$',
        views.UserProfileUpdate.as_view(),
        name='user_profile_edit'),
]