from app.core.config import settings
from agora_token_builder import RtcTokenBuilder
import time

# 1. Ensure these are correct!
APP_ID = settings.AGORA_APP_ID
APP_CERTIFICATE = settings.AGORA_APP_CERTIFICATE
CHANNEL_NAME = "test_channel" 

def generate_wildcard_token():
    # Use 0 for the UID to allow ANY user to join
    UID = 0 
    EXPIRATION = 3600

    current_timestamp = int(time.time())
    expire_timestamp = current_timestamp + EXPIRATION
    
    try:
        token = RtcTokenBuilder.buildTokenWithUid(
            APP_ID, APP_CERTIFICATE, CHANNEL_NAME, UID, 1, expire_timestamp
        )
        print("\n✅ NEW WILDCARD TOKEN (Copy this):")
        print(token)
        print(f"\n👉 Use Channel Name: {CHANNEL_NAME}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_wildcard_token()