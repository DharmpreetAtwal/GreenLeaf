from django.http import HttpResponse
from django.template import loader


# Create your views here.
def admin_dash(request):
    template = loader.get_template('admin_dash.html')
    return HttpResponse(template.render())