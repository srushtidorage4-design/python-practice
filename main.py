print("apanacollege",  end="")
print("shradhasatpute")

def calc_prod(a=1,b=6):
    print(a*b)
    return a*b
calc_prod()


cities=["gurgaon","pune","chennai","mumbai"]
def print_len(cities):
    print(len(list))

    print_len(cities)

def print_list(list):
    for item in list:
        print(item,end="")




def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)    


calc_fact(5)  


def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")

converter(800)


def testing():
    print("testing function called..")

    def inner():
        print("Inner function called..")

    return inner

result=testing()
print(type(result))
result()

def my_function(num):
    print("my_function is called..")
    def getSqr():
        print("getSqr called..")
        return num*num
    return getSqr


result = my_function(10)
print(result())


def addition(a,b):
    if a>10 and b>10:
        return a+b
    print("Both numbers should be greater than 10")

result=addition(9,20)
print(result)

#Day:2

# Task1: Tuples and tuple unpacking
student_record=("Alice",20,"computer science",3.8)
name,age,major,gpa=student_record
print(f"{name}is {age}year old,majoring in {major}with a {gpa} GPA.")


# Task2: positional and keyword Argument

def describe_pet(animal_type,pet_name):
    print(f"I have a {animal_type} name {pet_name}.")

describe_pet("Dog","Buddy")

describe_pet(pet_name="Whiskers",animal_type="cat")

# Task 3 Arbitary positional argumennts

def calculate_average(*args):
    average=sum(args)/len(args)
    return average

result1=calculate_average(80,90,70)
print("Average of 3 score:",result1)

result2=calculate_average(80,90,70,85,75,95)
print("Average of 6 scores:", result2)


#Task 4:Arbitary keyword Arguments

def build_user_profile(username,**kwargs):
    print("Username:",username)

    for key,value in kwargs.items():
        print(key,":",value)

build_user_profile("Alice",location="pune",hobby="coding",is_active=True)
   


#Task5: combining *args and **kwargs
  
def restaurant_order(table_number,*menu_items,**special_request):
    print("Table Number:",table_number)

    print("Ordered Items :")
    for item in menu_items:
        print("_",item)

    print("special Request:")
    for key,value in special_request.items():
        print(key,":",value)

restaurant_order(5,"pizza","burger","french fries","cold coffee",allergies="peanuts",extra_spicy=True)

# Task 6: nested function and tuple return

def data_procerssor(x,y):
    def add_numbers():
        return x+y
    def multiply_numbers():
        return x*y
    return add_numbers(),
    multiply_numbers() 
    addition_result,multiplication_result=data_processor(5,10)
    print("Addition:",addition_result)
    print("Multiplication:",multiplication_result)

#Day:3

# Task1:understanding callbacks

def square_number(n):
    return n*n
def process_list(numbers,callback):
    results=[]

    for number in numbers:results.append(callback(number))
    return results
numbers=[1,2,3,4,5]
result=process_list(numbers,square_number)
print(result)


#Task 2: creating a basic closure

def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier

times_three=make_multiplier(3)
times_five=make_multiplier(5)

print(times_three(10))
print(times_five(10))


#Task 3:closure with state

def create_account(initial_balance):
    def  deposit(amount):
         nonlocal initial_balance
         initial_balance=initial_balance+amount
         return initial_balance
    return deposit
account=create_account(100)
print(account(50))
print(account(20))


#Task 4:Decorators-old 

def greetings():
    return "hello world"
def uppercase_decorator(func):
    def  wrapper():
        result=func()
        return result.upper()
    return wrapper

greetings=uppercase_decorator(greetings)
print(greetings())


#Task5:Decorators

def log_execution(func):
    def wrapper(a,b):
        print("Starting execution...")

        result=func(a,b)
        print("finished execution.")

        return result
    return wrapper
@log_execution
def add_numbers(a,b):
    return a+b

result=add_numbers(5,7)
print(result)


#Task6:practical decorator-zero division checker

def safe_divide(func):
    def wrapper(a,b):
        if b==0:
            return "Error: cannnot divide by zero!"
        return func(a,b)
    return wrapper

@safe_divide
def divide(a,b):
    return a/b
print(divide(10,2))
print(divide(10,0))

#Day:4

#Task 1: Basic class and object creation

class Book:
    def read(self):
        print("Reading a great book!")
my_book=Book()
my_book.read()


#Task 2:The constructor _init_

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
my_car=Car("Toyota","Corolla",2022)
print(my_car.make)
print(my_car.year)


#Task3: Adding Instance Methods
#Add display_info()to the same car class:

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print(f"{self.year}{self.make}{self.model}")

    def display_info(self):
        print(f"{self.year}{self.make}{self.model}")

my_car=Car("Toyota","Corolla",2022)

print(my_car.make)
print(my_car.year)
my_car.display_info()


# Task 4:Encapsulation  

class BankAccount:
    def __init__(self,account_holder,initial_balance):
        self.account_holder=account_holder
        self.__balance=initial_balance

my_account=BankAccount("Alice",1000)

print(my_account.account_holder)
#print(my_account.__balance)

#Task 5:Getters and setters

class BankAccount:
    def __init__(self,account_holder,initial_balance):
        self.account__holder=account_holder
        self.__balance=initial_balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance=self.__balance=amount
        print("New balance:",self.__balance)

my_account=BankAccount("Alice",1000)

my_account.deposit(500)
print("Current balance:",my_account.get_balance())



#Task 6:Name Mangling

class BankAccount:
    def __init__(self,account_holder,initial_balance):
        self.account_holder=account_holder
        self.__balance=initial_balance

    def get_balance(self): 
        return self.__balance
    def deposite(self,amount):
        self.__balance=self.__balance+amount
        print("New balance:",self.__balance)
my_account=BankAccount("Alice",1000)
my_account.deposite(500)

print("Current balance:",my_account.get_balance())
print("Mangled balance:",my_account._BankAccount__balance)









class person:
    def testing(self):
        print("testing function called...")


p1=person()
p1.name="mayuri"

p1.testing()



