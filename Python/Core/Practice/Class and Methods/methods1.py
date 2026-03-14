class Profile:

    def __init__(self,username):
        self.followers=0
        self.username=username

    def follow(self):
        print("Someone followed you ") # action when followed
        self.followers+=1              # followers increment

    def update_username(self,x):
        self.username=x

p1=Profile("Hey_Tarun") #old username

p1.follow()     #follow method called
print(p1.followers) #after calling followers

p1.update_username("Tarun") # updated username
print(p1.username)
