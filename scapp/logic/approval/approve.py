#coding:utf-8
__author__ = 'Johnny'

from scapp.models import OA_Reimbursement
from scapp.logic import State_Factory
from scapp.config import PER_PAGE

class Approve():
    #获取当前所属项目审批报销
    def get_approval_by_project(self,cur_user_id):
        query_sql="is_paid=0 and is_refuse=0 and approval_type=2  and approval in " \
                  "(select id from oa_project where manager_id="+str(cur_user_id)+" and version='2015') "

        approval=OA_Reimbursement.query.filter(query_sql)
        return approval

    def get_approval_by_org(self,cur_user_id):
        query_sql="is_paid=0 and approval_type=1 and org_id in " \
                  "(select id from oa_org where manager="+str(cur_user_id)+" and version='2015')"
        approval=OA_Reimbursement.query.filter(query_sql)
        return approval

    #获取审批清单
    def get_approval_by_user(self,cur_user,page,PER_PAGE=PER_PAGE):

        approval_project=self.get_approval_by_project(cur_user.id)
        approval_org=self.get_approval_by_org(cur_user.id)

        approval_project[0:0]=approval_org
        return approval_project

    # def get_approval_by_user_filter_cu(self,cur_user,create_user):

    #审批
    def do_approve(self,cur_user,id,approval_type,result,reason):

        cur_state=State_Factory(approval_type).cur_state

        #通过
        if result=='1':
            if cur_state.approval_success(id,cur_user):
                return True
            else:
                return False
        #拒绝
        elif result=='2':
            if cur_state.approval_deny(id,cur_user,reason):
                return True
            else:
                return False
        #退回
        else:
            if cur_state.approval_retreat(id,cur_user,reason):
                return True
            else:
                return False


