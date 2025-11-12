import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 9997
    buffer_size = 4096

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        message = input("Enter message to send (UDP): ").strip()
        if not message:
            print("[UDP CLIENT] No message entered. Exiting.")
            return

        client.sendto(message.encode("utf-8"), (server_ip, server_port))
        print(f"[UDP CLIENT] Sent -> '{message}' to {server_ip}:{server_port}")

        client.settimeout(5.0)
        try:
            data, server = client.recvfrom(buffer_size)
            print(f"[UDP CLIENT] Reply from {server[0]}:{server[1]} -> {data.decode('utf-8', errors='replace')}")
        except socket.timeout:
            print("[UDP CLIENT] No reply received (timeout).")
    except Exception as e:
        print(f"[UDP CLIENT] Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
