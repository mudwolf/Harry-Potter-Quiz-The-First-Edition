import time

print("Welcome to the Harry Potter Quiz : The First Edition\n\n")
time.sleep(1)
score = 0
name = input("What is your name? \n")
print("Hello," +name + "\n\n")
time.sleep(1.5)
print("This Quiz consits of 7 Questions")
time.sleep(2)
print("To answer Type 1,2,3,4 and Enter from the following ")
time.sleep(2)
print("Let's get started")
time.sleep(2)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

#Question 1
q1 = int(input("\n\nQ1. What was the name of Hagrid’s three-headed dog that guarded the Philosopher’s Stone?\n\n""1.Fluffy \n2.Tiny \n3.Bruce \n4.Snuggles""\n\nAnswer : "))

if q1 == 1:
  score += 1
  print("\nCorrect")
  print("Score " + str(score) + " / 7")
else:
  print("\nWrong Answer.") 
  print("\nTotal Score  : " + str(score))
  print("\n💀 Game Over 💀 \n\n Refresh or Restart ")
  exit()
  
time.sleep(3)


#Question 2
q2 = int(input("\n\nQ2. What breed of dragon was Norbert – Hagrid’s baby dragon?\n\n""1.Common Welsh Green \n2.Chinese Fireball \n3.Hungarian Horntail \n4.Norwegian Ridgebac""\n\nAnswer : "))

if q2 == 4:
  score += 1
  print("\nCorrect")
  print("Score " + str(score) + " / 7")
else:
  print("\nWrong Answer.") 
  print("\nTotal Score  : " + str(score))
  print("\n💀 Game Over 💀 \n\n Refresh or Restart ")
  exit()
time.sleep(3)


#Question 3
q3 = int(input("\n\nQ3. What colour was the Weasley jumper than Harry got as a Christmas present?\n\n""1.Blue \n2.Brown \n3.Maroon \n4.Emerald green""\n\nAnswer : "))

if q3 == 4:
  score += 1
  print("\nCorrect")
  print("Score " + str(score) + " / 7")
else:
  print("\nWrong Answer.") 
  print("\nTotal Score  : " + str(score))
  print("\n💀 Game Over 💀 \n\n Refresh or Restart ")
  exit()
time.sleep(3)


#Question 4
q4 = int(input("\n\nQ4. During the Sorting Ceremony, who was the first student to be sorted into Gryffindor?\n\n""1.Hermione Granger \n2.Lavender Brown \n3.Parvati Patil \n4.Dean Thomas""\n\nAnswer : "))

if q4 == 2:
  score += 1
  print("\nCorrect")
  print("Score " + str(score) + " / 7")
else:
  print("\nWrong Answer.") 
  print("\nTotal Score  : " + str(score))
  print("\n💀 Game Over 💀 \n\n Refresh or Restart ")
  exit()
time.sleep(3)


#Question 5
q5 = int(input("\n\nQ5. On the giant wizarding chessboard through the trapdoor, what chess piece did Hermione play as?\n\n""1.Bishop \n2.Pawn \n3.Castle \n4.Knight""\n\nAnswer : "))

if q5 == 3:
  score += 1
  print("\nCorrect")
  print("Score " + str(score) + " / 7")
else:
  print("\nWrong Answer.") 
  print("\nTotal Score  : " + str(score))
  print("\n💀 Game Over 💀 \n\n Refresh or Restart ")
  exit()
time.sleep(3)


#Question 6
q6 = int(input("\n\nQ6. What did the first-years have to do as the practical part of their Transfiguration exam?\n\n""1.Turn a hedgehog into a pin cushion \n2.Turn a mouse into a snuff-box \n3.Turn a rat into a goblet \n4.Turn a toad into a balloon""\n\nAnswer : "))

if q6 == 2:
  score += 1
  print("\nCorrect")
  print("Score " + str(score) + " / 7")
else:
  print("\nWrong Answer.") 
  print("\nTotal Score  : " + str(score))
  print("\n💀 Game Over 💀 \n\n Refresh or Restart ")
  exit()
time.sleep(3)


#Question 7
q7 = int(input("\n\nQ7. On Harry’s school list, what material did it say his cauldron should be made from?\n""1.Pewter \n2.Gold \n3.Steel \n4.Iron""\n\nAnswer : "))

if q7 == 1:
  score += 1
  print("Correct")
  print("Score " + str(score) + " / 7")
else:
  print("\nWrong Answer.") 
  print("\nTotal Score  : " + str(score))
  print("\n💀 Game Over 💀 \n\n Refresh or Restart ")
  exit()
time.sleep(1.5)

print("\n\n\nCongratulation "+name+", You have won Harry Potter Quiz : The First Edition\n\n")
time.sleep(2)
print("Signing off in\n")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
exit()


 



