import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 6677

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f"[SERVER] Listening on {ip}:{port}")

    while True:
        client, address = server.accept()
        try:
            print(f"[+] Connection established from {address[0]}:{address[1]}")
            data = client.recv(1024).decode("utf-8")
            if not data:
                print("[SERVER] No data received.")
            else:
                print(f"[CLIENT] {data}")
                response = data.upper()
                client.send(response.encode("utf-8"))
                print(f"[SERVER] Sent back: {response}")
        except Exception as e:
            print(f"[SERVER] Error: {e}")
        finally:
            client.close()
            print("[SERVER] Connection closed\n" + "-" * 40)
