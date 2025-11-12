import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 6677

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip, port))
        print(f"[CLIENT] Connected to server {ip}:{port}")
        message = input("Enter message: ")
        if message:
            client.send(message.encode("utf-8"))
            response = client.recv(1024).decode("utf-8")
            print(f"[SERVER RESPONSE] {response}")
        else:
            print("[CLIENT] No message entered.")
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
    finally:
        client.close()
        print("[CLIENT] Connection closed")
