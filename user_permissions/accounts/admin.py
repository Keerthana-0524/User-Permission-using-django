
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.utils.html import mark_safe

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = '__all__'

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'permissions', 'edit_link', 'delete_link')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

    def permissions(self, obj):
        if obj.is_superuser:
            return mark_safe('Superuser')
        elif obj.is_staff:
            return mark_safe('Admin')
        else:
            return mark_safe('User')

    def edit_link(self, obj):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return mark_safe(f'<a href="{obj.id}/change/">📝</a>')
        else:
            return ' '

    def delete_link(self, obj):
        if self.request.user.is_superuser:
            return mark_safe(f'<a href="{obj.id}/delete/">❌</a>')
        else:
            return



    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)


admin.site.register(CustomUser, CustomUserAdmin)
