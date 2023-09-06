# try:
#     file_data = open("nova.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
#     # print(a_dict["nothing"])
# except KeyError as error_message:
#     print(f"the key {error_message} doesnot exits")
# except FileNotFoundError:
#     file_data = open("nova.txt","w")
#     file_data.write("something")
# else:
#     print("this is else")
#     content = file_data.read()
#     print(content)
# finally:
#     print("this is finally")
#     file_data.close()


## raise
# height = float(input("enter height : "))
# weight = int(input("enter weight : "))
# if height > 3:
#     raise ValueError("human height should not be over 3 meter")
# bmi = weight /height ** 2
# print(bmi)


# # coding challenge_1
# fruits = ["Apple", "Orange","Pear"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruitpie")
#     else:
#         print(fruit + "pie")

# make_pie(4)



facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:    
        print(post["Likes"])
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass



print(total_likes)