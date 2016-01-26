# -*- coding:utf-8 -*-

import json
from Utility import Utils
from .models import *


class ProductHelper:

    @staticmethod
    def __getAllStocks(dataprovider):
        result = dataprovider.getAllStockProdInfo()
        stocks = json.loads(result)
        return stocks

    @staticmethod
    def __getAllFunds(dataprovider):
        result = dataprovider.getAllFundProdInfo()
        funds = json.loads(result)
        return funds

#    ***********     refresh product performance test result     ***********
# 2016-01-25 22:49:49.581000 Start refreshing product DB...
# 2016-01-25 22:49:49.583000 Deleting product DB...
# 2016-01-25 22:49:49.676000 Start query product info...
# 2016-01-25 22:49:50.804000 Done.
# 2016-01-25 22:49:51.130000 Saved to DB.
    @staticmethod
    def refresh_productDB(dataprovider):
        Utils.log("Start refreshing product DB...")

        Utils.log("Deleting product DB...")
        ProductInfo.objects.all().delete()

        Utils.log("Start query product info...")
        stocks = ProductHelper.__getAllStocks(dataprovider)
        funds = ProductHelper.__getAllFunds(dataprovider)

        Utils.log("Saving to DB....")
        products = []
        # insert product info
        for stock in stocks:
            product = ProductInfo(symbol=stock["symbol"], cn_name=stock["name"], issue_type="stock")
            products.append(product)
        for fund in funds:
            product = ProductInfo(symbol=fund["symbol"], cn_name=fund["name"], issue_type="fund")
            products.append(product)
        ProductInfo.objects.bulk_create(products)
        Utils.log("Done.")

        message = "Fetching stock info done:" + str(len(products))
        return message

