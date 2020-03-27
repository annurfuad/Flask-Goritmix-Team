from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Department, Role

class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    def enabled_department():
        return Department.query.all()

    def enabled_role():
        return Role.query.all()


    department = QuerySelectField(query_factory=enabled_department,
                                  get_label="name")
    role = QuerySelectField(query_factory=enabled_role,
                            get_label="name")
    submit = SubmitField('Submit')