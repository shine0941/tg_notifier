import requests
import os

class TelegramNotifier:
    def __init__(self, bot_token=None, chat_id=None):
        # 支援環境變數設定，方便部署
        self.bot_token = bot_token or os.getenv("TG_BOT_TOKEN")
        self.chat_id = chat_id or os.getenv("TG_CHAT_ID")
        if not self.bot_token or not self.chat_id:
            raise ValueError("Telegram bot token 或 chat_id 未設定")

    def send(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message}
        resp = requests.post(url, json=payload)
        if resp.status_code != 200:
            raise Exception(f"發送失敗: {resp.text}")
        return resp.json()