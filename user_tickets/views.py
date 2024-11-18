from django.http import HttpResponse
from django.template import loader

from admin_dash.models import User
from user_tickets.models import Ticket


# Create your views here.
def user_tickets_view(request, id):
    user = User.objects.get(pk=id)
    tickets = Ticket.objects.filter(user_id=id)
    template = loader.get_template("user_tickets.html")
    context = {'tickets': tickets, 'user': user}

    return HttpResponse(template.render(context, request))