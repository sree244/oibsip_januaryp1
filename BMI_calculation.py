# the below code is for calculation of BMI index when user inputs are height and weight.

def cal_BMI(h,w):
  c=w/h
  if(c<18.5):
    print("your BMI is :",c,"\nYour weight status is underweight!!")
  elif(18.5<c<=24.9):
    print("Your BMI is: ",c,"\nYour weight status is Normal range!!")
  elif(25.0<=c<=29.9):
    print("Your BMI is: ",c,"\nYour weight status is Overweight!!")
  else:
    print("Your BMI is: ",c,"\nYour weight status is Obesity!!!")
weight=float(input("Enter weight in kilograms:"))
height=float(input("Enter height in meters:"))
cal_BMI(height,weight)
