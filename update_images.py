import sys

file_path = 'pages/segunda-fase.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
except FileNotFoundError:
    print(f"Error: {file_path} not found.")
    sys.exit(1)

html = html.replace('textura_papel_organico_1780619777884.png', 'Fundo-Dobra-3-Desfoque v2.jpg')
html = html.replace('novo_titulo_1.png', 'E-se-estivermos-fazendo-a-pergunta-errada.png')
html = html.replace('doc_dobra3_montanha_1780617433197.png', 'Menino.jpg')
html = html.replace('doc_dobra3_cidades_1780617454941.png', 'Cidade.png')
html = html.replace('novo_titulo_2.png', 'Nós-sobreviveremos-ao-modelo-de-crescimento-que-construímos.png')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated image paths!")
