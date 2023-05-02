from django.db import models
from django.urls import reverse


class Menu(models.Model):
    menu_name = models.CharField(max_length=60, verbose_name='Название меню', unique=True)
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    def get_url(self):
        return reverse('branch', args=self.slug)

    def __str__(self):
        return f'{self.menu_name} - {self.slug}'


class MenuItem(models.Model):
    mi_name = models.CharField(max_length=60, verbose_name='Название пункта меню', unique=True)
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню')
    mi_parent = models.ForeignKey('MenuItem', on_delete=models.CASCADE, verbose_name='Элемент-родитель', null=True, blank=True)

    def get_url(self):
        return reverse('branch', args=self.slug)

    def __str__(self):
        if self.mi_parent:
            return f'Ветка {self.mi_name} - {self.slug}. Меню - {self.menu}. Ветка-родитель - {self.mi_parent.mi_name}'
        else:
            return f'Корневая ветка {self.mi_name} - {self.slug}. Меню - {self.menu}.'

