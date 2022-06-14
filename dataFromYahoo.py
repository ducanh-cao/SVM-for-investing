import urllib.request
import os
import time

path = "C:/Users/CaoDucAnh/Desktop/myProject/svmForInvesting/intraQuarter"

def Check_Yahoo():
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    i = 0

    for e in stock_list[1:]:
        try:
            e = e.replace("C:/Users/CaoDucAnh/Desktop/myProject/svmForInvesting/intraQuarter/_KeyStats\\","")
            link = "http://finance.yahoo.com/q/ks?s="+e.upper()+"+Key+Statistics"
            resp = urllib.request.urlopen(link).read()

            save = "forward/"+str(e)+".html"
            store = open(save,"w")
            store.write(str(resp))
            store.close()
            i = i + 1
            print("Done", i)

        except Exception as e:
            print(str(e))
            time.sleep(1)


Check_Yahoo()   