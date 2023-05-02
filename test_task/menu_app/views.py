from django.views.generic import DetailView, ListView, TemplateView
from .models import Menu


class MenusView(TemplateView):
    template_name = 'menu_app/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.id:
            context['menus'] = Menu.objects.all()
        return context

