class User():
    def __init__(self, user_name, user_id):
        self.user = user_name
        self.id = user_id
        self.followers = 0
        self.following = 0
    

    def follow(self,user):
        user.followers +=1
        self.following +=1

user = User("user_1", 17)
user2 = User("user_2",18)
user.follow(user2)
print(user.followers)
print(user.following)
print(user2.followers)
print(user2.following)


