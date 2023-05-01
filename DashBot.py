from distutils.command.upload import upload
import time,requests,random,os,base64,hashlib
from itertools import cycle
from urllib3 import connection
from json import loads
from threading import Thread

substitution = {"r":"w",
"l":"w",
"R":"W",
"L":"W",
"no":"nu",
"has":"haz",
"have":"haz",
"you":"uu",
"the":"da",
"R":"W",
"The":"Da" }
#Prefixes
prefix = ["<3 ",
"H-hewwo?? ",
"HIIII! ",
"Haiiii! ",
"Huohhhh. ",
"OWO ",
"OwO ",
"UwU ",
"88w88 ",
"H-h-hi, ",]
#Suffixes
suffix = [" :3",
" UwU",
" >_>",
" ^_^",
"..",
" Huoh.",
" ^-^",
" ;_;",
" xD",
" x3",
" :D",
" :P",
" ;3",
" XDDD",
" Sigh.",
" ._.",
" >_<"
"xD xD xD",
":D :D :D",]
def owoify(owo):
    for word, initial in substitution.items():
        owo = owo.replace(word.lower(), initial)
    output = random.choice(prefix) + owo + random.choice(suffix)
    return output

def request(self, method, url, body=None, headers=None):
    if headers is None:
        headers = {}
    else:
        # Avoid modifying the headers passed into .request()
        headers = headers.copy()
    super(connection.HTTPConnection, self).request(method, url, body=body, headers=headers)
connection.HTTPConnection.request = request

def comment_chk(*,username,comment,levelid,percentage,type):
        part_1 = username + comment + levelid + str(percentage) + type + "xPT6iUrtws0J"
        return base64.b64encode(xor(hashlib.sha1(part_1.encode()).hexdigest(),"29481").encode()).decode()
def xor(data, key):
        return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
def gjp_encrypt(data):
        return base64.b64encode(xor(data,"37526").encode()).decode()
def gjp_decrypt(data):
        return xor(base64.b64decode(data.encode()).decode(),"37526")

def getGJUsers(target):
    data={
        "secret":"Wmfd2893gb7",
        "str":target
    }
    request =  requests.post("http://www.boomlings.com/database/getGJUsers20.php",data=data,headers={"User-Agent": ""}).text.split(":")[1::2]
    username = request[0]
    uuid = request[2]
    accountid = request[10]
    return (username,accountid,uuid)

def uploadGJComment(name,passw,comment,perc,level):
        try:
                accountid = getGJUsers(name)[1]                                                                                                                        
                gjp = gjp_encrypt(passw)
                c = base64.b64encode(comment.encode()).decode()
                chk = comment_chk(username=name,comment=c,levelid=str(level),percentage=perc,type="0")
                data={
                    "secret":"Wmfd2893gb7",
                    "accountID":accountid,
                    "gjp":gjp,
                    "userName":name,
                    "comment":c,
                    "levelID":level,
                    "percent":perc,
                    "chk":chk
                }
                return requests.post("http://www.boomlings.com/database/uploadGJComment21.php",data=data,headers={"User-Agent": ""}).text
        except:
                return "problem"


print(" _____            _     ____        _   ")
print("|  __ \          | |   |  _ \      | |  ")
print("| |  | | __ _ ___| |__ | |_) | ___ | |_ ")
print("| |  | |/ _` / __| '_ \|  _ < / _ \| __|")
print("| |__| | (_| \__ \ | | | |_) | (_) | |_ ")
print("|_____/ \__,_|___/_| |_|____/ \___/ \__|")
print("v1.1")


