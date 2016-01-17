
# -*- coding:utf-8 -*-
#bb[0]:股票名  bb[1]:今日开盘价    bb[2]：昨日收盘价    bb[3]:当前价格   bb[4]:今日最高价    bb[5]:今日最低价
#bb[6]:买一报价 bb[7]:卖一报价     bb[8]:成交股票数(股）bb[9]:成交金额元 bb[10]:买一申请股数 bb[11]:买一报价
#bb[12]:买二股数 bb[13]:买二报价   bb[14]:买三股数      bb[15]:买三报价  bb[16]:买四申请股数 bb[17]:买四报价
#bb[18]:买五股数 bb[19]:买五报价   bb[20]:卖一股数      bb[21]:卖一报价  bb[22]:卖二申请股数 bb[23]:卖二报价
#bb[24]:卖三股数 bb[25]:卖三报价   bb[26]:卖四股数      bb[27]:卖四报价  bb[28]:卖五股数     bb[29]:卖五报价
#bb[30]:日期     bb[31]:时间       bb[32]:unknown

#查询大盘指数
#查询大盘指数，比如查询上证综合指数（000001）：
#http://hq.sinajs.cn/list=s_sh000001
#服务器返回的数据为：
#var hq_str_s_sh000001="上证指数,3094.668,-128.073,-3.97,436653,5458126";
#数据含义分别为：指数名称，当前点数，当前价格，涨跌率，成交量（手），成交额（万元）；


import urllib
import urllib2
import json
import re

class ProductPicker:
    floattype = (1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)
    inttype = (8,) #consicer 10,12,14,16,18,20,22,24,26,28
    stringtype = (0,)
    daytype = (30,)
    timetype = (31,)

    def __init__(self, stocklist):
        if len(stocklist) == 0:
            raise Exception("Stock list can't be empty")
        self.url = 'http://hq.sinajs.cn/list=' + stocklist
        self.data = {}

    def getData(self):
       contents = urllib.urlopen(self.url).read()
       for content in str(contents).splitlines():
           temp = content.split(",")
           symbol = temp[0][11:19]
           self.data[symbol] = self.generate_stock_data(temp)
       return self.data

    @staticmethod
    def generate_stock_data(splitteddata):
        if len(splitteddata) <= 1:
            return None
        #trim first char and leave cn name only
        splitteddata[0] = splitteddata[0][splitteddata[0].find('"') +1:]
        return splitteddata

    @staticmethod
    def addDoubleQuote(match):
        value = match.group(1)
        return '"' + value + '"' + ':'

    @staticmethod
    def getAllStocks():
        url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_bkzj_lxjlr?num=10000&sort=cnt_r0x_ratio&asc=0&bankuai='
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        dataJsonStr = response.read()   #replace("\x95N", "\xc9\xfd")
        dataJsonStrUni = dataJsonStr.decode("GBK")
        result = re.sub(u'(\w+)\:', ProductPicker.addDoubleQuote, dataJsonStrUni)
        stocks = json.loads(result)
        return stocks