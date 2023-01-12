def spy_game(l):
   t = ""
   for i in range(len(l)):
      if l[i]=='0' or l[i]=='7':
         t += l[i]
   if '007' in t:
      return True
   else:
      return False
   