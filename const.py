class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


a1= B()    
