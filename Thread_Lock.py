import threading

counter = 0
lock = threading.Lock()


def increment():
  global counter
  for _ in range(100_000):
    # Acquire lock before modifying shared state
    with lock:
      counter += 1


threads = [threading.Thread(target=increment) for _ in range(5)]

for t in threads:
  t.start()

for t in threads:
  t.join()

print(f"Final counter value: {counter}")  # Always 500000