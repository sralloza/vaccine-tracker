from sys import stderr

import requests

from vaccine_tracker.config import settings


def notify_text(msg: str):
    for chat_id in settings.chat_ids:
        response = requests.post(
            f"https://api.telegram.org/bot{settings.bot_token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": msg,
                "parse_mode": "markdown",
                "disable_web_page_preview": True,
            },
        )
        if not response.ok:
            data = {"msg": msg, "chat_id": chat_id, "response_text": response.text}
            print(data, file=stderr)
            response.raise_for_status()
