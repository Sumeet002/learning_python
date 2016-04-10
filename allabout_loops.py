#while
count  = 1
while count < 5 :
  print "%d Mississippi" % count
  count +=1

#infinite loop
#while 1:
#  str = raw_input("Ask GROOT a question:")
#  print "I am GROOT!"

#while with if/else
count = 5
while count > 0 :
  count = count - 1
  if count == 0 :
    print "We are low on energy Sir!"
  print "We are at %d"% (count*10) + u"\u0025" +" energy Sir!"

else:
  print "We are out of power Sir! I am shutting down"
  print "No! Jarvis dont leave me alone buddy"

#for
for letter in "Supercalifragilisticexpialidocious":
  print letter

bourne_series = ['Identity','Supremacy','Ultimatum','Legacy']
for serie in bourne_series:
  print serie

for serie in range(len(bourne_series)):
  print bourne_series[serie]

#else with for and indentation problem
for pos in range(1,20):
  if pos < 4 :
    print "Congratulations your team made the top3 . You are qualified for the champions league"
  else:
    print "You are not amongst the elite!"

for pos in range(1,20):
  if pos < 4 :
    print "Congratulations your team made the top3 . You are qualified for the champions league"
else:
    print "You are not amongst the elite!"

#nested loops while
#comma suppresses default newline in print
mat = 8
posy=0
while posy < mat:
  print "\t\t",
  posx=0
  while posx < mat:
    print "%d" % (8*posy + posx),
    posx +=1
  print "\n",
  posy+=1


#nested loops for
#comma suppresses default newline in print
insanity = 8
for posy in range(0,insanity):
  print "\t\t",
  for posx in "All work and no play makes Jack a dull boy":
    print posx,
  print "\n",

#break
dest_floor = int(raw_input("Enter floor no(10 storey building):"))
print dest_floor
for curr_floor in range(0,10):
  if (curr_floor == dest_floor):
    print "You have arrived on floor no %d" % dest_floor
    break
  print "You are now on floor no %d" % curr_floor

#continue
num = 0
for num in range(0,25):
  if (num % 3 == 0):
    print "ping"
    continue
  if (num % 5 == 0):
    print "pong"
    continue
  print "%d"%num

#pass
for letter in "Show me the $":
  if letter == '$':
    pass
    print "......",
  print letter,
