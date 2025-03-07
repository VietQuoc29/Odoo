import pytest
from models.employee import Employee
from models.database import SessionLocal, init_db

@pytest.fixture(scope="module")
def session():
    init_db()
    session = SessionLocal()
    yield session
    session.close()

def test_create_employee(session):
    emp = Employee(name="John Doe")
    session.add(emp)
    session.commit()
    
    assert emp.id is not None
    assert emp.name == "John Doe"
