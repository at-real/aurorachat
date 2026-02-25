def checkAdmin(user,dirs):
   filepath = os.path.join(dirs[3], user)
   if os.path.exists(filepath):
      return True
   return False

def ban(user,msg,dirs):
   if not checkAdmin(user,dirs):
      return "<{[SYSTEM]}>: Unauthorized."
   parts = data['content'].split(' ', 2)
   userToBan = parts[2].strip()
   usrOrIp = parts[1].strip()
   if usrOrIp == "user":
      filepath = os.path.join(dirs[0], userToBan)
      if os.path.exists(filepath):
         filepath2 = os.path.join(dirs[1], userToBan)
         if os.path.exists(filepath2):
            return "<{[SYSTEM]}>: User already banned."
         else:
            with open(filepath2, 'w') as f:
               f.write('banned')
            return "<{[SYSTEM]}>: User banned successfully."
      else:
         return "<{[SYSTEM]}>: Account not found."
   elif usrOrIp == "ip":
      filepath = os.path.join(dirs[2], userToBan)
      if os.path.exists(filepath):
         return "<{[SYSTEM]}>: IP already banned."
      else:
         with open(filepath, 'w') as f:
            f.write('banned')
         return "<{[SYSTEM]}>: IP banned successfully."
   else:
      return "<{[SYSTEM]}>: Invalid syntax."
def unban(user,msg,dirs):
   if not checkAdmin(user,dirs):
      return "<{[SYSTEM]}>: Unauthorized."
   parts = data['content'].split(' ', 2)
   userToUnban = parts[2].strip()
   usrOrIp = parts[1].strip()
   if usrOrIp == "user":
      filepath = os.path.join(ACCOUNT_DIR, userToUnban)
      if os.path.exists(filepath):
            filepath2 = os.path.join(BANNEDUSR_DIR, userToUnban)
            if os.path.exists(filepath2):
                  os.remove(filepath2)
                  return "<{[SYSTEM]}>: User unbanned successfully."
            else:
                  return "<{[SYSTEM]}>: Account not banned."
      else:
            return "<{[SYSTEM]}>: Account not found."
   elif usrOrIp == "ip":
      filepath2 = os.path.join(BANNEDIP_DIR, userToUnban)
      if os.path.exists(filepath2):
         os.remove(filepath2)
         return "<{[SYSTEM]}>: IP unbanned successfully."
      else:
         return "<{[SYSTEM]}>: IP not banned."
   else:
      return "<{[SYSTEM]}>: Invalid syntax."
def welcomeMsg(user,dirs,broadcast):
   filepath = os.path.join(dirs[4], user)
   if not os.path.exists(filepath):
      with open(filepath, 'w') as f:
         f.write('known')
      broadcast("<{[SYSTEM]}>: " + f"{user}, type /info if you're new!")

def cmd(cmd,callback,args=[],kwargs={}): # Command wrapper
   if data['content'].startswith(cmd+' '):
      return callback(*args, **kwargs)

def checkCmd(user,msg,dirs,broadcast):
   welcomeMsg(user,dirs,broadcast)

   result = cmd("/ban", ban, args=[user,msg,dirs])
   result = cmd("/unban", unban, args=[user,msg,dirs])

   import custom_commands

   result = custom_commands.cmdSetup(user,msg,dirs,broadcast)

   if result != None:
      broadcast(result)
