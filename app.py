class USER:
    def __init__(self, accno,pin):
        self.accno = accno
        self.pin = pin
        self.balance=0
        self.history = []
class ADMIN:
    def __init__(self,atmn):
        self.atmn=atmn
        self.balance=0
        self.money=[0,0,0,0]