import sys

file_path = 'pages/segunda-fase.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
except FileNotFoundError:
    print(f"Error: {file_path} not found.")
    sys.exit(1)

html = html.replace('"/projetoplantar/assets/', '"../assets/')
html = html.replace("'/projetoplantar/assets/", "'../assets/")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixed image paths in segunda-fase.html")
