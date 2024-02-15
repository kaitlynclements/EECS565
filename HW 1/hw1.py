# test565hw1.py

'''
Author: Kaitlyn Clements
KUID: 3072622
Course: EECS 565
Assignment: HW1
Due: Saturday 02/10 11:59PM
Description: You will get familiar with the attacks for guessing passwords. Alice sets a password for her account. 
Now you should crack her password with different settings. Please write the programs to achieve the brute force attack and get Alice's password. 
You need to call the Check(string) function to check if you found the correct answer. 
'''

import hashlib
import itertools
import time

def check(target, guessed_password, task): # Change the hash
    myhash = hashlib.md5(guessed_password.encode()).hexdigest()
    if target == myhash:
        print(f"Task {task}: Success! Password is: ", guessed_password)
        return True
    else:
        return False
    
# Task 1: The hash value of her password by MD5 is 94d9e03c11395841301a7aee967864ec. 
# You know the password is a length of 14. (The password can be combined with A-Z, a-z, or 0-9)
def task1():
    target = "94d9e03c11395841301a7aee967864ec"
    p_len = 14
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    start_time = time.time()
    for combo in itertools.product(chars, repeat=p_len):
        password = ''.join(combo)
        if check(target, password, 1) == True:
            end_time = time.time() # Stop measuring time
            test_time = end_time - start_time
            print("Time to crack: ", test_time, "seconds")

# Task 2: The hash value of her password by MD5 is f593def02f37f3a6d57bcbc9480a3316.
# You know the specific password format: <4-UPPER CASE LETTER><3-DIGIT-NUMBER><4-SMALLER CASE LETTER>
# e.g., XYEX234ascf
def task2():
    target = "f593def02f37f3a6d57bcbc9480a3316"
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = upper.lower()
    digits = '0123456789'

    start_time = time.time()
    for u in itertools.product(upper, repeat=4):
        for digit in itertools.product(digits, repeat=3):
            for l in itertools.product(lower, repeat=4):
                password = ''.join(u) + ''.join(digit) + ''.join(l)
                if check(target, password, 2) == True:
                    end_time = time.time()
                    test_time = end_time - start_time
                    return(print("Time to crack: ", test_time, "seconds"))

# Task 3: The hash value of her password by MD5 is bfb2c12706757b8324368de6a365338b.
# You know the specific password format: the length is 11 and it includes 7 upper case letters
# and the number "1234". But you don't know the position of "1234"
def task3():
    target = "bfb2c12706757b8324368de6a365338b"
    p_len = 11
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '1234'

    start_time = time.time()
    for u in itertools.combinations_with_replacement(upper, 7):
        for x in range(8):
            for digit in itertools.permutations(digits):
                password = ''.join(u[:x]) + ''.join(digit) + ''.join(u[x:])
                if check(target, password, 3) == True:
                    end_time = time.time()
                    test_time = end_time - start_time
                    return(print("Time to crack: ", test_time, "seconds"))




#print(task1())
task2()
print()
task3()
