import os

LINE = "Stop trying to impress people who will forget your name by next year. Learn to code instead."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

with open("/output/entry.txt", "rb") as f:
    written = f.read()
assert written == LINE.encode("utf-8"), "output mismatch"
assert len(written) == 92, "output must be exactly 92 bytes"
print("wrote /output/entry.txt:", len(written), "bytes")
