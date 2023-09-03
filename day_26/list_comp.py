# list comprehensions 

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# square_numbers = [ number*number for number in numbers]
# print(square_numbers)
# even_number = [numb for numb in numbers if numb%2 == 0]
# print(even_number)

with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

ansewer = [int(num) for num in file1_data if num in file2_data]
print(ansewer)