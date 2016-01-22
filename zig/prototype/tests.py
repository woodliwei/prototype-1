from django.test import TestCase
# Create your tests here.

from Utility.webapi import *
from rtmd import *

sinaStrings = getDetailedRtmd("sh600000,sh600004")
rtmd = SinaJsRTMD(sinaStrings)
