from django.http import HttpResponse
from django.template import loader
from .models import User

# Create your views here.
def admin_dash(request):
    user_list = User.objects.all().values()
    context = {'user_list': user_list}
    template = loader.get_template('admin_dash.html')
    return HttpResponse(template.render(context, request))