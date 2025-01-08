Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

ans = int(input("Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))

if ans == 1:
    Gryffindor += 1  # Properly increment Gryffindor
elif ans == 2:
    Slytherin += 1
ans = int(input(" When I’m dead, I want people to remember me as:\n1)The Good \n2)The Great \n3)The Wise \n4)The Bold\n"))

if ans == 4:
    Gryffindor += 2  # Properly increment Gryffindor
elif ans == 2:
    Slytherin += 2
elif ans == 3 :
  Ravenclaw += 2
elif ans == 1:
  Hufflepuff += 2   # Example: increment another house for Dusk (customizable)

ans =int(input("Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
if ans == 4:
    Gryffindor += 2  # Properly increment Gryffindor
elif ans == 1:
    Slytherin += 4
elif ans == 3 :
  Ravenclaw += 4
elif ans == 2:
  Hufflepuff += 4 
print("Gryffindor:", Gryffindor)
print("Slytherin:", Slytherin)
print("Ravenclaw:", Ravenclaw)
print("Hufflepuff :", Hufflepuff )
if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')