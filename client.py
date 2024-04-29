import socket

# Sunucuya bağlan
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4337))

# Tahmin için 5 hakkı tanımla
hak = 5

while hak > 0:
    tahmin = input("Tahmininizi girin: ").upper()
    client_socket.send(tahmin.encode())
    cevap = client_socket.recv(1024).decode()
    print("Sunucudan gelen cevap:", cevap)
    if cevap == "Tebrikler" or cevap == "Bilemediniz":
        break
    hak -= 1

# Bağlantıyı kapat
client_socket.close()
