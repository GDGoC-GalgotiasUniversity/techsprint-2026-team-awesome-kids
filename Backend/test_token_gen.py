from app.core.config import settings
from agora_token_builder import RtcTokenBuilder
import time

# Mock Settings manually if .env isn't loading in this script context
# Or ensure your .env is correct.
APP_ID = settings.AGORA_APP_ID
APP_CERTIFICATE = settings.AGORA_APP_CERTIFICATE
CHANNEL_NAME = "test_channel"
UID = 123456
EXPIRATION = 3600

def test_gen():
    if not APP_ID or not APP_CERTIFICATE:
        print("❌ Error: Missing AGORA_APP_ID or AGORA_APP_CERTIFICATE in .env")
        return

    print(f"🔹 App ID: {APP_ID}")
    print(f"🔹 Channel: {CHANNEL_NAME}")
    print(f"🔹 UID: {UID}")

    try:
        current_timestamp = int(time.time())
        expire_timestamp = current_timestamp + EXPIRATION
        
        token = RtcTokenBuilder.buildTokenWithUid(
            APP_ID, APP_CERTIFICATE, CHANNEL_NAME, UID, 1, expire_timestamp
        )
        print("\n✅ Token Generated Successfully:")
        print(token)
        print("\n👉 Copy this token for Step 2.")
    except Exception as e:
        print(f"\n❌ Generation Failed: {e}")

if __name__ == "__main__":
    test_gen()