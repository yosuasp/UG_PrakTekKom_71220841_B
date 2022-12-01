def add(p,d):
    return f'{p} +{d} = {p+d}'
def subtract(p,d):
    return f'{p} - {d} = {p-d}'
def multiply(p,d):
    return f'{p} * {d}= {p*d}'
def divide(p,d):
    return f'{p} / {d} = {p/d}'
kalkulator = {
    'add':add,
    'subtract': subtract,
    'multiply' : multiply,
    'divide' : divide
}
print ("select operation.")
for i,option in enumerate (kalkulator,start=1):
    print(f'{i}. {option}')

choice = list (kalkulator)[int(input('\nEnter choice(1/2/3/4):'))-1]

num1 = float(input('\nEnter first number:'))
num2 = float(input('Enter scond number: '))
print(kalkulator[choice](num1,num2))









