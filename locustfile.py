from locust import HttpUser, task, between

class SentinelUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def index(self):
        self.client.get("/")

    @task(3)
    def post_transaction(self):
        self.client.post("/transaction", json={
            "amount": 7500,
            "user_id": "user123",
            "merchant": "Amazon",
            "device_id": "iPhone14"
        })
