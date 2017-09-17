from django.conf.urls import url
from views import *

urlpatterns = [

    url(r'^$', view=accueil, name="accueil"),
    url(r'^boutique/', view=boutique, name="boutique"),
    url(r'^realisations/', view=realisations, name='realisations'),

]
