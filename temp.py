

class Test():
    def __init__(self,name):
        self.username=name

    def __eq__(self,gg):
        if not isinstance(gg,Test):
            print("Invalid Instance!")
            return False
        else:
            print("good")
        return self.username==gg.username

a=Test("suho")
b=Test("suo")
if a==b:
    print("True")
else:
    print("False")
