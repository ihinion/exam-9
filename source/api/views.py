from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.generic import View
from webapp.models import Photo, Favorite


class PhotoFavorView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        fav, created = Favorite.objects.get_or_create(photo=photo, user=request.user)
        if created:
            return HttpResponse()
        else:
            return HttpResponseForbidden()


class PhotoUnFavorView(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        fav = get_object_or_404(photo.favorites, user=request.user)
        fav.delete()
        return HttpResponse()