# -*- coding: UTF-8 -*-

first = ["bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
second = ["on","yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
third = ["yüz", "bin", "milyon", "milyar", "trilyon", "katrilyon"] # katrilyonun devamını ekleyerek devam edebilirsin.

def numberToMoney(value) :
    if value <= 0.0 :
        return ("0",0)
    valueList = value.split(".")
    if len(valueList) == 0:
        valueText = value
        centValue = 0
    else:
        valueText = valueList[0]
        centValue = int(valueList[1])

	return ("%s" % ('.'.join([ i-3<0 and valueText[:i] or valueText[i-3:i] for i in range(len(valueText)%3, len(valueText)+1, 3) if i ])),centValue)

def compareMoney(value, index, listLen):
    realText =""
    valueText = value
    value = long(value)
    if value == 0:
        return realText
    elif value <= 9:
        realText+=first[value-1]
    elif value <= 99:
        if long(valueText[0]) != 0:
            realText+=second[long(valueText[0])-1]
            if len(valueText) > 1:
    			if long(valueText[1]) != 0:
    				if (value%10) != 0:
    					realText+=first[long(valueText[1])-1]
        else:
			if len(valueText) == 3:
				if long(valueText[1]) != 0:
					realText+=second[long(valueText[1])-1]
					exValue = long(valueText[1:])
					if (exValue%10) != 0:
						realText+=first[long(valueText[2])-1]
				else:
					if long(valueText[2]) != 0:
						realText+=first[long(valueText[2])-1]
			else:
				if long(valueText[1]) != 0:
					realText+=first[long(valueText[1])-1]
    elif value <= 999:
		if long(valueText[0]) != 0:
			realText+=first[long(valueText[0])-1]
			realText+=third[0]
			if realText == "biryüz":
				realText = "yüz"
		if long(valueText[1]) != 0:
			realText+=second[long(valueText[1])-1]
			exValue = long(valueText[1:])
			if (exValue%10) != 0:
				realText+=first[long(valueText[2])-1]
		else:
			if long(valueText[2]) != 0:
				realText+=first[long(valueText[2])-1]
	
    if listLen > 0:
		getIndex = listLen-1-index
		#print "index %d j %d"%(getIndex,index)
		if getIndex > 0:
			realText+=third[getIndex]
    realText+=" "

    return realText

def valueToText(value):
    price = str(value)
    realText = ""
    (priceText, centText) = numberToMoney(price)
    priceList = priceText.split(".")
    print "%s,%d"%(priceText,centText)
    for index in xrange(len(priceList)):
    	realText+=compareMoney(priceList[index],index,len(priceList))
    if price > 0:
    	realText+="TL"
    
    if centText > 0:
    	realText+=" "
    	realText+=compareMoney(str(centText),0,0)
    	realText+="Kuruş"
    return realText

print valueToText("999436854424135221.13")
print "\n"
print "Ürün Fiyatı: %s"%valueToText("199.99")

