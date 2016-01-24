# -*- coding:utf-8 -*-

import json
from Utility import Utils
from .models import *


class ProductHelper:

    @staticmethod
    def __getAllStocks(dataprovider):
        result = dataprovider.getAllProdInfo()
        stocks = json.loads(result)
        return stocks

#    ***********     refresh product performance test result     ***********
# 2016-01-17 13:57:09.623000 Deleting product DB... (deleting 70mm)
# 2016-01-17 13:57:09.692000 Start query product info... (query web api 1,017mm)
# 2016-01-17 13:57:10.709000 Done. (insert 211mm)
# 2016-01-17 13:57:10.920000 fetching stock info done:2817
    @staticmethod
    def refresh_productDB(dataprovider):
        Utils.log("Start refreshing product DB...")
        Utils.log("Deleting product DB...")
        ProductInfo.objects.all().delete()
        Utils.log("Start query product info...")
        stocks = ProductHelper.__getAllStocks(dataprovider)
        Utils.log("Done. \r\nSaving to DB...")
        products = []
        for stock in stocks:
            product = ProductInfo(symbol=stock["symbol"], cn_name=stock["name"])
            products.append(product)
        ProductInfo.objects.bulk_create(products)
        message = "Fetching stock info done:" + str(len(stocks))
        return message

