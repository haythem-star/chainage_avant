class Regle:
    premisses = []
    conclusions = []
    def __init__(self,str,num):
        self.num = num
        regle = str.split('si')[1].strip()
        self.regle= regle
        self.premisses = regle.split(' alors ')[0].split(' et ')
        self.conclusions = regle.split(' alors ')[1].split(' et ')












