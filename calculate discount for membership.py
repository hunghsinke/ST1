#write a description of class calculateDiscount here
#author: Hung Hsin ke 
#date created: 12/7/2021

def calculateDiscountA(totalAmount, noOfYears):#step 3
    discountValue = totalAmount * (0.02 + noOfYears * 0.01)
    print (f'Your discount is {discountValue:.2f}')

def calculateDiscountB(totalAmount):#step 4
    discountValue = totalAmount * 0.02
    print(f'Your discount is {discountValue:.2f}')

def main():
    totalAmount = float(input('Enter total purchase amount:' )) #step 1
    f_letter = input('Enter first letter of your membership (A, B): ')
    f_letter = f_letter[0]
    f_letter = f_letter.upper()
    if f_letter == 'A':
        noOfYears = int(input('Enter the number of years: '))#step 2
        calculateDiscountA(totalAmount, noOfYears)
    elif f_letter == 'B':
        calculateDiscountB(totalAmount)
    else:
        print('Not a registered customer, sorry no discount')

main() #start of the program