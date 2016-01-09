
from django.conf.urls import url
from . import views


app_name = "prototype"
urlpatterns = [
    url(r'^bigdata/$', views.bigdata_trend_testing, name='bigdata'),
    url(r'^strategy/$', views.strat_trend_manage, name='strategy'),
    url(r'^strategymanage/$', views.strat_manage, name='strategy_manage'),
    url(r'^strategyshop/$', views.strat_shop, name='strategy_shop'),
    url(r'^bigdata_result/$', views.bigdata_trend_test_result, name='bigdata_result'),
    url(r'^bigdata_result_dynamic/$', views.bigdata_trend_test_result_dynamic, name='bigdata_result_dynamic'),
    # url(r'^bigdata_history/$', views.bigdata_history, name='bigdata_history'),
    url(r'^aboutus/$', views.about_us, name='aboutus'),
    url(r'^$', views.strat_trend_manage),
    url(r'^.+/$', views.under_construction),
]

