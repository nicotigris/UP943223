import pytest
from app import app, db, Project, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_project(client):
    response = client.post('/create_project', data=dict(
        name='Test Project',
        description='Test Description',
        deadline='2022-12-31'
    ))
    assert response.status_code == 302  # Redirect to index

def test_assign_task(client):
    client.post('/create_project', data=dict(
        name='Test Project',
        description='Test Description',
        deadline='2022-12-31'
    ))
    response = client.post('/assign_task/1', data=dict(
        name='Test Task',
        status='Incomplete'
    ))
    assert response.status_code == 302  # Redirect to index
