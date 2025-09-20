import pickle

student = {"Name":"Sreesandhya","Course":"Python","Batch":2}

with open("Student_Details.pkl","wb") as file:
    pickle.dump(student,file)

