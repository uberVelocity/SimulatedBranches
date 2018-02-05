import basebehavior.behaviorimplementation
import random

class Mysubbehavior_x(basebehavior.behaviorimplementation.BehaviorImplementation):

    def implementation_init(self):
        #initialize counter to 0
        self.counter = 0

    def implementation_update(self):
        #print counter
        print self.counter
        #increment
        self.counter += 1
        if random.random() < 0.25:
            self.set_failed("random number was too small")
        if self.counter == 10:
            self.set_finished()