
from __future__ import unicode_literals
from django.shortcuts import render_to_response
import json
from .models import MyData
from .controls import *

# Create your views here.
from django.http import HttpResponse

def hello1(request, num):
    try:
        num = int(num)
    except ValueError:
        raise Http404()


def bigdata_trend_testing(requst):
    return render_to_response("bigdata_trend_testing.html", get_context("bigdata_trend_testing"))


def bigdata_trend_test_result(request):
    return render_to_response('bigdata_trend_test_result.html', get_context("bigdata_trend_test_result"))


def strat_trend_manage(requst):
    return render_to_response("strat_trend_manage.html", get_context("strat_trend_manage"))


def about_us(requst):
    return render_to_response("about_us.html", get_context("about_us"))

# def defaultViews(request):
#     return render_to_response(
#         'group.html',
#         dict(
#             {
#                 "SHIndexName": json.dumps("上证指数"),
#                 "dateList": json.dumps(MyData.dateList),
#                 "marketData": json.dumps(MyData.marketData)
#             },
#
#         )
#     )

#dict(dict1, **dict2)

# Set active items in Title Bar and Nav Bar
# {"title_strategy": "active",
#   "title_bigdata": "",
#   "about": "",
#   "nav_trendTest": "active",
#   "nav_historyData": "",
#   "nav_historyTest": ""}
def get_context(pageName):
    activeDict= {
        "bigdata_trend_testing":
            {
                "title_bigdata": "active",
                "nav_trendTest": "active",
                "buy_indexes_list": SelectDropdown("buyList", "multiselect", MyData.buyindexes),
                "sell_indexes_list": SelectDropdown("sellList", "multiselect", MyData.sellindexes),
            },
        "strat_trend_manage":
            {
                "title_strategy": "active",
                "nav_index_manage": "active",
            },
        "bigdata_trend_test_result":
            {
                "title_bigdata": "active",
                "nav_historyTest": "active",
                "SHIndexName": json.dumps("上证指数"),
                "dateList": json.dumps(MyData.dateList),
                "marketData": json.dumps(MyData.marketData),
            },
        "about_us":
            {
                "title_aboutUs": "active",
                "no_navBar": True,
            }
    }
    return activeDict[pageName]
