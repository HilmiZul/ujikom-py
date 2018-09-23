from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template import RequestContext

from petugas.models import Petugas

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    p = Petugas.objects.get(id=request.session['id'])
    return render(request, 'index.html', {'p':p})


def e404(request):
    response = render(
                'templates/layout/404.html',
                context_instance=RequestContext(request)
                )
    response.status_code = 404
    return response

def e500(request):
    response = render(
                'templates/layout/500.html',
                context_instance=RequestContext(request)
                )
    response.status_code = 500
    return response
