"""Week6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from Modules.views import(
    home1_view,
    About1_view,
    ContactUs1_view,
    Help1_view,
    Abs_summarize,
    Ext_summarize,
    ODQA_dataset,
    SQuAD_dataset,
    #detail,
    get_articles,
    get_contents,
    
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home1_view,name="home1"),
    path('About1/',About1_view,name="About1"),
    #path('Projects/',Projects_view,name="Projects"),
    path('dataset/Abs_summarize',Abs_summarize,name="Abs_summarize"),
    path('dataset/Ext_summarize',Ext_summarize,name="Ext_summarize"),
    path('ODQA_dataset',ODQA_dataset,name="ODQA_dataset"),
    path('SQuAD_dataset',SQuAD_dataset,name="SQuAD_dataset"),
    #path('dataset/Abs_summerize/<str:article_id>',detail, name='detail'),
    path('ContactUs1/',ContactUs1_view,name="ContactUs1"),
    path('Help1/',Help1_view,name="Help1"),
    path('dataset/<str:dataset>/<str:folder_path>',get_articles, name='get_articles'),
    path('dataset/<str:dataset>/<str:folder_path>/<str:article>',get_contents, name ='get_contents'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

