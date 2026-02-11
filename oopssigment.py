class Learner:

    def __init__(self,fullname,course,age,Feespaid):
        self.fullname = fullname
        self.course = course
        self.age = age
        self.Feespaid = Feespaid


    def values(self):
        print("Honesty and Transparency")



    def set(self):
        print("Firefox Lab")



learner1 = Learner("Caled Gero","MIT",17,43000)
print(learner1.fullname,learner1.course,learner1.age,learner1.Feespaid)
learner2 = Learner("Carson Okumi","CyberSecurity",21,89000)
print(learner2.fullname,learner2.course,learner1.age,learner2.Feespaid)
learner3 = Learner("Victor Senior","System Review",23,23900)
print(learner1.fullname,learner3.course,learner3.age,learner3.Feespaid)
