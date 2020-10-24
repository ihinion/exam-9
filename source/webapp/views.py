from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import PhotoForm, PhotoFormUpdate

from webapp.models import Photo


class PhotoView(DetailView):
    template_name = 'photos/photo_detail.html'
    model = Photo


class IndexView(ListView):
    template_name = 'photos/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ['-created_at']


class PhotoCreateView(CreateView):
    template_name = 'photos/photo_create.html'
    form_class = PhotoForm
    model = Photo

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect('webapp:photo_detail', pk=photo.pk)


class PhotoUpdateView(UpdateView):
    template_name = 'photos/photo_update.html'
    form_class = PhotoFormUpdate
    model = Photo

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    template_name = 'photos/photo_delete.html'
    model = Photo
    success_url = reverse_lazy('webapp:index')
