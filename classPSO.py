import math
import random

#case minimization 

global PSI #0.7 or 0.8
global CMAX #1.47 or 1.62


#class for the creation of a particle
class Particle:
    def __init__(self,x_init):
        self.location = []
        self.speed=[]
        self.best=[]
        self.neighboor = []
        self.best_neigboor = math.inf
        self.best_eval = math.inf
        for i in range(len(x_init)):
            self.location.append(x_init[i])
            self.speed.append(random.uniform(-1,1))

    def getEval(self,function):
        eval =  function(self.location)
        if eval > self.best_eval : 
            self.best_eval = eval
        return eval
    
    def new_position(self, limite):
        for i in range(len(self.location)):
            self.location[i] = self.location[i] + self.speed[i]
            if self.location[i] < limite[i]:
                self.location[i] = limite[i]
            if self.location[i] > limite[i]:
                self.location = limite[i]

    def new_speed(self):
        for i in range(len(self.location)):
            term1 = CMAX * random.random()*(self.best[i]-self.location[i])
            term2 = CMAX * random.random()*(self.best_neigboor[i]-self.location[i])
            self.speed[i] = PSI * self.speed[i] + term1 + term2

    def setBestNeigboor(self,loc, value):
        self.best_neigboor = value
        self.neighboor = loc

    
        

class PSO():
    def __init__(self,epocs, p_num, limit, x_init, function) :
        swarm = []
        for i in range(p_num):
            swarm.append(Particle(x_init[i]))
        count = 0
        global_best =  math.inf
        while count<epocs:
            for i in range(len(p_num)):
                swarm[i].getEval(function)
                if swarm[i].best < global_best:  # line to change for maximisation
                    best_position = swarm[i].location
                    for j in range(p_num):
                        swarm[j].setBestNeigboor(best_position, swarm[i].best)
            for i in range(p_num):
                swarm[i].new_speed()
                swarm[i].new_pisition(limit)
            count +=1
        print("Position : ", swarm[0].neighboor)
        print("value : ", swarm[0].best_neigboor)
        
