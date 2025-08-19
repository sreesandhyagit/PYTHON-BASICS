"""
def Fun():
    def nf():
        print("Hi")
    nf()
    print("Outer function")

Fun()
"""
"""
def Fun():
    course="python"
    def nf():        
        print(course)
        print("Hi")
    nf()
    print("Outer function")

Fun()
"""
def Fun():
    course="python"
    def nf():    
        nonlocal course
        course=course+"Full Stack"    
        print(course)
        print("Hi")
    nf()
    print("Outer function")
    print(course)

Fun()