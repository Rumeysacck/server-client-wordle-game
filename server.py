import socket
import threading

HOST = "127.0.0.1"  # Yerel ana bilgisayar
PORT = 4337  # Sunucu port numarası

# Kelimeyi ve kalan hak sayısını tanımlayın
kelime = "KALP"
kalan_hak = 5

def handle_client(client_socket):
    global kelime, kalan_hak

    # Kelimeyi yıldızlarla gösterin
    gizli_kelime = ""
    for harf in kelime:
        gizli_kelime += "*"

    while kalan_hak > 0:
        # Gizli kelimeyi ve kalan hakkı gönderin
        mesaj = f"{gizli_kelime} ({kalan_hak} hak kaldı)"
        client_socket.send(mesaj.encode())

        # Tahmini alın
        tahmin = client_socket.recv(1024).decode()

        # Tahmini kontrol edin
        dogru_harfler = 0
        for i, harf in enumerate(kelime):
            if harf == tahmin[i]:
                dogru_harfler += 1
                gizli_kelime = gizli_kelime[:i] + harf + gizli_kelime[i+1:]

        # Geri bildirim verin
        if doğru_harfler == len(kelime):
            mesaj = "Tebrikler! Doğru kelimeyi buldunuz."
            break
        else:
            yeni_gizli_kelime = ""
            for i, harf in enumerate(gizli_kelime):
                if harf == "*":
                    yeni_gizli_kelime += "*"
                elif harf in tahmin:
                    yeni_gizli_kelime += harf
                else:
                    yeni_gizli_kelime += harf.lower()
            gizli_kelime = yeni_gizli_kelime
            kalan_hak -= 1

    # Sonucu gönderin
    client_socket.send(mesaj.encode())
    client_socket.close()

# Sunucuyu başlatın
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

while True:
    # Yeni bir bağlantı kabul edin
    client_socket, address = server_socket.accept()
    print(f"Bağlantı kuruldu: {address}")

    # Her istemci için ayrı bir iş parçacığı oluşturun
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
