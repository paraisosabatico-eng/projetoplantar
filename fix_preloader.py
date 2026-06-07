import sys

file_path = 'index.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
except FileNotFoundError:
    print(f"Error: {file_path} not found.")
    sys.exit(1)

# Replace the img.src path and add onerror handler
target_block = """            img.onload = function () {
                loaded++;
                bar.style.width = ((loaded / TOTAL) * 100) + '%';

                if (loaded === TOTAL) {
                    sizeCanvas();
                    draw();
                    initScroll();
                    // Esconde o loader
                    requestAnimationFrame(() => {
                        loader.classList.add('hidden');
                        setTimeout(() => loader.remove(), 700);
                    });
                }
            };"""

new_block = """            img.onload = function () {
                loaded++;
                bar.style.width = ((loaded / TOTAL) * 100) + '%';

                if (loaded === TOTAL) {
                    sizeCanvas();
                    draw();
                    initScroll();
                    // Esconde o loader
                    requestAnimationFrame(() => {
                        loader.classList.add('hidden');
                        setTimeout(() => loader.remove(), 700);
                    });
                }
            };
            
            img.onerror = function () {
                loaded++; // Continua mesmo com erro para não travar o site
                bar.style.width = ((loaded / TOTAL) * 100) + '%';
                if (loaded === TOTAL) {
                    sizeCanvas();
                    draw();
                    initScroll();
                    requestAnimationFrame(() => {
                        loader.classList.add('hidden');
                        setTimeout(() => loader.remove(), 700);
                    });
                }
            };"""

if target_block in html:
    html = html.replace(target_block, new_block)
else:
    print("Could not find onload block")

# Replace absolute path with relative path
if "'/projetoplantar/Jpeg Hero Web/Timeline 1_000'" in html:
    html = html.replace("'/projetoplantar/Jpeg Hero Web/Timeline 1_000'", "'./Jpeg Hero Web/Timeline 1_000'")
else:
    print("Could not find image src path")

# Also fix the img tags I just added in Dobra 3 that might need relative paths instead of absolute
# Well, they are already `src="assets/images/..."` so they are relative!

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixed preloader.")
