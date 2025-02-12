import pytest
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.api
class TestGreenAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.instance_id = os.getenv("GREEN_API_INSTANCE_ID")
        self.api_token = os.getenv("GREEN_API_TOKEN")
        self.test_phone = os.getenv("TEST_PHONE_NUMBER")
        self.base_url = f"https://api.green-api.com/waInstance{self.instance_id}"
        self.headers = {'Content-Type': 'application/json'}

    def test_send_message(self):
        """Тест отправки сообщения"""
        endpoint = f"{self.base_url}/sendMessage/{self.api_token}"
        message = f"Test message {datetime.now()}"
        payload = {
            "chatId": f"{self.test_phone}@c.us",
            "message": message
        }
        
        response = requests.post(endpoint, json=payload, headers=self.headers)
        assert response.status_code == 200
        response_data = response.json()
        assert "idMessage" in response_data
        return response_data["idMessage"]

    def test_get_chat_history(self):
        """Тест получения истории чата"""
        endpoint = f"{self.base_url}/getChatHistory/{self.api_token}"
        payload = {
            "chatId": f"{self.test_phone}@c.us",
            "count": 10
        }
        
        response = requests.post(endpoint, json=payload, headers=self.headers)
        assert response.status_code == 200
        messages = response.json()
        assert isinstance(messages, list)
        if messages:
            assert all(isinstance(msg, dict) for msg in messages)
            assert all("type" in msg for msg in messages)

    @pytest.mark.parametrize("invalid_chat_id", [
        "",
        "invalid_format",
        "@c.us",
        "123"
    ])
    def test_send_message_invalid_chat_id(self, invalid_chat_id):
        """Тест отправки сообщения с неверным форматом chatId"""
        endpoint = f"{self.base_url}/sendMessage/{self.api_token}"
        payload = {
            "chatId": invalid_chat_id,
            "message": "Test message"
        }
        
        response = requests.post(endpoint, json=payload, headers=self.headers)
        assert response.status_code in [400, 401, 404]

    def test_send_empty_message(self):
        """Тест отправки пустого сообщения"""
        endpoint = f"{self.base_url}/sendMessage/{self.api_token}"
        payload = {
            "chatId": f"{self.test_phone}@c.us",
            "message": ""
        }
        
        response = requests.post(endpoint, json=payload, headers=self.headers)
        assert response.status_code in [400, 401, 404]
