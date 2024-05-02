import socket

# Sunucuya bağlan
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4337))

# Tahmin için 5 hakkı tanımla
hak = 5

while hak > 0:
    gizli_kelime = client_socket.recv(1024).decode()
    print("Sunucudan gelen gizli kelime:", gizli_kelime)
    
    tahmin_edildi = False  # Tahminin doğru olup olmadığını kontrol etmek için
    
    while not tahmin_edildi:
        tahmin = input("Tahmininizi girin: ").upper()
        client_socket.send(tahmin.encode())
        cevap = client_socket.recv(1024).decode()
        print("Sunucudan gelen cevap:", cevap)
        
        if cevap == "Tebrikler":
            print("Doğru kelimeyi buldunuz!")
            tahmin_edildi = True  # Doğru tahmin yapıldı, iç döngüden çık
            break
        elif cevap == " Bilemediniz":
            print("Doğru kelimeyi bulamadınız.")
            tahmin_edildi = True  # Hakkı tükendi veya yanlış tahmin, iç döngüden çık
            break
        
    if cevap == "Tebrikler" or cevap == " Bilemediniz":
        break  # Dış döngüden çık
        
    hak -= 1

# Eğer tüm haklar kullanıldıysa ve doğru kelime bulunamadıysa
if hak == 0 and cevap == " Bilemediniz":
    print("5 tahmin hakkınızı kullandınız ve doğru kelimeyi bulamadınız.")
    
# Bağlantıyı kapat
client_socket.close()
