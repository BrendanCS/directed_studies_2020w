#################### ham cheese production model ###################

# this is the simplest type of act-r model
# it uses only the production system and one buffer
# the buffer represents the focus of thought
# we call it the focus buffer but it is often called the goal buffer
# productions fire if they match the focus buffer
# each production changes the contents of focus buffer so a different production will fire on the next cycle


import ccm      
log=ccm.log()   

from ccm.lib.actr import *  

#####
# Python ACT-R requires an environment
# but in this case we will not be using anything in the environment
# so we 'pass' on putting things in there

class MyEnvironment(ccm.Model):
    pass

#####
# create an act-r agent

class MyAgent(ACTR):

    DMbuffer=Buffer()                    
    DM=Memory(DMbuffer)                   
    focus=Buffer()

    production_time=0.03         # production parameter settings
    production_sd=0.01
    production_threshold=-10

    pm_new=PMNew(alpha=0.2)      # The new TD-inspired utility learning system

## this is based on the ACT-R model "parma-ham"

    def init():
        DM.add('action1:turn_key')                  
        DM.add('action2:reevaluate')
        focus.set('buffer 1a')

    def startCar(focus='buffer 1a'):
        print "Trying to start car - WHAT SHOULD I DO?"
        focus.set('buffer 1')    # two matching conditions: functions "decision_1" & "decision_2"


    def decision_1a(focus='buffer 1'):   
    	print " "
    	print "Requesting action 1..."
        DM.request('action1:?')             
        focus.set('buffer 2')             

    def decision_1b(focus='buffer 2', DMbuffer='action1:?action1'): 
    	print " "     
        print action1        
        focus.set('buffer 1') 	# LOOP to buffer 1


    def decision_2a(focus='buffer 1'):
    	print " "
    	print "Requesting action 2..."
        DM.request('action2:?')             
        focus.set('buffer 3')
        self.reward(0.1)

    def decision_2b(focus='buffer 3', DMbuffer='action2:?action2'):
    	print " "
        print action2          
        focus.set('buffer 1') 	# LOOP to buffer 1
      


    def do_nothing(focus='buffer done'):
    	print "I'm done"	
        self.stop()


tim=MyAgent()                              
subway=MyEnvironment()                    
subway.agent=tim                          
ccm.log_everything(subway)                 

subway.run(20)     # run for 5 seconds to learn that param ham is more rewarding to use                              
ccm.finished()                             
