import socket
import random

# Tahmin edilecek kelimeler
kelimeler = ["fren", "cips", "priz", "bluz", "roka", "üzüm", "dize", "sert", "adil", "tarz"]

# Doğru tahmini kontrol et
def kontrol(tahmin):
    if tahmin == kelime:
        print("Tebrikler")
    else:
        print("Bilemediniz")

# Sunucu soketini oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 4337))
server_socket.listen(1)

print("Sunucu başlatıldı. İstemci bekleniyor...")

# Bağlantıyı kabul et
client_socket, client_address = server_socket.accept()
print("İstemci bağlandı:", client_address)

# Rastgele kelime seç
kelime = random.choice(kelimeler)
kelime = kelime.upper()
print("Doğru kelime:", kelime)

# Sadece ilk harfi gönder (büyük harfle)
ilk_harf_goster = kelime[0].upper() + "*" * (len(kelime) - 1)
client_socket.send(ilk_harf_goster.encode())

# Tahmin için 5 hakkı tanımla
hak = 5

while hak > 0:
    tahmin = client_socket.recv(1024).decode().lower()
    tahmin = tahmin.upper()
    print("İstemcinin tahmini:", tahmin)
    
    if len(tahmin) != len(kelime):
        client_socket.send("Lütfen 4 harfli bir kelime giriniz.".encode())
        continue
    
    cevap = ""
    for i in range(len(kelime)):
        if tahmin[i] == kelime[i]:
            cevap += tahmin[i].upper()
        elif tahmin[i] in kelime:
            cevap += tahmin[i].lower()
        else:
            cevap += "*"
    if hak==1 and cevap.upper()!=kelime.upper():
        client_socket.send(f"Bilemediniz maalesef, Tahmin edilmesi gereken kelime: {kelime}".encode())
        break
    
    if cevap.upper() == kelime.upper():
        client_socket.send(f"Tebrikler, oyunu kazandınız!!".encode())
        break
    else:
        client_socket.send(cevap.encode())
        hak -= 1

# Bağlantıyı kapat
client_socket.close()
server_socket.close()
