import http.server
import socketserver

# Define a porta em que o servidor irá escutar
port = 8000

# Define o manipulador de requisições
handler = http.server.SimpleHTTPRequestHandler

# Inicializa o servidor
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Servidor rodando na porta {port}")
    # Mantém o servidor em execução até que ele seja interrompido
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Se o usuário pressionar Ctrl + C, o servidor será interrompido
        print("Servidor interrompido pelo usuário")
