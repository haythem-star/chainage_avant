from Fait import Fait
from Regle import Regle
from base_faits import Base_faits


class Data:
    bases_faits = []
    regles = []
    def __init__(self):
        file1 = open("file1.txt", "r")
        Lines = file1.readlines()

        count = 0
        num_regle=0
        print('Regles : ')
        for line in Lines:
            line = line.strip()
            count += 1
            if(line[0:1] == 'r'):
                print (line)
                num_regle += 1
                self.regles.append(Regle(line,num_regle))
            if(line[0:2] == 'BF'):
                self.bases_faits.append(Base_faits(line))
            if (line[0:3] == 'BUT'):
                self.but = line.split(' : ')[1]



        file1.close()

    def affiche_base_faits(self):
        numBF = 1
        for j in self.bases_faits:
            print('bases de faits '+ str(numBF)+':')
            numBF = numBF+1
            print('{', end='')
            for k in j.faits:
                print(k.fait,end=',')
            print('}')
        print('but à montrer : ')
        print(self.but)

    def chainage_avant(self,bool):
        logFile = open('logFile.txt','w')
        # nb_regle_exicutes = 0
        echec = False;
        while((not exist(self.bases_faits[0].faits,self.but)) or bool) and (len(self.regles) > 0) and (not echec):
            echec = True
            for i in self.regles:
                if(premisses_existes(self.bases_faits[0].faits,i.premisses)):
                    echec = False
                    add_conclusons_to_faits(self.bases_faits[0].faits,i.conclusions,i.num,logFile)
                    self.regles.remove(i)

        logFile.write('base de faits :\n')
        logFile.write('[')
        for h in self.bases_faits[0].faits:
            logFile.write('{'+h.fait+',explication : '+str(h.explication)+'}')
        logFile.write(']\n')
        if (not bool):
            logFile.write('but : '+self.but+'\n')
            if (exist(self.bases_faits[0].faits,self.but)):
                logFile.write('resultat : OK')
            else:
                logFile.write('resultat : echec')
        logFile.close()


def exist(t,s):
    for i in t:
        if(i.fait == s):
            return True
    return False

def premisses_existes(t,p):
    for i in p:
        diff = 0
        for j in t:
            if(j.fait == i):
                break
            diff +=1
            if (diff == len(t)):
                return False
    return True

def add_conclusons_to_faits(BF,c,num,f):
    for i in c:
        f.write(i+ ' est ajouté à la base de faits on execute la regle r'+str(num)+'\n')
        # print(i+ ' est ajouté à la base de faits on execute la regle r'+str(num))
        BF.append(Fait(i,num))
