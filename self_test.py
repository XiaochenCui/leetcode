class SelfTest(object):
    def __init__(self, name):
        self.name = name
    def showself(self):
        print("self:%s"%self)
        print("self:{}".format(self))
    def display(self):
        self.showself()
        print("name:{}".format(self.name))

st = SelfTest("hello")
st.display()
print("%X"%(id(st)))
print("{}".format(id(st)))