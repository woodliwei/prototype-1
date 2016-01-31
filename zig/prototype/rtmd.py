# -*- coding:utf-8 -*-
import json
from product import ProductType


class SinaStringType:
    unknown = -1
    # stock_sh = 0
    # stock_sz = 1
    fund_f = 2
    fund_fu = 3
    index = 4
    stock = 5


class SinaStringParser:
    __stockMapping = {
        0: ["cn_name", "股票名", str],
        1: ["op", "今日开盘价", float],
        2: ["lccp", "昨日收盘价", float],
        3: ["cp", "当前价格", float],
        4: ["hp", "今日最高价", float],
        5: ["lp", "今日最低价", float],
        6: ["ap", "买一报价", float],
        7: ["bp", "卖一报价", float],
        8: ["vs", "成交股票数", int],
        9: ["to", "成交金额", float],
        10: ["bas", "买一股数", int],
        11: ["bap", "买一报价", float],
        12: ["bas2", "买二股数", int],
        13: ["bap2", "买二报价", float],
        14: ["bas3", "买三股数", int],
        15: ["bap3", "买三报价", float],
        16: ["bas4", "买四股数", int],
        17: ["bap4", "买四报价", float],
        18: ["bas5", "买五股数", int],
        19: ["bap5", "买五报价", float],
        20: ["bbs", "卖一股数", int],
        21: ["bbp", "卖一报价", float],
        22: ["bbs2", "卖二股数", int],
        23: ["bbp2", "卖二报价", float],
        24: ["bbs3", "卖三股数", int],
        25: ["bbp3", "卖三报价", float],
        26: ["bbs4", "卖四股数", int],
        27: ["bbp4", "卖四报价", float],
        28: ["bbs5", "卖五股数", int],
        29: ["bbp5", "卖五报价", float],
        30: ["date", "日期", str],  #todo consider to change to date type
        31: ["time", "时间", str],  #todo consider to change to time type
        }

    # var hq_str_sh600000="
    # var hq_str_f_370027="
    # var hq_str_s_sh000001="
    # var hq_str_fu_370027="
    @staticmethod
    def getSinaStringType(sinaString):
        if sinaString.startswith("var hq_str_sh") or sinaString.startswith("var hq_str_sz"):
            return SinaStringType.stock
        if sinaString.startswith("var hq_str_s_"):
            return SinaStringType.index
        if sinaString.startswith("var hq_str_f_"):
            return SinaStringType.fund_f
        if sinaString.startswith("var hq_str_fu_"):
            return SinaStringType.fund_fu

    @staticmethod
    def getSinaStringMapping(sinaStringType):
        if sinaStringType == SinaStringType.stock:
            return SinaStringParser.__stockMapping
        return None


class SinaRTMD:

    def __init__(self, sinaStrings, useMapping = True):
        strings = sinaStrings.split("\n")
        self.data = []
        for sinaString in strings:
            if len(sinaString) > 30:
                self.data.append(SinaRTMD.createRTMDData(sinaString, useMapping))

    @staticmethod
    def createRTMDData(sinaString, useMapping):
        data = {}
        mapping = None

        data_start_pos = sinaString.find("\"")
        # format datastring remove "var hq-str_shxxxx="" part.
        dataString = sinaString[data_start_pos + 1: -2]
        # get symbol
        data["symbol"] = sinaString[11: data_start_pos - 1]

        if useMapping:
            dataType = SinaStringParser.getSinaStringType(sinaString)
            mapping = SinaStringParser.getSinaStringMapping(dataType)
        return SinaRTMD.__parseString(data, dataString, mapping)

    @staticmethod
    def __parseString(data, dataString, mapping):
        splittedStr = dataString.split(',')
        for i in range(len(splittedStr)):
            if mapping is not None and i in mapping:
                # encoding error here if convert string as default encoding is ascii
                if mapping[i][2] is not None and mapping[i][2] != str:
                    value = mapping[i][2](splittedStr[i])
                else:
                    value = splittedStr[i]
                data[mapping[i][0]] = value
            else:
                value = splittedStr[i]
                data[i] = value
        return data

    # Tojson refer http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html
    def toJsonString(self):
        return json.dumps(self.data, ensure_ascii=False)

