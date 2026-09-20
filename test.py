import subprocess
import time
import re

# Volume for the assistant's speech only (0.0 = silent, 1.0 = normal).
# This does NOT touch the Mac's system output volume.
SPEECH_VOLUME = 0

result = subprocess.run(
    ["say", "-v", "?"],
    capture_output=True,
    text=True
)

for line in result.stdout.splitlines():
    if not line.strip():
        continue

    # Voice name is everything before the locale code (e.g. "en_US")
    match = re.match(r"^(.+?)\s+[a-z]{2}_[A-Z]{2}\b", line)
    if not match:
        continue
    voice_name = match.group(1).strip()

    print(f"Now speaking: {voice_name}")

    subprocess.run([
        "say",
        "-v", voice_name,
        f"[[volm {SPEECH_VOLUME}]] Hello. This is {voice_name} speaking."
    ])
    # Wait a bit before moving on to the next voice
    time.sleep(1)


