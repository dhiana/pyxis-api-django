from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

def fake_runs_api(request):
  response = HttpResponse("")
  response.status_code = 200
  return response

urlpatterns = [
    # Examples:
    # url(r'^$', 'pyxis_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^runs/$', fake_runs_api),
    url(r'^admin/', include(admin.site.urls)),
]
