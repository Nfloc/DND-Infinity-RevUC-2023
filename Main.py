#Owen Haney, Atishay Jain
#Rev UC 2023
#GUIzero interface for RFID reading

from re import Match
from types import MappingProxyType
from guizero import App, Text, PushButton, TextBox, Combo, Box, Window
from rfid_module import readCharacter, writeCharacter
from time import sleep
import sys
import random

# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522



app = App(title="DND RFID",height=800)

def kill():
    app.destroy()
    

def write2(name,classs,race,xp,st,dex,con,intt,wis,cha,money,armor):
    
    #Sets up the area
    wr2=Window(app,title="DND RFID WRITE2",height=800)

    person=Box(wr2,width="fill",align="top",border=2)
    chars=Text(person,text="Character", size=15)

    stats=Box(wr2,align="top",border=2,width="fill")
    stat=Text(stats,text="Stats",size=15)

    abil=Box(wr2,align="top",border=2,width="fill")
    abili=Text(abil,text="Ability Scores",size=15)

    ski=Box(wr2,align="top",border=2,width="fill")
    skil=Text(ski,text="Skills",size=15)

    
    cn=Text(person,text=name)
    race=Text(person,text=race)
    clas=Text(person,text=classs)
    x=Text(stats, text="Xp {}".format(xp),size=10)
    abs=Text(stats, text="Armour {}".format(armor),size=10)
    abs=Text(stats, text="Money {}".format(money),size=10)

    #The Ability Score section of inputes all in Text Boxes
    abs=Text(abil, text="Strength {}".format(st),size=10)
    abs=Text(abil, text="dexterity {}".format(dex),size=10)
    abs=Text(abil, text="Constitution {}".format(con),size=10)
    abs=Text(abil, text="Intelligence {}".format(intt),size=10)
    abs=Text(abil, text="Wisdom {}".format(wis),size=10)
    abs=Text(abil, text="Charisma {}".format(cha),size=10)
    
    
    

    #Calculate modifiers
    st=int(st);dex=int(dex);con=int(con);intt=int(intt);wis=int(wis);cha=int(cha)

    Mstr = ((st-(st%2))/2)-5
    Mdex = ((dex-(dex%2))/2)-5
    Mcon = ((con-(con%2))/2)-5
    Mint = ((intt-(intt%2))/2)-5
    Mwis = ((wis-(wis%2))/2)-5
    Mcha = ((cha-(cha%2))/2)-5

    if race=="Human":
      Minv+=1
    if race=="elf":
      Mcha = Mcha +1
    if race=="orc":
      Mst = Mst +1
    if race=="Dwarf":
      Mcon+=1

    Mat = Mstr
    Mac = Mdex
    Msn  = Mdex
    Mar  = Mint
    Minv  = Mint
    Mins  = Mwis
    Mhe  = Mwis
    Mpec  = Mwis
    Mpes  = Mcha
    Mde  = Mcha
   
    if classs == "Barbarian":
      Mat = Mat*2 
      Mpec = Mpec*2
    if classs == "Knight":
      Mac = Mac*2 
      Mpes = Mpes*2
    if classs == "Wizard":
      Mar = Mat*2 
      Mhe = Mpec*2  

    abs=Text(ski, text="Atheletics {}".format(Mat),size=10)
    abs=Text(ski, text="Acrobatics {}".format(Mac),size=10)
    #IDK this abbreviation
    abs=Text(ski, text="Arcana {}".format(Mar),size=10)
    abs=Text(ski, text="Investigation {}".format(Minv),size=10)
    abs=Text(ski, text="Insight {}".format(Mins),size=10)
    #IDK this abbreviation
    abs=Text(ski, text="Perception {}".format(Mpec),size=10)
    abs=Text(ski, text="Persuasion {}".format(Mpes),size=10)
    abs=Text(ski, text="Deception {}".format(Mde),size=10)

    #Calculate level
    if int(xp)<300:
      level=2
    elif int(xp)<900:
      level=3
    elif int(xp)<2700:
      level=4
    elif int(xp)<6500:
      level=5
    elif int(xp)<14000:
      level=5
    elif int(xp)<23000:
      level=6
    elif int(xp)<34000:
      level=7
    elif int(xp)<48000:
      level=8
    elif int(xp)<64000:
      level=9
    elif int(xp)<85000:
      level=10
    elif int(xp)<100000:
      level=11
    elif int(xp)<900:
      level=12
    abs=Text(stats, text="Level {}".format(level),size=10)
    
    kille=PushButton(wr2,text="Exit",command=kill)

    #Actually write the RFID
    export=st+" "+dex+" "+con+" "+intt+" "+wis+" "+cha
    writeCharacter(export)
   
   
    






