import basebehavior.behaviorimplementation
import random
import rospy

class Mysubbehavior_x(basebehavior.behaviorimplementation.behaviorImplementation):

    def implementation_init(self):
        self.counter = 0

    def implementation_update(self):
        self.counter += 1
        #adding memory to self, passing a dictionary that takes the value of counter with key 'counter'
        self.m.add_item("my_key", rospy.Time.now().to_sec(), {'counter' : self.counter})
        if random.random() < 0.25:
            self.set_failed("random number was too small")
        if self.counter == 10:
            self.set_finished()