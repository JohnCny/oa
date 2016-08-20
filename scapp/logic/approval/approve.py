__author__ = 'Johnny'

from scapp.models import OA_Project,OA_Org,OA_Reimbursement
from scapp.logic import State_Factory

class Approve():
    #获取当前所属项目审批报销
    def get_approval_by_project(self,projects):
        query_sql="is_paid=0 and approval_type=2 and version='2015' and approval in ("+projects+") "
        approval=OA_Reimbursement.query.filter(query_sql)
        return approval

    def get_approval_by_org(self,orgs):
        query_sql="is_paid=0 and and approval_type=1 and version='2015' and org_id in ("+orgs+")"
        approval=OA_Reimbursement.query.filter(query_sql)
        return approval

    #获取审批清单
    def get_approval_by_user(self,cur_user):
        in_charge_project=OA_Project.query.filter_by(manager_id=cur_user.id)
        in_charge_org=OA_Org.query.filter_by(manager=cur_user.id)

        approval_project=self.get_approval_by_project(in_charge_project)
        approval_org=self.get_approval_by_org(in_charge_org)

        return dict(approval_project,**approval_org)

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


