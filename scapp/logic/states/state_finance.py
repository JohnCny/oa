# coding:utf-8
__author__ = 'Johnny'
#财务审批
from states import State
from scapp.models import OA_Reimbursement,OA_Project,OA_Org
from scapp import db
from scapp.config import logger

class State_Finance(State):

   #审批通过
    def approval_success(self,id,cur_user):

        reim=OA_Reimbursement.query.filter_by(id=id)

        reim.approval_type='4'
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