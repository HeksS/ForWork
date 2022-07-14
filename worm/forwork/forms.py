from .models import Role,Staf
from django.forms import ModelForm,TextInput,Select


# Форма для добавления роли
class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['Name', 'Kategor']

        widgets = {
            "Name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название роли'

            }),
            "Kategor": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'

            }),
        }


# Форма для добавления сотрудника
class UsersForm(ModelForm):
    class Meta:
        model = Staf

        fields = ['FIO', 'Gender','Age','Post']

        widgets = {
            "FIO": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'ФИО'

            }),
            "Gender": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пол'

            }),
            "Age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'

            }),
            "Post": Select(attrs={
                'class': 'form-control'
            }),
        }