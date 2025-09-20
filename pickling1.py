import pickle

with open("Student_Details.pkl","rb") as file:
    print(pickle.load(file))
    