import socket

def main():
    localIP = "127.0.0.1"
    localPort = 9997
    buffer_size = 1024

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((localIP, localPort))
    print(f"[UDP SERVER] Server up and listening on {localIP}:{localPort}")

    try:
        while True:
            data, addr = serverSocket.recvfrom(buffer_size) 
            if not data:
                print("[UDP SERVER] Received empty packet, ignoring.")
                continue
            pesan = data.decode("utf-8", errors="replace")
            ip_client, port_client = addr
            print("-" * 50)
            print(f"[RECEIVED] From {ip_client}:{port_client}")
            print(f"[MESSAGE ] {pesan}")
            print("-" * 50)

            reply = "Selamat datang di UDP server"
            serverSocket.sendto(reply.encode("utf-8"), addr)
            print(f"[SENT    ] To {ip_client}:{port_client} -> {reply}\n")
    except KeyboardInterrupt:
        print("\n[UDP SERVER] Stopping server (KeyboardInterrupt).")
    except Exception as e:
        print(f"[UDP SERVER] Error: {e}")
    finally:
        serverSocket.close()

if __name__ == "__main__":
    main()
