# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
import json
from .models import MyData
from .models import Mysite
from .controls import *

def hello1(request, num):
    try:
        num = int(num)
    except ValueError:
        raise Http404()


def bigdata_trend_testing(requst):
    return render_to_response("bigdata_trend_testing.html", get_context("bigdata_trend_testing"))


def bigdata_trend_test_result(request):
    return render_to_response('bigdata_trend_test_result.html', get_context("bigdata_trend_test_result"))


def bigdata_trend_test_result_dynamic(request):
    return render_to_response('bigdata_trend_test_result_dynamic.html', get_context("bigdata_trend_test_result_dynamic"))


def bigdata_history(request):
    return render_to_response('bigdata_history.html', get_context("bigdata_history"))


def strat_trend_manage(requst):
    return render_to_response("strat_manage_index.html", get_context("strat_manage_index"))


def strat_manage(requst):
    return render_to_response("strat_manage.html", get_context("strat_manage"))


def strat_shop(requst):
    return render_to_response("strat_shop.html", get_context("strat_shop"))


def about_us(requst):
    return render_to_response("about_us.html", get_context("about_us"))


def under_construction(requst):
    return render_to_response("under_construction.html", get_context("under_construction"))

def local_test(requst):
    #testDBAction()
    return render_to_response("bigdata_trend_test_result_dynamic.html", get_context("test_sample"))
    #return HttpResponse("bigdata_trend_test_result_hc.html")


def testDBAction():
    # Add
     s = Mysite(title='test_Title', url='http://testURL', author='guoqingc', num='0')
     s.save()

    # Search and Update
    # s = Mysite.objects.get(title='test_Title')
    # s.url = 'http://testURL2'
    # s.save()

    # Delete
    # s = Mysite.objects.get(title='test_Title')
    # s.delete()

    # Delete All
    # Mysite.objects.all().delete()



# Set active items in Title Bar and Nav Bar
#   "title_strategy": "active",
#   "title_bigdata": "",
#   "title_aboutUs": "",
#   "nav_trendTest": "active",
#   "nav_historyData": "",
#   "nav_historyTest": ""
def get_context(pageName):
    activeDict= {
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
        "bigdata_history":
            {
                "title_bigdata": "active",
                "nav_historyData": "active",
                "SHIndexName": json.dumps("上证指数"),
                "dateList": json.dumps(MyData.dateList),
                "marketData": json.dumps(MyData.marketData),
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
    return activeDict[pageName]
