import datetime

CurrentDate= (datetime.datetime.today())
print (CurrentDate)
print (datetime.datetime.today().weekday())
if CurrentDate.weekday() != 5 and CurrentDate.weekday() != 6:
  print ("nao e fds")
else:
  print ("é fds")