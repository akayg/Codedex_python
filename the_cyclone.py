# code for ammusment park ride
credit=int(input("credit "))
height=int(input("input height in cm"))
if height >= 137 and credit >=10 :
  print("Enjoy the ride!")
elif height >=137 and credit < 10 :
  print("You don't have enough credit")
elif height < 137 and credit >= 10 :
  print("you are not tall enough")
else :
  print("You does not meet either requirement :( ")