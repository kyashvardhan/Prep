# tests/test_tasks.py

import time
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_check_task():
    # Create a task with a 2-second duration.
    response = client.post("/tasks/", params={"duration": 2})
    assert response.status_code == 200
    task_id = response.json()["task_id"]
    
    # Initially, the task should be pending or started.
    status_response = client.get(f"/tasks/{task_id}")
    status = status_response.json()["status"]
    assert status in ["PENDING", "STARTED"]
    
    # Wait for task completion.
    time.sleep(3)
    final_response = client.get(f"/tasks/{task_id}")
    final_data = final_response.json()
    assert final_data["status"] == "SUCCESS"
    assert "Task completed" in final_data["result"]
