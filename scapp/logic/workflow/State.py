__author__ = 'Johnny'



#状态基类
class State():

    def approve(self):
        return

    def deny(self):
        return

    def get_cur_state(self):
        #todo:获取当前状态
        cur_state=0
        return cur_state

    def get_next_state(self):
        next_state=0
        return next_state;

class PMStatus(State):
    def approve(self):
        #todo:取得下一个审批人,审批当前状态置为下一节点状态
        next_approver=0
        cur_state=0
        result=True
        return result

    def deny(self):
        #todo:状态回到前一节点，标志为退回件

        result=True
        return result