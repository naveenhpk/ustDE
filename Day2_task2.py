class Vehicle:
    def __init__(self,maxsp,mil,seatcap):
        self.maxsp=maxsp
        self.mil=mil
        self.seatcap = seatcap

    def fare(self,seatcap):
        fare=self.seatcap*100
        return fare

    # def display(self):
    #     print("Millage",self.mil)
    #     print("Maximum Speed",self.maxsp)


class Bus(Vehicle):
    def __init__(self,maxsp,mil):
        super().__init__(self,maxsp,mil,seatcap=50)

    def fare(self):
        basefare=super.fare()
        self.totalfare=basefare+(basefare*0.1)
        return totalfare


    # def display(self):
    #     # super.display()
    #     print("Total fare",self.totalfare)


B=Bus(80,70)
print(B.fare())
# print()

