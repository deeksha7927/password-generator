#import the required libraries
import string
import random
#defining function to generate password
def password_generator():
  s1=string.ascii_lowercase
  s2 = string.ascii_uppercase
  s3 = string.digits
  s4 = string.punctuation
  s1=list(s1)
  s2=list(s2)
  s3=list(s3)
  s4=list(s4)
  s=[]
  s.extend(s1)
  s.extend(s2)
  s.extend(s3)
  s.extend(s4)
  #Enter the length of the password
  plen=int(input("Enter the password length \n"))
  pa1=random.choice(s1)+random.choice(s2)+random.choice(s3)+random.choice(s4)
  random.shuffle(s)
  x=plen-4
  pa2="".join(s[0:x])
  print("Your password is:")
  return pa1+pa2
print(password_generator())




