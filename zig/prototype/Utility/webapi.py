# -*- coding:utf-8 -*-

import urllib2
import re

def getSinaApiResult(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    dataJsonStr = response.read()
    dataJsonStrUni = dataJsonStr.decode("GBK")
    result = addDoubleQuote(dataJsonStrUni)
    return result


def addDoubleQuote(jsonString):
    return re.sub(u'([A-Za-z]\w+)\:', addDoubleQuoteInRe, jsonString)


def addDoubleQuoteInRe(match):
    value = match.group(1)
    return '"' + value + '"' + ':'


# bb[0]:股票名  bb[1]:今日开盘价    bb[2]：昨日收盘价    bb[3]:当前价格   bb[4]:今日最高价    bb[5]:今日最低价
# bb[6]:买一报价 bb[7]:卖一报价     bb[8]:成交股票数(股）bb[9]:成交金额元 bb[10]:买一申请股数 bb[11]:买一报价
# bb[12]:买二股数 bb[13]:买二报价   bb[14]:买三股数      bb[15]:买三报价  bb[16]:买四申请股数 bb[17]:买四报价
# bb[18]:买五股数 bb[19]:买五报价   bb[20]:卖一股数      bb[21]:卖一报价  bb[22]:卖二申请股数 bb[23]:卖二报价
# bb[24]:卖三股数 bb[25]:卖三报价   bb[26]:卖四股数      bb[27]:卖四报价  bb[28]:卖五股数     bb[29]:卖五报价
# bb[30]:日期     bb[31]:时间       bb[32]:unknown

# 查询大盘指数
# 查询大盘指数，比如查询上证综合指数（000001）：
# http://hq.sinajs.cn/list=s_sh000001
# 服务器返回的数据为：
# var hq_str_s_sh000001="上证指数,3094.668,-128.073,-3.97,436653,5458126";
# 数据含义分别为：指数名称，当前点数，当前价格，涨跌率，成交量（手），成交额（万元）；

#sample var hq_str_sh600000="浦发银行,17.220,17.250,16.580,17.460,16.500,16.520,16.560,34197115,582845476.000,1000,16.520,19213,16.510,35492,16.500,5700,16.490,4800,16.480,3200,16.560,45300,16.600,102100,16.630,136346,16.640,27100,16.650,2016-01-21,15:00:00,00";
#       var hq_str_sh600004="白云机场,12.320,12.450,12.200,12.510,12.010,12.200,12.250,5320053,65624470.000,39500,12.200,1800,12.050,200,12.040,2000,12.030,9400,12.020,27349,12.250,900,12.260,14600,12.270,10900,12.280,83800,12.290,2016-01-21,15:00:00,00";

#  ***********  performance   *********
# 2016-01-17 21:25:27.925000 getting rtmd from web api: sz300497
# 2016-01-17 21:25:27.959000 getting rtmd from web api done (34mm)

# todo add more check here. 1. must start with alphabet. Only contain [a-zA-Z][0-9]
def getDetailedRtmd(stocks):
    url = 'http://hq.sinajs.cn/list=' + stocks
    return getSinaApiResult(url)


# *** Money Flow Sample Data  ***
# [{
# symbol:"sz000933"
# name:"神火股份",
# cnt_r0x_ratio:"9",
# trade:"5.5800",
# changeratio:"0.268182",
# turnover:"6699.8",
# amount:"6743352176.0000",
# netamount:"1339718102.1900",
# ratioamount:"0.198672",
# r0_net:"844973272.7100",
# r0x_ratio:"0.721736"}]
def getAllMoneyFlowInfo():
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_bkzj_lxjlr?num=10000'
    return getSinaApiResult(url)


def getAllProdInfo():
    return getAllMoneyFlowInfo()