un = input("Username: ")
pw = input("Password: ")
lvlid = input("Level ID: ")
print("Bot is running on " + lvlid + "!")
uploadGJComment(un,pw,"DashBot is running here! Use /help1 /help2 /help3 for the list of available commands.","0",lvlid)
def commands(level):
  url=f"http://gdbrowser.com/api/comments/{level}?count=1"
  r=loads(requests.get(url).text)[0]
  u=r['username']
  com=r['content']
  perc=random.randint(42,69)
  eightball=['Without a doubt', 'Nope', 'Definitely yes', 'This will never happen']
  coin=['Tails', 'Heads']
  yesNo=['Yes', 'No']
  if(com.startswith("/ai")):
    c=com.split("/ai ")
    resp = requests.get("http://api.brainshop.ai/get?bid=169422&key=4GCemcdYgy50PlZ2&uid=0&msg="+c[1], headers={'Accept': 'application/json'})
    jsonResp = resp.json()
    airesp = jsonResp["cnt"]
    uploadGJComment(un,pw,f"{u}, {airesp}",perc,level)
    print(f"/ai executed by {u}: {com}")
  elif(com.startswith("/owoify")):
    c=com.split("/owoify ")
    resp = requests.get("http://api.brainshop.ai/get?bid=169422&key=4GCemcdYgy50PlZ2&uid=0&msg="+c[1], headers={'Accept': 'application/json'})
    jsonResp = resp.json()
    airesp = jsonResp["cnt"]
    cc = owoify(airesp)
    uploadGJComment(un,pw,f"{u}, {cc}",perc,level)
    print(f"owoify executed by {u}: {com}")
  elif(com.startswith("/help1")):
      uploadGJComment(un,pw,f"Commands: /info, /ai (input), /diceroll, /coinflip, /8ball (question) (page 1/3, /help2, /help3)",perc,level)
      print(f"help1 executed by {u}: {com}")
  elif(com.startswith("/help2")):
      uploadGJComment(un,pw,f"Commands: /fart, /poll (option1), (option2), /cool, /owoify (input) (/help1, page 2/3, /help3)",perc,level)
      print(f"help2 executed by {u}: {com}")
  elif(com.startswith("/help3")):
      uploadGJComment(un,pw,f"Commands: /rickroll (username), /stats (username), /likeif (input) (/help1, /help2, page 3/3)",perc,level)
      print(f"help3 executed by {u}: {com}")
  elif(com.startswith("/info")):
      uploadGJComment(un,pw,f"Version 1.1 is running. Use /cmdinfo and then the command name to see how to use. Example: /cmdinfo 8ball",perc,level)
      print(f"info executed by {u}: {com}")
  elif(com.startswith("/stats")):
     c=com.split("/stats ")
     cc=c[1]
     shtats=loads(requests.get(f"http://gdbrowser.com/api/profile/{cc}").text)
     ccc=f"@{u}, {c[1]} has {shtats['stars']} Stars, {shtats['diamonds']} Diamonds, {shtats['coins']} Coins, {shtats['userCoins']} User Coins, {shtats['demons']} Demons and {shtats['cp']} Creator Points."
     uploadGJComment(un,pw,f"{ccc}",perc,level)
     print(f"stats executed by {u}: {com}")
  elif(com.startswith("/cmdinfo stats")):
      uploadGJComment(un,pw,f"INFO: /stats will write the stats of the specified user.",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
  elif(com.startswith("Im")):
     c=com.split("Im ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm Dad! (stupid joke bruh)",perc,level)
  elif(com.startswith("im")):
     c=com.split("im ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm Dad! (stupid joke bruh)",perc,level)
  elif(com.startswith("I'm")):
     c=com.split("I'm ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm Dad! (stupid joke bruh)",perc,level)
  elif(com.startswith("i'm")):
     c=com.split("i'm ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm Dad! (stupid joke bruh)",perc,level)
  elif(com.startswith("I am")):
     c=com.split("I am")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm Dad! (stupid joke bruh)",perc,level)
  elif(com.startswith("i am")):
     c=com.split("i am ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm Dad! (stupid joke bruh)",perc,level)
  elif(com.startswith("i am")):
     c=com.split("i am ")
     cc=c[1]
     uploadGJComment(un,pw,f"Hey {cc}, I'm Dad! (stupid joke bruh)",perc,level)
  elif(com.startswith("/8ball")):
     balls = random.choice(eightball)
     uploadGJComment(un,pw,f"@{u}, the Magic 8 Ball says: {balls}",perc,level)
     print(f"8ball executed by {u}: {com}")
  elif(com.startswith("/cmdinfo 8ball")):
      uploadGJComment(un,pw,f"INFO: /8ball will write a random answer.",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
  elif(com.startswith("/cool")):
     cool=random.randint(0,100)
     uploadGJComment(un,pw,f"@{u}, you are {cool}% cool!",perc,level)
     print(f"cool executed by {u}: {com}")
  elif(com.startswith("/cmdinfo cool")):
      uploadGJComment(un,pw,f"INFO: /cool will show how cool are you in percents.",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
  elif(com.startswith("/coinflip")):
     flip=random.choice(coin)
     uploadGJComment(un,pw,f"@{u}, {flip}",perc,level)
     print(f"coinflip executed by {u}: {com}")
  elif(com.startswith("/cmdinfo coinflip")):
      uploadGJComment(un,pw,f"INFO: /coinflip will say Heads or Tails randomly.",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
  elif(com.startswith("/diceroll")):
     roll=random.randint(1,6)
     uploadGJComment(un,pw,f"@{u}, {roll}",perc,level)
     print(f"diceroll executed by {u}: {com}")
  elif(com.startswith("/cmdinfo diceroll")):
      uploadGJComment(un,pw,f"INFO: /diceroll will write a random number between 1 and 6.",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
  elif(com.startswith("/poll")):
     c=com.split("/poll ")
     cc=c[1]
     d=cc.split(", ")
     dd=d[1]
     ccc=cc.split(", " + dd)
     cccc=ccc[0]
     uploadGJComment(un,pw,f"POLL by {u}: Like = {cccc}, Dislike = {dd}",perc,level)
     print(f"poll executed by {u}: {com}")
  elif(com.startswith("/cmdinfo poll")):
      uploadGJComment(un,pw,f"INFO: /poll will write a message with the options you added. (separate options with ,)",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
  elif(com.startswith("/likeif")):
     c=com.split("/likeif ")
     cc=c[1]
     uploadGJComment(un,pw,f"Like if {cc}",perc,level)
     print(f"likeif executed by {u}: {com}")
  elif(com.startswith("/cmdinfo likeif")):
      uploadGJComment(un,pw,f"INFO: /likeif will post a like if comment with your input.",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
  elif(com.startswith("/fart")):
     uploadGJComment(un,pw,f"@{u} farddddddddddddddd",perc,level)
     print(f"fart executed by {u}: {com}")
  elif(com.startswith("/cmdinfo fart")):
      uploadGJComment(un,pw,f"INFO: /fart will fart.",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
  elif(com.startswith("/rickroll")):
     c=com.split("/rickroll ")
     cc=c[1]
     uploadGJComment(un,pw,f"@{cc}, you got rickrolled by @{u}: Never gonna give you up,...",perc,level)
     print(f"rickroll executed by {u}: {com}")
  elif(com.startswith("/cmdinfo rickroll")):
      uploadGJComment(un,pw,f"INFO: /rickroll will post the rickroll lyrics and mentioning the specified user.",perc,level)
      print(f"cmdinfo executed by {u}: {com}")
lvl = lvlid
while 1:
    try:
        t=Thread(target=commands,args=(lvl,))
        t.start()
        time.sleep(1.6)
    except:
        print("err")
