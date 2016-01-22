import sys
import datetime


def printChinese(list):
    print "".join(i for i in list)


def log(msg):
    print >>sys.stderr, datetime.datetime.now(), msg