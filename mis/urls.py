from django.conf.urls import static
from django.urls import path,include
from django.contrib import admin
from mis import settings
import workflow.views
import invent.urls
import basedata.urls
import selfhelp.urls
import mis.views

urlpatterns = [
    path('', mis.views.home),
    path("admin/<app>/<model>)/<int:object_id>/start",
        workflow.views.start),
    path("admin/<app>/<model>/<int:object_id>/approve/<int:operation>",
        workflow.views.approve),
    path("admin/<app>/<model>/<int:object_id>/restart/<int:instance>",
        workflow.views.restart),
    #path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('admin/invent/', include(invent.urls)),
    path('admin/basedata/', include(basedata.urls)),
    path('admin/selfhelp/', include(selfhelp.urls)),

    #url(r'^$', mis.views.home),
    #url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/start", workflow.views.start),
    #url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/approve/(?P<operation>\d+)", workflow.views.approve),
    #url(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/restart/(?P<instance>\d+)", workflow.views.restart),
    #path('grappelli/', include('grappelli.urls')),
    #path('admin/', admin.site.urls),
    #url(r'^admin/invent/', include(invent.urls)),
    #url(r'^admin/basedata/', include(basedata.urls)),
    #url(r'^admin/selfhelp/', include(selfhelp.urls)),
]
urlpatterns += static.static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
