#! /usr/bin/env python
#coding=utf-8
#code: youstar
#data:20120417
import codecs,sys
from optparse import OptionParser

#split value to list
def SetValue(line,iname,ilist):
    if line[0] == iname:
        for ii in line[1].split(";"):
            ilist.append(ii)
                
#read information from txt 
def ReadInfo(filename):
    global name,idcard,qq,weakpw,subpw,nickname,year,domain,phone
    #utf-8 need codecs
    try:
        hfile = codecs.open(filename,'r','utf-8')
        for lines in hfile.readlines():
            lines = lines.strip()
            line = lines.split(":")
            SetValue(line,'name',name)
            SetValue(line,'idcard',idcard)
            SetValue(line,'qq',qq)
            SetValue(line,'weakpw',weakpw)
            SetValue(line,'subpw',subpw)
            SetValue(line,'nickname',nickname)
            SetValue(line,'year',year)
            SetValue(line,'domain',domain)
            SetValue(line,'phone',phone)
            
        hfile.close()
    except:
        print 'read information error'

#deal idcard
def dealidcard():
    global idcard,tempid
    if len(idcard[0]) == 18:
        try:
            tempid = ''
            for i in range(5,13):
                tempid = tempid + idcard[0][i]
            idcard[0] = tempid
            ## month <10 delete 0
            if idcard[0][4]=='0' and idcard[0][6]=='0':
                tempid = ''
                for i in range(0,4):
                    tempid = tempid + idcard[0][i]
                tempid = tempid + idcard[0][5]+idcard[0][7]
                idcard.append(tempid)
        except:
            print 'deal idcard error'

#rules
def namerule():
    global name,passwd,idcard
    for iname in name:
        passwd.append(iname.replace(' ',''))  
def cardrule():
    global idcard,passwd
    for iid in idcard:
        passwd.append(iid)
        if len(name)>0:
            for iname in name:
                passwd.append(iname.replace(' ','')+iid)
                passwd.append(iid+iname.replace(' ',''))
                fname = iname.split(' ')
                passwd.append(iid+fname[0][0]+fname[1][0])
                passwd.append(fname[0][0]+fname[1][0]+iid)
def phonerule():
    global phone,passwd,name
    for iphone in phone:
        passwd.append(iphone)
        if len(name)>0:
            for iname in name:
                passwd.append(iname.replace(' ','')+iphone)
                passwd.append(iphone+iname.replace(' ',''))
                fname = iname.split(' ')
                passwd.append(iphone+fname[0][0]+fname[1][0])
                passwd.append(fname[0][0]+fname[1][0]+iphone)            
def qqrule():
    global qq,name,subpw,passwd
    for iqq in qq:
        passwd.append(iqq)
        if len(name)>0:
            for iname in name:
                passwd.append(iname.replace(' ','')+iqq)
                passwd.append(iqq+iname.replace(' ',''))
                fname = iname.split(' ')
                passwd.append(iqq+fname[0][0]+fname[1][0])
                passwd.append(fname[0][0]+fname[1][0]+iqq)
        if len(subpw)>0:
            for isubpw in subpw:
                passwd.append(isubpw+iqq)
                passwd.append(iqq+isubpw)
def weakpws():
    global weakpw,passwd
    for iwpw in weakpw:
        passwd.append(iwpw)
def yearrules():
    global year,name,subpw
    for iyear in year:
        passwd.append(iyear)
        if len(name)>0:
            for iname in name:
                passwd.append(iname.replace(' ','')+iyear)
                passwd.append(iyear+iname.replace(' ',''))
                fname = iname.split(' ')
                passwd.append(iyear+fname[0][0]+fname[1][0])
                passwd.append(fname[0][0]+fname[1][0]+iyear)
def domainrules():
    global domain,subpw
    for idom in domain:
        passwd.append(idom)
        if len(subpw)>0:
            for isubpw in subpw:
                passwd.append(idom + isubpw)
                passwd.append(isubpw + idom)              
def nicknamerules():
    global nickname,year
    for inick in nickname:
        passwd.append(inick)
        if len(year)>0:
            for iyear in year:
                passwd.append(inick+iyear)
                passwd.append(iyear+inick)
#make rules
def makeruls():
    global name,idcard,qq,weakpw,subpw,nickname,year
    if len(name)>0:
        namerule()
    if len(idcard)>0:
        cardrule()
    if len(year)>0:
        yearrules()
    if len(domain)>0:
        domainrules()
    if len(nickname)>0:
        nicknamerules()
    if len(phone)>0:
        phonerule()
    if len(qq)>0:
        qqrule()
    if len(weakpw)>0:
        weakpws()

#genarate file
def Genaratefile(filename):
    global passwd,strpw
    strpw = u''
    for ipw in passwd:
        strpw = strpw + ipw +u'\r\n'
    try:
        file = codecs.open(filename, "w", "utf-8")
        file.write(strpw)
        file.close()
    except:
        print 'write file failed'

#show help
def sdgthelp():
    print "\n|---------------------------------------------------------------|"
    print "|      youstar[@]foxmail[dot]com  v1.0                          |"
    print "|      4/2012      sdgt.py                                      |"
    print "|      --social dic generate tool--                             |"
    print "| Usage:    sdgt.py  'info file path'  'dic file path'          |"
    print "| Example:  sdgt.py  C:\zhang.txt C:\zhangdic.txt               |"
    print "|---------------------------------------------------------------|\n"
    sys.exit(1)    
    
if __name__=='__main__':
    name=[];idcard=[];qq=[];weakpw=[];subpw=[];nickname=[];year=[];passwd=[];domain=[];phone=[]
    if len(sys.argv) != 3:
        sdgthelp()
    else:
        try:
            ReadInfo(sys.argv[1])
            #deal some data
            dealidcard()
            #make rule
            makeruls()
            #generate passwd
            Genaratefile(sys.argv[2])
            print 'generate success'
        except:
            print 'generate failed'