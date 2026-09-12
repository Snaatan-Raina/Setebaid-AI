import subprocess
import time

result = subprocess.run(
    ["say", "-v", "?"],
    capture_output=True,
    text=True
)

for line in result.stdout.splitlines():
    voice_name = line.split()[0]

    print(f"Now speaking: {voice_name}")

    subprocess.run([
        "say",
        "-v", voice_name,
        f"Hello. This is {voice_name} speakingggg."
    ])
    time.sleep(0.1)