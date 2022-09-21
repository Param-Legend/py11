n=int(input('enter year to knew it is leap or not '))
if(n%4==0 and n%100!=0 or n%400==0):
  print('this is leap year')
else:
  print('this is not in leap year')

cm = float(input('enter cm to convert inch and feet'))
print(float(cm*0.394),'inch')
print(float(cm*0.0328),'Feet')
