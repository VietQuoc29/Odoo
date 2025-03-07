import pytest
from models.employee import Employee
from models.employee_skill import EmployeeSkill
from models.database import SessionLocal, init_db

@pytest.fixture(scope="module")
def session():
    init_db()
    session = SessionLocal()
    yield session
    session.close()

def test_create_employee_skill(session):
    emp = Employee(name="Jane Doe")
    session.add(emp)
    session.commit()

    skill = EmployeeSkill(name="Python", employee_id=emp.id, is_critical=True)
    session.add(skill)
    session.commit()

    assert skill.id is not None
    assert skill.name == "Python"
    assert skill.is_critical is True
    assert skill.employee_id == emp.id
