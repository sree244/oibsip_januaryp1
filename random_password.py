# the below code is for random password generator.

import random
n=int(input("Enter length of the password that you want to generate:"))
isatleast_1_uppercase=input("Enter True if atleast one element of password is uppercase otherwise False:")
isatleast_1_special=input("Enter True if atleast one element of password is special character otherwise False:")
isatleast_1_lowercase=input("Enter True if atleast one element of password is lowercase otherwise False:")
uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
specials=['!','@','#','$','%','^','&','*']
password=""
if((isatleast_1_special) and (isatleast_1_lowercase) and (isatleast_1_uppercase) and (n<3)):
  print("Enter the length of the password correctly!!!!")
else:
  if(isatleast_1_uppercase):
    password=password+random.choice(uppercase)
  if(isatleast_1_lowercase):
    password=password+(random.choice(uppercase)).lower()
  if(isatleast_1_special):
    password=password+random.choice(specials)
  if(n==3):
    print("Your random password that is generated is : ",password)
  else:
    for i in range(0,n-3):
      m=random.choice([1,2,3])
      if(m==1):
        password=password+random.choice(uppercase)
      elif(m==2):
        password=password+(random.choice(uppercase)).lower()
      else:
        password=password+random.choice(specials)
    print("Your random password that is generated is : ",password)
