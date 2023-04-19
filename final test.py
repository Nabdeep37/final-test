phonedirectory = {}
option=0
while(option!=5):
#display the menu
 print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
 print("1. add a record.")
 print("2. search a record.")
 print("3. update a record.")
 print("4. delete a record.")
 print("5. quit")

#for taking user's choice
 option = int(input("enter option:"))

#for adding a record use conditions for showing options
 if(option==1):
  n=input("Enter your name:")
  if any(char.isdigit() for char in n):
    print("there is an error in your name")
  m=int(input("Enter your 10-digit mobile number:"))
  if len(str(m)) == 10:
    print("valid phone number")
    print("Record added")
  else:
    print("invalid phone number")
  phonedirectory.update({n:m})
  
 #for search a record
 if(option==2):
  n=input("Enter name to search:")
  if n in phonedirectory:
    print(n + ":" + str(m))
  else:
    print(n + "not found")

  #for update a record
 elif(option==3):
  n = input("Enter your name:")
  if n in phonedirectory:
    phone= input("Enter new 10-digit phone number: ")
    m= phone
    print("record updated")
  else:
     print(n + " not found")

  #for deleting a record
 elif(option==4):
  n=input("Enter your name:")
  if n in phonedirectory:
    del m
    print("record deleted")
  else:
    print(n+":"+"not found")

  #for quit
 elif(option==5):
   break

 #invalid option
else:
  print("your option is invalid")