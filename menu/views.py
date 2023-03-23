from django.views import generic


class MenuView(generic.TemplateView):
    template_name = "menu/index.html"
