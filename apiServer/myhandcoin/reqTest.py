#-*- coding: utf-8 -*-

#!/usr/bin/python

#한인택이 만든 코인,리플 가격정보 긁개 버전 V0.00.001

#https://www.samchully.co.kr/customer/gas/inquiry/check.do

#http://rmtr.samchully.co.kr/Main/LogIn_ext.do

#https://www.korbit.co.kr/

#https://www.bitstamp.net/api/ticker/

#https://api.korbit.co.kr/v1/ticker?currency_pair=xrp_krw"

import urllib2

import json

import datetime

import sys

# import mysql.connector

#

# cnx = mysql.connector.connect(user='scott', password='tiger',

#                               host='127.0.0.1',

#                               database='employees')

# cnx.close()


print("코인,리플 가격정보 긁개 버전 V0.00.001")

#resp = urllib2.urlopen("https://www.samchully.co.kr/customer/gas/inquiry/check.do").read()

#resp = urllib2.urlopen("http://rmtr.samchully.co.kr/Main/LogIn_ext.do").read()

#resp = urllib2.urlopen("https://www.korbit.co.kr/")

respBTC = urllib2.urlopen("https://www.bitstamp.net/api/ticker/").read()

respXRP = urllib2.urlopen("https://www.bitstamp.net/api/v2/ticker/xrpbtc/").read()

respXRPBITTHUM = urllib2.urlopen("https://api.bithumb.com/public/ticker/XRP").read()

respBTG = urllib2.urlopen("https://api.bithumb.com/public/ticker/BTG").read()

respBCH = urllib2.urlopen("https://api.bithumb.com/public/ticker/BCH").read()

#print("BTC : "+respBTC)

#print("XRP : "+respXRP)

btcDic = json.loads(respBTC.replace(" ",""))

xrpDic = json.loads(respXRP.replace(" ",""))

btgDic = json.loads(respBTG.replace(" ",""))

bchDic = json.loads(respBCH.replace(" ",""))

bitthumDic = json.loads(respXRPBITTHUM.replace(" ",""))


i = datetime.datetime.now()

print ("Current date & time = %s" % i)


print("BTC Last :$"+btcDic["last"]+"  XRP Last :$"+xrpDic["last"])

#print("빗썸-리플 응답>>>>> $"+respXRPBITTHUM)

# print("bitthumDic Last>>>>> "+bitthumDic["buy_price"])

btcLast = float(btcDic["last"])

xrpLast = float(xrpDic["last"])

bitthumLast = float(bitthumDic["data"]["buy_price"])

bitthumUnitTrade = float(bitthumDic["data"]["units_traded"])

btgLast = float(btgDic["data"]["buy_price"])

btgUnitTrade = float(btgDic["data"]["units_traded"])

bchLast = float(bchDic["data"]["buy_price"])

bchUnitTrade = float(bchDic["data"]["units_traded"])


krwXRP = btcLast * xrpLast * 1100

krwBitXRP = btcLast * xrpLast * 1100


btcAddComma = format(btcLast,",f")

addComma = format(krwXRP,",f")

addComma2 = format(bitthumLast,",f")

addComma3 = format(bitthumUnitTrade,",f")

btgAddComma = format(btgLast,",f")

bchAddComma = format(bchLast,",f")

print("XRP :"+addComma +"원, 빗썸:"+addComma2+"원")

print("XRP 거래량 BITTHUM >>>>> "+addComma3+" 개")

print("BTG >>>>> "+btgAddComma+" 개")

print("BCH >>>>> "+bchAddComma+" 개")


myAVG=4705

check=bitthumLast-myAVG

if check > 0:

    if check > 470:

        print("10퍼 Mode")

    else:

        print("아싸")

else:

    addComma4 = format(check,",f")

    print("헐존버모드"+addComma4+"원")


btcAddComma = btcAddComma.replace(".000000","")

addComma2 = addComma2.replace(".000000","")

bchAddComma = bchAddComma.replace(".000000","")

btgAddComma = bchAddComma.replace(".000000","")

btgAddComma = bchAddComma.replace(".000000","")


filename = datetime.datetime.now().strftime("%Y-%m-%d")+"_COIN_DATA.txt"

f = open(filename, 'a')

f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" BTC$"+btcAddComma+" BCH:"+bchAddComma+" BTG:"+btgAddComma+" XRP:"+addComma2+" XRP량:"+addComma3+"\r\n")

f.close()

#print("XRP KRW_KORBIT>>>>> "+respXRPBITTHUM)
