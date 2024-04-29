import socket

HOST = "127.0.0.1"  # Yerel ana bilgisayar
PORT = 4337  # Sunucu port numarası

# Soket bağlantısı kurun
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    # Sunucudan mesaj alın
    mesaj = client_socket.recv(1024).decode()
    print(mesaj)

    # Tahmini girin
    tahmin = input("Tahmininiz: ")
    client_socket.send(tahmin.encode())

    # Sonucu kontrol edin
    sonuc_mesaji = client_socket.recv(1024).decode()
    print(sonuc_mesaji)

    # Oyun bittiyse döngüyü sonlandırın
    if sonuc_mesaji.startswith("Tebrikler!") or sonuc_mesaji.startswith("Bilemediniz"):
        break

# Bağlantıyı kapatın
client_socket.close()
