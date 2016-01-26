# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render_to_response
from .controls import *
from .product import *
from Utility import webapi
from rtmd import *
from django.http import HttpResponse


def bigdata_trend_testing(requst):
    return render_to_response("bigdata_trend_testing.html", get_context("bigdata_trend_testing"))


def bigdata_trend_test_result(request):
    return render_to_response('bigdata_trend_test_result.html', get_context("bigdata_trend_test_result"))


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
    if request.GET.get('ty') == 'rtmd':
        products = request.GET.get('value')
        if products is not None:
            result = SinaRTMD(webapi.getDetailedRtmd(products)).toJsonString()
    response = HttpResponse(result)
    # set no cache in repsonse header
    response['Cache-Control'] = 'no-cache'
    return response


def about_us(requst):
    return render_to_response("about_us.html", get_context("about_us"))


def under_construction(requst):
    return render_to_response("under_construction.html", get_context("under_construction"))


def local_test(requst):
    return render_to_response("bigdata_trend_test_result_dynamic.html", get_context("test_sample"))


# Set active items in Title Bar and Nav Bar
def get_context(pageName):
    context_mapping = {
        "bigdata_trend_test_result_dynamic":
            {
                "title_bigdata": "active",
                "nav_historyTest": "active",
                "StockName": json.dumps("600001.ss"),
                "dateList": json.dumps(MyData.dateList),
                "marketData": json.dumps(MyData.marketData),
                "resultList": json.dumps(MyData.resultList),
                "startDate": json.dumps(MyData.startDate),
                "endDate": json.dumps(MyData.endDate),
            },
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
                "avg_5_10": json.dumps(MyData.avg_5_10),
                "gain_5_10": json.dumps(MyData.gain_5_10),
                "avg_5_50": json.dumps(MyData.avg_5_50),
                "gain_5_50": json.dumps(MyData.gain_5_50),
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
            },
        "test_sample":
            {
                "title_bigdata": "active",
                "nav_historyTest": "active",
                "StockName": json.dumps("600001.ss"),
                "categories": json.dumps(MyData.dateList2),
                "vals": json.dumps(MyData.marketData2),
                "avg_5_10": json.dumps(MyData.avg_5_10),
                "resultList": json.dumps(MyData.resultList),
                "startDate": json.dumps(MyData.startDate),
                "endDate": json.dumps(MyData.endDate),
            }
    }
    return context_mapping[pageName]

