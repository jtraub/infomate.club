import socket
import time
import random

if __name__ == "__main__":
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(("postgres", 5432))
                print("Postgres had started")
                break
        except socket.error:
            print("Waiting for postgres")
            time.sleep(0.5 + (random.randint(0, 100) / 1000))
