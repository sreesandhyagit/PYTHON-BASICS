
"""
class Students:
    institute="OneTeam"
    def getDetails(self,n,c):
        self.name=n
        self.course=c
    
    def showDetails(self):
        print(f"Student Name : {self.name}")
        print("Course : ",self.course)

st1=Students()
st1.getDetails("Siva","Python")
st1.showDetails()
print(st1.institute)
"""
class Students:
    institute="OneTeam"
    def __init__(self,n,c):
        self.name=n
        self.course=c
    
    def showDetails(self):
        print(f"Student Name : {self.name}")
        print("Course : ",self.course)

st1=Students("Siva","Python")
st1.showDetails()
print(st1.institute)
