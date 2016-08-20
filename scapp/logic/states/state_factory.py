__author__ = 'Johnny'
from states import State
from state_project import State_Project
from state_org import State_Org
from state_finance import State_Finance
from state_payment import State_Payment

class State_Factory():

    def __init__(self,state_type):
        if state_type=='2':
            self.cur_state=State_Project()
        elif state_type=='1':
            self.cur_state=State_Org()
        elif state_type=='3':
            self.cur_state=State_Finance()
        else:
            self.cur_state=State_Payment()