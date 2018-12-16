from django.test import TestCase
from bs4 import BeautifulSoup
from urllib.request import urlopen

def getNum():
    html=urlopen("https://www.dhlottery.co.kr/gameResult.do?method=statByNumber")
    bsObj=BeautifulSoup(html)
    ret={}
    i=1
    for item in bsObj.findAll("td",{"class":"graph"}):
        ret.update({i:[i]*int(item.next_sibling.next_sibling.get_text())})
        i+=1
    return ret
