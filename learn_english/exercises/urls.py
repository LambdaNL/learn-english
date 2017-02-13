"""learn_english URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r"^exercise/(?P<name>verbs|adverbs|imperatives|quantifiers|gerund)/(?P<level>A1|A2|B1|B2|C1|.*)", views.exercise, name='exercise'),
    url(r"^adverbs/(?P<level>A1|A2|B1|B2|C1|.*)", views.adverbs, name='adverbs'),
    url(r"^verbs/(?P<level>A1|A2|B1|B2|C1|.*)", views.verbs, name='verbs'),
    url(r"^imperatives/(?P<level>A1|A2|B1|B2|C1|.*)", views.imperatives, name='imperatives'),
    url(r"^gerund/(?P<level>A1|A2|B1|B2|C1|.*)", views.gerund, name='gerund'),
    url(r"^quantifiers/(?P<level>A1|A2|B1|B2|C1|.*)", views.quantifiers, name='quantifiers'),
    url(r'^results/', views.results, name='results'),
    url(r'^startg/', views.startg, name='startg'),
]
