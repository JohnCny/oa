#coding:utf-8
__author__ = 'Johnny'

from scapp.models import OA_Reimbursement
from scapp.logic import State_Factory
from scapp.config import PER_PAGE
from scapp.logic.constant.query_sql import QUERY_SUM_AMOUNT_BY_USER
from scapp import db

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

        approval_paged=approval_project.union(approval_org).paginate(page, per_page = PER_PAGE)

        return approval_paged

    #获取审批清单，按用户分组，统计总额
    def get_sum_amount_by_create_user(self,approval_user):
        sql=QUERY_SUM_AMOUNT_BY_USER%(approval_user.id,approval_user.id)
        sum_amount_approval=db.session.execute(sql)
        return sum_amount_approval

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


