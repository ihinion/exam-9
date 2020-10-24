from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.models import Profile
from webapp.models import Photo, Favorite


class ProfileInline(admin.StackedInline):
    model = Profile
    exclude = []


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Photo)
admin.site.register(Favorite)