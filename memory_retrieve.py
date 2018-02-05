import basebehavior.behaviorimplementation

class Mymainbehavior_x(basebehavior.behaviorimplementation.BehaviorImplementation):
    def implementation_init(self):
        self.createSubbehavior()
        self.startMySubbehavior = False
        self.selected_behaviors = [('mySubBehavior', "self.startMySubbehavior == True")]
        self.state = 'idle'
        self.last_recogtime = 0

    def createSubbehavior(self):
        self.startMySubbehavior = False
        self.mySubBehavior = self.ab.mysubbehavior({})

    def implementation_update(self):
        if self.state == 'idle':
            self.startMySubbehavior = True
            self.state = 'runningMySubbehavior'
            print "starting my subbehavior.."
        elif self.state == 'runningMySubbehavior':
            if self.mySubBehavior.is_finished():
                print "finished my subbehavior"
                self.createSubbehavior()
            elif self.mySubBehavior.is_failed():
                print self.mySubBehavior.get_failure_reason()
                self.createSubbehavior()
                print "my subbehavior failed"
                self.state = 'idle'
            else:
                if (self.m.n_occurs('my_key') > 0):
                    (recogtime, obs) = self.m.get_last_observation("my_key")
                if not obs == None and recogtime > self.last_recogtime:
                    self.last_recogtime = recogtime
                    print obs['counter']