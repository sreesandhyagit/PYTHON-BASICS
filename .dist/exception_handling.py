# a=12
# b=2
# print(a/b)
# print("Completed")

# """
# a=12
# b=0
# print(a/b)
# print("Completed")
# """

# a=12
# b=0
# try:
#     print(a/b)
# except Exception:
#     print("Cannot divide by zero")
# print("Completed")

# a=12
# b=0
# try:
#     print(a/b)
# except:
#     print("Cannot divide by zero")    
# print("Completed")

# """
# a=12
# b=0
# print(a/c)
# print("Completed")
# """
# a=12
# b=0
# try:
#     print(a/c)
# except:
#     print("Cannot divide by zero")    
# print("Completed")

# """
# a=12
# b=0
# print(a/"Python")
# print("Completed")
# """
# a=12
# b=0
# try:
#     print(a/"Python")
# except:
#     print("Cannot divide by zero")    
# print("Completed")


# a=12
# b=0
# try:
#     print(a/"Python")
# except Exception as e:
#     print(e)  
# print("Completed")

# a=12
# b=0
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except NameError:
#     print("Please provide value")
# except TypeError:
#     print("Please provide integer value")
# except Exception as error:
#     print("Error :",error)
    
# print("Completed")

# a=12
# b=2
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except NameError:
#     print("Please provide value")
# except TypeError:
#     print("Please provide integer value")
# except Exception as error:
#     print("Error :",error)
# else:
#     print("Program executed..No error raised")
    
# print("Completed")

# a=12
# b=0
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except NameError:
#     print("Please provide value")
# except TypeError:
#     print("Please provide integer value")
# except Exception as error:
#     print("Error :",error)
# else:
#     print("Program executed..No error raised")
# finally:
#     print("Completed")

balance = 0
try:
    if balance<=0:
        print("Withdrawal amount")
        raise ValueError 
except ValueError:
    print("Invalid Balance Amount")