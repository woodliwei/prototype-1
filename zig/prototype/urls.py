
from django.conf.urls import url
from . import views


app_name = "prototype"
urlpatterns = [
    url(r'^bigdata/$', views.bigdata_trend_testing, name='bigdata'),
    url(r'^strategy/$', views.strat_trend_manage, name='strategy'),
    url(r'^bigdata_result/$', views.bigdata_trend_test_result, name='bigdata_result'),
    url(r'^$', views.strat_trend_manage),
]