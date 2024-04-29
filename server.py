import socket

# Tahmin edilecek kelime
kelime = "KABE"

# Doğru tahmini kontrol et
def kontrol(tahmin):
    if tahmin == kelime:
        return "Tebrikler"
    else:
        return "Bilemediniz"

# Sunucu soketini oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 4337))
server_socket.listen(1)

print("Sunucu başlatıldı. İstemci bekleniyor...")

# Bağlantıyı kabul et
client_socket, client_address = server_socket.accept()
print("İstemci bağlandı:", client_address)

# Tahmin için 5 hakkı tanımla
hak = 5

while hak > 0:
    tahmin = client_socket.recv(1024).decode()
    print("İstemcinin tahmini:", tahmin)
    cevap = ""
    for i in range(len(kelime)):
        if tahmin[i] == kelime[i]:
            cevap += tahmin[i]
        elif tahmin[i] in kelime:
            cevap += tahmin[i].lower()
        else:
            cevap += "*"
    if cevap == kelime:
        client_socket.send("Tebrikler".encode())
        break
    else:
        client_socket.send(cevap.encode())
        hak -= 1
        if hak == 0:
            client_socket.send("  Bilemediniz".encode())

# Bağlantıyı kapat
client_socket.close()
server_socket.close()
