# my_file =open("sample_file.txt","w")
# my_file.write("Hello Developer")
# my_file.close()

# my_file =open("sample_file1.txt","a")
# my_file.write("Hello Sreesandhya")
# my_file.close()

# with open("Sample_file2.txt","w") as my_file:
#     my_file.write("Python is a high level programming language")
# # my_file.write("Hi") #this will make error

# with open("Sample_file3.txt","a") as my_file:
#     my_file.write("Python is a high level programming language.\n")
#     my_file.write("Hi Sreesandhya")

# with open("Sample_file3.txt","r") as my_file:
#     content = my_file.read()
#     print(content)

# with open("Car.jpg","rb") as my_file:
#     content = my_file.read()

# with open("new_car_image.jpg","wb") as my_file:
#     my_file.write(content)

with open("Sample_audio.mp3","rb") as my_file:
    content = my_file.read()

with open("new_sample_audio.mp3","wb") as my_file:
    my_file.write(content)