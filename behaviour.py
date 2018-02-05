import basebehavior.behaviorimplementation


class Mymainbehavior_x(basebehavior.behaviorimplementation.BehaviorImplementation):
    '''this is a behavior implementation template'''
    #this implementation should not define an __init__ !!!
    def implementation_init(self):
        #CALLED ONCE
        #define list of sub-behavior here
        self.createSubbehavior()
        self.startMySubbehavior = False
        self.selected_behaviors = [('mySubBehavior', "self.startMySubbehavior == True")]
        self.state = 'idle'
    
    def createSubbehavior(self):
        self.startMySubbehavior = False
        self.mySubBehavior = self.ab.mysubbehavior({})

    def implementation_update(self):
        #CALLED at 10Hz
        #check what behaviors have failed or finished and do other things when something has failed 
        if self.state == 'idle':
            self.startMySubbehavior = True
            self.state = 'runningMySubbehavior'
            print "starting my subbehavior.."
        elif self.mySubBehavior.is_failed():
            print self.mySubBehavior.get_failure_reason()
            self.createSubbehavior()
            print "my subbehavior failed"
            self.state = 'idle'
[mybehaviour]
description = "It does things you can't even dream of"
postcondition = False

[mysubbehaviour]
description = "It fixes the main behaviour"
postcondition = False

