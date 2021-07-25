principal=float(input('Enter the amount to be invested: '))
interestRate=float(input('Enter the interest rate per year: '))
noOfYears=int(input('Enter the No. of years: '))
finalSum=0
for i in range(0,noOfYears):
  finalSum+=((principal*interestRate)/100)
principal+=finalSum
print('Total amount to be received after {} years is {}.'.format(noOfYears,principal))
 

  
