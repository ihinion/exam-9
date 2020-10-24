from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.models import Profile
from webapp.models import Photo, Favorite

# юзернейм - пароль
# admin admin / суперюзер
# test test / пользователь без прав
# test2 test2 / пользователь с правами на удаление и редактирование всех фотографий

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