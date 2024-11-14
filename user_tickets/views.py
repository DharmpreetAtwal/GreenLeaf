from django.http import HttpResponse
from django.template import loader


# Create your views here.
def user_tickets_view(request):
    template = loader.get_template("user_tickets.html")
    return HttpResponse(template.render())