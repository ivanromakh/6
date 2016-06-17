from django.views.generic import DetailView
from django.shortcuts import render_to_response
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from .models import UserProfile, assure_user_profile_exists
from django.template.context import RequestContext

class UserProfileDetail(DetailView):
    model = UserProfile
    def user(self,request):
        requestcontext = RequestContext(request)
        render_to_response("userprofile/userprofile_detail.html")

class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ('homepage',)

    def get(self, request, *args, **kwargs):
        assure_user_profile_exists(kwargs['pk'])
        return (super(UserProfileUpdate, self).
                get(self, request, *args, **kwargs))