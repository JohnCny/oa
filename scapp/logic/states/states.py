#coding:utf-8
__author__ = 'Johnny'


class State():

    def __init__(self):
        None

    def __init__(self,reim_id):
        if reim_id=='1':
            cur_state=Project_State()

    #审批通过
    def approval_success(self,id,cur_user):
        return
    #审批拒绝
    def approval_deny(self,id,cur_user,reason):
        return
    #审批退回
    def approval_retreat(self,id,cur_user,reason):
        return



