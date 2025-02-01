# There is a certain four digit number (6714) that when you subtract the numbers in a decending order
# to the one from the ascending order, it gives the number it self. And for any 4 digit number if you put under the same function,
# and keep doing it the number you get, it would eventually gets you Keprekae's constant

def shuffle(number):
    if len(str(number)) != 4: # The length of the number must be four
        print("please in put a four digit number")
        # return shuffle() # The length of the number must be four this is a clear oversight
    else:
        list = []
        list2 = [] 
        digit = 1  # I needed to predefine the digit value
        while number > 0: # putting digit here causes an extra zero to be added to the list
            digit = number % 10
            number = number // 10
            list.append(digit)
            list.sort()
        print(list)
        num1 = 0
        num2 = 0   
       
        for i in range(len(list)): # list can not be interpreted as an integer
           num1 = num1 + 10**(len(list)-i-1)*(list[i])
        print(num1)
        list2 = list[::-1]
        for i in range(len(list2)):
            num2 = num2 + 10**(len(list)-i-1)*(list2[i])
        print(num2)
        diff = num2 - num1
        if diff != 6174:
            print(diff)
            return shuffle(diff)
        else:
            print(diff)

         
         
shuffle(1334)