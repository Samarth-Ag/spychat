class  parent:
    count=10

    def __init__(self):

        print "calling constructor"



    def hi(self):
        #self.count=0
        self.count+=5
        print self.count




y=parent()
y.hi()
print y.count

