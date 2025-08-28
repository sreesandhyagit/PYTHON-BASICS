class Students:
    institute='OneTeam'

    # def get_details(self):
    #     print(self)
    #     self.name="Arjun"
    #     self.age=23

    def get_details(self,n,a):
        self.name=n
        self.age=a
    
    def display(self):
        print(f"Your name is {self.name} and you are {self.age} years old")
        

st1=Students()
st2=Students()

# print(st1.institute)
# print(st2.institute)

# st1.get_details()
# print(st1.name)
# print()

st1.get_details("Arjun",21)
st2.get_details("Anu",20)
# print(st1.name)
# print(st2.name)
st1.display()
st2.display()