def readApp():
    
    t=readCharacter()
    var=t.split()
    re=Window(app,title="DND RFID READ",height=800)
    person=Box(re,width="fill",align="top",border=2)
    chars=Text(person,text="Character", size=15)

    stats=Box(re,align="top",border=2,width="fill")
    stat=Text(stats,text="Stats",size=15)

    abil=Box(re,align="top",border=2,width="fill")
    abili=Text(abil,text="Ability Scores",size=15)

    ski=Box(re,align="top",border=2,width="fill")
    skil=Text(ski,text="Skills",size=15)

    
    cn=Text(person,text=var[6])
    race=Text(person,text=var[7])
    clas=Text(person,text=var[8])
    x=Text(stats, text="Xp {}".format(var[9]),size=10)
    abs=Text(stats, text="Armour {}".format(var[10]),size=10)
    abs=Text(stats, text="Money {}".format(var[11]),size=10)

    #The Ability Score section of inputes all in Text Boxes
    abs=Text(abil, text="Strength {}".format(var[0]),size=10)
    abs=Text(abil, text="dexterity {}".format(var[1]),size=10)
    abs=Text(abil, text="Constitution {}".format(var[2]),size=10)
    abs=Text(abil, text="Intelligence {}".format(var[3]),size=10)
    abs=Text(abil, text="Wisdom {}".format(var[4]),size=10)
    abs=Text(abil, text="Charisma {}".format(var[5]),size=10)
    kille=PushButton(re,text="Exit",command=kill)









#Create the write
def writeApp():

    
    wr=Window(app, title="DND RFID WRITE",height=800)
    

    abs=Text(wr,text="\n\n")
    cn=TextBox(wr,text="Enter Name",width=24)
    clas=Combo(wr, options=["Select Class","Knight", "Wizard", "Barbarian"])
    race=Combo(wr, options=["Select Race","Human", "Elf", "Dwarf", "Orc"])
    xp=TextBox(wr,text="Enter XP",width=15)
    abs=Text(wr, text="\n\nAbility Scores")

    abs=Text(wr, text="STR",size=8)
    st=TextBox(wr)
    
    abs=Text(wr, text="DEX",size=8)
    dex=TextBox(wr)
    
    abs=Text(wr, text="CON",size=8)
    con=TextBox(wr)
    
    abs=Text(wr, text="INT",size=8)
    intt=TextBox(wr)
    
    abs=Text(wr, text="WIS",size=8)
    wis=TextBox(wr)
    
    abs=Text(wr, text="CHA",size=8)
    cha=TextBox(wr)

    abs=Text(wr, text="Money",size=8)
    money =TextBox(wr)
    
    abs=Text(wr, text="Armor",size=8)
    armor =TextBox(wr)

    fwrite=PushButton(wr,text="WRITE!",command=lambda:write2(cn.value,clas.value,race.value,xp.value,st.value,dex.value,con.value,intt.value,wis.value,cha.value,money.value,armor.value))
    
def Dice2(nds):
    
    Dc2=Window(app,title="Dice2")
    Rr = random.randint(1,nds)
    abs= Text(Dc2,text =str(Rr),width=24)
    
def Dice():

    Dc=Window(app, title="Roll Dice")

    nds=TextBox(Dc,text="Enter Number of dice sides",width=24)

    fwrite=PushButton(Dc,text="Roll!",command=lambda:Dice2(int(nds.value)))
    

intro = Text(app,text="RFID - Interactive Interface",size=30)
read = PushButton(app, text="Read Figure",width=35,height=10)
write = PushButton(app, text="Write to Figure",command=writeApp,width=35,height=10)
Dice_Roll = PushButton(app, text="Roll dice",command=Dice,width=35,height=10)

app.display()   
