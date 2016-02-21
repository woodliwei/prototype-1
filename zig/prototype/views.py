# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render_to_response
from .controls import *
from .product import *
from Utility import webapi
from rtmd import *
from django.http import HttpResponse, HttpResponseRedirect


def bigdata_trend_testing(requst):
    return render_to_response("bigdata_trend_testing.html", get_context("bigdata_trend_testing"))


def bigdata_trend_test_result(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    if not request.user.has_perm('prototype.view_test_result'):
        return HttpResponse("您没有运行回测的权限，请联系管理员。")
    return render_to_response('bigdata_trend_test_result.html', get_context("bigdata_trend_test_result"))

def bigdata_trend_test_result_new(request):
    return render_to_response('bigdata_trend_test_result_new.html', get_context("bigdata_trend_test_result"))

def bigdata_mktdata(request):
    return render_to_response('bigdata_mkt_data.html', get_context("bigdata_mkt_data"))


def strat_trend_manage(requst):
    return render_to_response("strat_manage_index.html", get_context("strat_manage_index"))


def strat_manage(requst):
    return render_to_response("strat_manage.html", get_context("strat_manage"))


def strat_shop(requst):
    return render_to_response("strat_shop.html", get_context("strat_shop"))


def zig_admin(request):
    message = "No action specified."
    if request.GET.get('refreshproduct') == 'true':
        message = ProductHelper.refresh_productDB(webapi)
    return render_to_response("zigadmin.html", {"message": message, "no_navBar": True})


def api(request):
    result = ""
    nocache = False

    if request.GET.get('ty') == 'rtmd':
        products = request.GET.get('value')
        if products is not None and len(products) > 0:
            result = SinaRTMD(webapi.getDetailedRtmd(products)).toJsonString()
            nocache = True
    response = HttpResponse(result)
    # set no cache in repsonse header
    if nocache:
        response['Cache-Control'] = 'no-cache'
    return response


def about_us(requst):
    return render_to_response("about_us.html", get_context("about_us"))


def under_construction(requst):
    return render_to_response("under_construction.html", get_context("under_construction"))

# Set active items in Title Bar and Nav Bar
def get_context(pageName):
    context_mapping = {
        "bigdata_trend_testing":
            {
                "title_bigdata": "active",
                "nav_trendTest": "active",
                "buy_indexes_list": SelectDropdown("buyList", "multiselect", MyData.buyindexes),
                "sell_indexes_list": SelectDropdown("sellList", "multiselect", MyData.sellindexes),
            },
        "bigdata_trend_test_result":
            {
                "title_bigdata": "active",
                "nav_historyTest": "active",
                "testResults": MyData.testResults,
            },
        "bigdata_mkt_data":
            {
                "title_bigdata": "active",
                "nav_mktData": "active",
            },
        "strat_manage":
            {
                "title_strategy": "active",
                "nav_strategy_mge": "active",
                "buy_indexes_list": SelectDropdown("buyList", "multiselect", MyData.buyindexes),
                "sell_indexes_list": SelectDropdown("sellList", "multiselect", MyData.sellindexes),
            },
        "strat_manage_index":
            {
                "title_strategy": "active",
                "nav_index_manage": "active",
            },
        "strat_shop":
            {
                "title_strategy": "active",
                "nav_strat_shop": "active",
            },
        "about_us":
            {
                "title_aboutUs": "active",
                "no_navBar": True,
            },
        "under_construction":
            {
                "no_navBar": True,
            }
    }
    return context_mapping[pageName]

