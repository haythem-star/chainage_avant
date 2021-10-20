from Fait import Fait


class Base_faits:
    faits = []
    def __init__(self,s):
        self.faits = []
        faits_s = s.split(' : ')[1].split(',')
        for i in faits_s:
            self.faits.append(Fait(i))
