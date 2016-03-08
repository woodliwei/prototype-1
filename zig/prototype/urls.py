
from django.conf.urls import url
from . import views
from django.contrib import admin


admin.autodiscover()

app_name = "prototype"
urlpatterns = [
    url(r'^bigdata/$', views.bigdata_trend_testing, name='bigdata'),
    url(r'^strategy/$', views.strat_trend_manage, name='strategy'),
    url(r'^strategymanage/$', views.strat_manage, name='strategy_manage'),
    url(r'^strategyshop/$', views.strat_shop, name='strategy_shop'),
    url(r'^bigdata_result/$', views.bigdata_trend_test_result, name='bigdata_result'),
    url(r'^bigdata_result_new/$', views.bigdata_trend_test_result_new, name='bigdata_result_new'),
    url(r'^bigdata_mktdata/$', views.bigdata_mktdata, name='bigdata_mktdata'),
    url(r'^zigadmin/$', views.zig_admin),
    url(r'^aboutus/$', views.about_us, name='aboutus'),
    url(r'^admin/', admin.site.urls),
    url(r'^login_test/', views.login_testing, name='login_test'),
    url(r'^api/$', views.api, name='api'),
    url(r'^$', views.strat_trend_manage),
    url(r'^.+/$', views.under_construction),
]

