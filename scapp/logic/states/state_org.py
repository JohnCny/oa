# coding:utf-8
__author__ = 'Johnny'
#部门审批
from states import State
from scapp.models import OA_Reimbursement,OA_Org
from scapp import db
from scapp.config import logger

class State_Org(State):

    #审批通过
    def approval_success(self,id,cur_user):

        reim=OA_Reimbursement.query.filter_by(id=id)
        org=OA_Org.query.filter_by(reim.approval)
        p_org_id=org.pId

        #向上查找父机构
        while p_org_id is not None:
            p_org=OA_Org.query.filter_by(id=p_org_id)
            #审批人不同时退出，同时审批类型为部门审批
            if p_org.manager != cur_user.id:
                approval=p_org.id
                break

            p_org_id=p_org.pId

        reim.approval=approval
        try:
            db.session.commit()
            return True
        except Exception, e:
            # 回滚
            db.session.rollback()
            logger.exception(e.message)
            return False

    #审批拒绝
    def approval_deny(self,id,cur_user,reason):
        reim=OA_Reimbursement.query.filter_by(id=id)
        reim.is_refuse = '1'
        reim.fail_reason = reason

        try:
            db.session.commit()
            return True
        except Exception, e:
            # 回滚
            db.session.rollback()
            logger.exception(e.message)
            return False

    #审批退回
    def approval_retreat(self,id,cur_user,reason):
        reim=OA_Reimbursement.query.filter_by(id=id)
        reim.is_retreat = '1'
        reim.approval=reim.project_id
        reim.approval_type= '0'
        reim.fail_reason = reason

        try:
            db.session.commit()
            return True
        except Exception, e:
            # 回滚
            db.session.rollback()
            logger.exception(e.message)
            return False