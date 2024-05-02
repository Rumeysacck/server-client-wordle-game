import socket

# Sunucunun IP adresi ve port numarası
HOST = '127.0.0.1'
PORT = 4337
# Ana kod akışı
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Sunucuya bağlandı.")
    
    while True:
        data = client_socket.recv(1024).decode()
        
        if not data:
            break
        print(data)

        if "Tebrikler" in data or "Bitti" in data:
            break

        guess = input("Tahmin: ")
        client_socket.sendall(guess.encode())
        # bunu yazdıktan sonra sunucudan cevap bekleyeceğiz doğal olarak


print("Oyun bitti.")