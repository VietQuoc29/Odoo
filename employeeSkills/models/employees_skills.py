# from odoo import models, fields, api
# from odoo.exceptions import UserError

# class EmployeeSkill(models.Model):
#     _name = 'employee.skills'
#     _description = 'Employee Skills'

#     name = fields.Char(string="Skill Name", required=True)
#     employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
#     is_critical = fields.Boolean(string="Critical Skill", default=False)

#     def send_critical_skill_email(self):
#         """Send email to HR if skill is marked 'critical'."""
#         if not self.is_critical:
#             raise UserError("This skill is not marked as critical!")

#         mail_template = self.env.ref('data\email_template.xml')
#         if mail_template:
#             mail_template.sudo().send_mail(self.id, force_send=True)
#         else:
#             raise UserError("Email template not found!")
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class EmployeeSkill(Base):
    __tablename__ = "employee_skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey("hr_employee.id"), nullable=False)
    is_critical = Column(Boolean, default=False)

    employee = relationship("Employee")
