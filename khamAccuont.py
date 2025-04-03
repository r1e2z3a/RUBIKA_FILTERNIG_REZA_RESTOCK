from arsein import Robot_Rubika
from time import sleep
from os import system
from random import choice
import os
import rainbowtext,pyfiglet
os.system("clear")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
green = '\033[32m' 
red = '\033[31m' 
green = '\033[32m' 
blue = '\033[36m' 
pink = '\033[35m' 
yellow = '\033[93m' 
darkblue = '\033[34m' 
white = '\033[00m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'
from time import sleep
def printlow(Str):

    for char in Str:

        print(char, end='', flush=True)

        sleep(.01)
print(rainbowtext.text(pyfiglet.figlet_format("Beni bot")))
printlow(g+"_"*64)
printlow (f"""
{red}└──>{blue}Beni
{red}└─────>>{g}@haiulla
{red}└─────────>>>{yw}https://rubika.ir/joinc/BHIFIHCG0NOFPOHEGKQDMZKIAZGIHFGC
""")
printlow(g+"_"*64)

bot = Robot_Rubika(input(f"""
{pink}Enter your auth :{yellow}"""))
os.system("clear")
print(rainbowtext.text(pyfiglet.figlet_format("Beni bot")))
printlow(g+"_"*64)
printlow (f"""
{red}└──>{blue}Beni
{red}└─────>>{g}@haiulla
{red}└─────────>>>{yw}https://rubika.ir/joinc/BHIFIHCG0NOFPOHEGKQDMZKIAZGIHFGC
""")
printlow(g+"_"*64)
deleted = []

while 1:
	try:
		while 1:
			try:
				message = choice([bot.getChatsUpdate(),bot.getMessagesChats(),bot.getChats()])
				break
			except:
				continue
		for msg in message:
			if 'object_guid' in msg.keys():
				if msg['abs_object']['type'] == 'Group' and not msg['object_guid'] in deleted:
					guidgap = msg['object_guid']
					namegap = msg['abs_object']['title']
					bot.leaveGroup(guidgap)
					print(f"{yellow}leave in group:{w} {namegap}")
					deleted.append(guidgap)
				elif msg['abs_object']['type'] == 'Channel' and not msg['object_guid'] in deleted:
					guidChannel = msg['object_guid']
					nameChannel = msg['abs_object']['title']
					bot.LeaveChannel(guidChannel)
					print(f"{pink}leave in channel:{w} {nameChannel}")
					deleted.append(guidChannel)
	except:
					     continue 
