def info():
   broadcast("<{[SYSTEM]}>: Type /rules to see the rules,")
   broadcast("and /discord to get a link to our Discord server.")

import random
def rules(user,dirs,broadcast):
   filepath = os.path.join(dirs[4], user) # 0% chance of silly rules on first time
   with open(filename, "r+") as f:
      data = f.read()
      f.seek(0)
      f.write('knownrules')
      f.truncate()
   silly = False
   if data == 'knownrules':
      if random.randint(1, 100) <= 10:
         silly = True
   if silly == False:
      broadcast("<{[SYSTEM]}>: Rules:")
      broadcast("1. No racist, sexist, homophobic, or other prejudiced language or behavior, whether it's aimed at another user or not.")
      broadcast("2. No asking for or sharing personal info of yourself or anyone else. This includes name, age, gender, location, phone number, email address, or any other personally identifiable information. Doxxing (or the threat of doing so) is grounds for a ban.")
      broadcast("3. No overly violent or sexual behavior or language, including threats of violence or harm of ANY kind. This includes threats or discussion of harming yourself.")
      broadcast("4. No political discussion. Usernames of political figures are allowed (with some exceptions), but any language that could incite arguments may get you banned.")
      broadcast("5. No impersonation of developers, moderators, admin, or any other Aurorachat staff. Additionally, ANY impersonation for the sake of harrassing another user is not allowed.")
      broadcast("6. No spamming.")
      broadcast("7. No hunting.")
      broadcast("8. No hacking.")
      broadcast("Friend code sharing is allowed, but please do not harrass or pressure other users for their friend codes.")
      broadcast("We are not accepting ban appeals at this time.")
   else:
      broadcast("<{[SYSTEM]}>: Rules (silly):")
      broadcast("1. No saying oatmeal")
      broadcast("2. Eat burger or else")
      broadcast("2. No numbers containing 6 or 7")
      broadcast("3. 100% accurate grammar")
      broadcast("4. Crow like a rooster when you log in")
      broadcast("5. Ganondorf Suavemente gif")
      broadcast("6. no more mr nice guy")
      broadcast("7. no hackertron")
      broadcast("8. eat burger")
      broadcast("9. Pigs must fly")
      broadcast("10. No more fortnite")
      broadcast("11. No battery")
      broadcast("12. No cats allowed")
      broadcast("13. No dogs allowed either")
      broadcast("Alright if I was an animal what animal do you think I would be? SERIOUS ANSWERS ONLY.")
      broadcast("A rooster. A rat. A rat. A rat. A rat. You’d be a rat. Jerma you’re a rat. You’d be a rat. I think you’d be a rat. I think i’d be a wolf. I think so too. I would be a wolf lion hybrid mix. King of the Junjile— Junjile, but still social and with it and ferocious.")
      broadcast("No ban appeals. Why can't you listen?")

def discord():
   broadcast("<{[SYSTEM]}>: Want access to the rest of Unitendo? Join our official Discord server here:")
   broadcast("https://discord.gg/dCSgz7KERv")

def cmd(cmd,callback,args=[],kwargs={}): # Command wrapper
   if data['content'].startswith(cmd+' '):
      return callback(*args, **kwargs)

# Custom commands (other than /ban, /unban, and the welcome message) go here
# Syntax:
# result = cmd("/cmd", func, args=[], kwargs={})
# the dirs variable is a list containing [ACCOUNT_DIR, BANNEDUSR_DIR, BANNEDIP_DIR, ADMIN_DIR, KNOWNUSR_DIR]
def cmdSetup(user,msg,dirs,broadcast):
   result = cmd("/info", info)
   result = cmd("/rules", rules, args=[user,dirs,broadcast])
   result = cmd("/discord", discord)

   return result
