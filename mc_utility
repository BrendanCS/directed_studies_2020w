#################### ham cheese production model ###################

## this model has productions that allow it to explore during learning

import ccm      
log=ccm.log()   

from ccm.lib.actr import *  

class MyEnvironment(ccm.Model):
    pass

#####
# create an act-r agent

class MyAgent(ACTR):
    
    focus=Buffer()

    production_time=0.02         # production parameter settings
    production_sd=0.10
    production_threshold=-20

    pm_new=PMNew(alpha=0.2)      # The new TD-inspired utility learning system

#### NOTE - this model uses an alternative way of writing chunks using a list instead of a dictionary form
#### so the order is what gives it meaning. This is just an alternative way of writing them, they work just the same

    def init():
        focus.set('state:engine_off goal:run_engine')

    def openDoor(focus='state:engine_off goal:run_engine'):  
    	print " "   
        print "Let start this engine!"          
        focus.set('state:engine_off action:start_car')             

    def sit(focus='state:engine_off action:start_car'):   
    	print " "       
        print "I'm going to start this car...."    
        focus.set('state:choose goal:run_engine action:unknown')
        											## following this the agent will choose to explore or not

## choose to explore different actions

    def explore(focus='state:choose goal:run_engine action:unknown'):
    	print " "       
        print "Let's explore..."   
        focus.set('state:explore goal:run_engine action:select')
 
    def exploreKey(focus='state:explore goal:run_engine action:select'):  
    	print " "        
        print "I'll turn the key"
        focus.set('state:make goal:run_engine action:turn_key')
        self.reward(0.0)    										# reward reset, no inherited reward

    def exploreReevaluate(focus='state:explore goal:run_engine action:select'):  
    	print " "     
        print "Going to reevaluate"
        focus.set('state:make goal:run_engine action:reevaluate')
        self.reward(0.0)  											# reward reset, no inherited rewardQ

## choose not to explore different ways

    def donotexplore(focus='state:choose ingrediant:ham varient:unknown'):
    	print " "          
        print "I am feeling rational in a narrow sort of way"    
        focus.set('state:donotexplore ingrediant:ham varient:select')
        self.reward(0.0)  # reward reset, no inherited reward

    def chooseKey(focus='state:make goal:run_engine action:turn_key'): # will inherit rewarded from ham
    	print " "         
        print "I will turn the key..."    
        focus.set('state:make goal:run_engine action:turnED_key')

    def chooseReevaluate(focus='state:make goal:run_engine action:reevaluate'): # will inherit rewared from parma_ham 
    	print " "        
        print "I will reevaluate..."    
        focus.set('state:make goal:run_engine action:reevaluatedED')

## resume car starting activity

    def Key(focus='state:make goal:run_engine action:turnED_key'):
    	print " "
        print "I have turnED the key"
        focus.set('state:engine_off goal:run_engine')
        self.reward(0.3)                                              

    def Reevaluate(focus='state:make goal:run_engine action:reevaluatED'):
    	print " "
        print "I have now reevaluatED ************"
        focus.set('state:engine_off goal:run_engine')
        self.reward(0.5)                                                 

    def CarStart(focus='state:on goal:in_progress'):
    	print " "
        print "I am making progress to starting this car"
        focus.set('state:engine_off goal:run_engine')
        self.reward(0.0)   # reset

                   

tim=MyAgent()                              
subway=MyEnvironment()                    
subway.agent=tim                          
ccm.log_everything(subway)                 
subway.run(3)                             
ccm.finished()                             
