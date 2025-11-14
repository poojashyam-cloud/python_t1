numberList = [10,501,22,37,100,999,87,351,2,3,9]
ansList = [] # Empty list

for num in numberList: # Iterate through each number
    # 0 and 1 is not a
    # prime number
    if num == 0 or num == 1:
        continue
    for i in range(2, num // 2 + 1):
        # If number is divisible by any
        # number (i) then it is not
        # a prime number
        if num % i == 0:
            break

    # If not divisible then it is
    # a prime number
    else:
        # if number is prime
        # then append to the list
        ansList.append(num)

# If list is non-empty then
# print th elements
if len(ansList):

    print("Prime Number : ", end="-> ")

    # printing the prime number
    # from the ansList
    for ans in ansList:
        print(ans, end=", ")

else:
    print("No any number from the given list is Prime")