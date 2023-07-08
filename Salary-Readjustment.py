print('Calculate your raise')
x = float(input('Enter your Salary:'))
if x > 1250 :
  s=(x*0.10)+x
  a=(x*0.10)
  print('You will receive an increase in the amount of',round(a,2),'totaling',round(s,2))
elif x <= 1250 :
  s=(x*0.15)+x
  a=(x*0.15)
  print('You will receive an increase in the amount of',round(a,2),'totaling',round(s,2))
