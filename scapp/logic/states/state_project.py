#coding:utf-8
__author__ = 'Johnny'
#项目审批
from states import State
from scapp.models import OA_Reimbursement,OA_Project,OA_Org
from scapp import db
from scapp.config import logger

class State_Project(State):

    #审批通过
    def approval_success(self,id,cur_user):

        reim=OA_Reimbursement.query.filter_by(id=id)
        project_tag=False

        project=OA_Project.query.filter_by(id=reim.approval)
        p_project_id=project.p_project_id
        #循环取得父项目
        while p_project_id is not None:
            p_project=OA_Project.query.filter_by(id=p_project_id)
            #审批人不同时退出，同时审批类型依然是项目
            if p_project.manager_id != cur_user.id:
                approval=p_project.id
                project_tag=True
                reim.approval_type=2
                break
            p_project_id=p_project.p_project_id

        #当没有父项时向上查找部门
        if p_project_id is None and not project_tag:
            p_org_id=project.p_org_id
            while p_org_id is not None:
                p_org=OA_Org.query.filter_by(id=p_org_id)
                #审批人不同时退出，同时审批类型为部门审批
                if p_org.manager != cur_user.id:
                    approval=p_org.id
                    reim.approval_type=1
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
