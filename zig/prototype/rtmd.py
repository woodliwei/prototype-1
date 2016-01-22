# -*- coding:utf-8 -*-
import json


# bb[0]:股票名  bb[1]:今日开盘价    bb[2]：昨日收盘价    bb[3]:当前价格   bb[4]:今日最高价    bb[5]:今日最低价
# bb[6]:买一报价 bb[7]:卖一报价     bb[8]:成交股票数(股）bb[9]:成交金额元 bb[10]:买一申请股数 bb[11]:买一报价
# bb[12]:买二股数 bb[13]:买二报价   bb[14]:买三股数      bb[15]:买三报价  bb[16]:买四申请股数 bb[17]:买四报价
# bb[18]:买五股数 bb[19]:买五报价   bb[20]:卖一股数      bb[21]:卖一报价  bb[22]:卖二申请股数 bb[23]:卖二报价
# bb[24]:卖三股数 bb[25]:卖三报价   bb[26]:卖四股数      bb[27]:卖四报价  bb[28]:卖五股数     bb[29]:卖五报价
# bb[30]:日期     bb[31]:时间       bb[32]:unknown
class SinaRTMD:
    __mapping = {
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

    def __init__(self, sinaStrings):
        strings = sinaStrings.split("\n")
        self.data = []
        for sinaString in strings:
            if len(sinaString) > 30:
                self.data.append(SinaRTMD.createRTMDData(sinaString))


    @staticmethod
    def createRTMDData(sinaString):
        data = {}
        data_start_pos = sinaString.find("\"")
        # format datastring remove "var hq-str_shxxxx="" part.
        dataString = sinaString[data_start_pos + 1: -2]
        # get symbol
        data["symbol"] = dataString[data_start_pos - 9: data_start_pos - 1]
        return SinaRTMD.__parseString(data, dataString)

    @staticmethod
    def __parseString(data, dataString):
        splittedStr = dataString.split(',')
        for i in range(len(splittedStr)):
            if i in SinaRTMD.__mapping:
                # encoding error here if convert string as default encoding is ascii
                if SinaRTMD.__mapping[i][2] != str:
                    value = SinaRTMD.__mapping[i][2](splittedStr[i])
                else:
                    value = splittedStr[i]
                data[SinaRTMD.__mapping[i][0]] = value
        return data

# To json refer http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html
    def toJsonString(self):
        return json.dumps(self.data, ensure_ascii=False)

