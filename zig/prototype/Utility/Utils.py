import sys
import datetime


def printChinese(list):
    print "".join(i for i in list)


def log(msg):
    msg = str(datetime.datetime.now()).rstrip("0") + "	" + msg
    print >>sys.stderr, msg
    return msg
