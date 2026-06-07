import sys

file_path = 'index.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
except FileNotFoundError:
    print(f"Error: {file_path} not found.")
    sys.exit(1)

# 1. Replace CSS
css_start = '        /* ──────────────────────────────────────────────\n           DOBRA 3 (BENTO BOX SÓLIDO - REFERÊNCIA)'
css_end_pattern = '        /* ──────────────────────────────────────────────\n           DOBRA 4 — POR QUE O PROJETO EXISTE'

css_new = """        /* ──────────────────────────────────────────────
           DOBRA 3 (NOVO LAYOUT ZIG-ZAG BENTO)
        ────────────────────────────────────────────── */
        .section-dobra-3 {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 8rem 2rem;
            gap: 4rem;
            overflow: hidden;
            background-color: #F3F4F0;
        }

        /* Fundo Paralax Wavy */
        .d3-bg-parallax {
            position: absolute;
            top: -10%;
            left: 0;
            width: 100%;
            height: 120%; /* Para o efeito parallax funcionar */
            object-fit: cover;
            z-index: 0;
        }

        .d3-content-wrapper {
            position: relative;
            z-index: 1;
            width: 100%;
            max-width: 80rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4rem;
        }

        .d3-title-img {
            width: 100%;
            max-width: 50rem;
            height: auto;
            margin: 0 auto;
            display: block;
        }

        .d3-grid-row {
            display: flex;
            width: 100%;
            gap: 2rem;
            align-items: stretch;
            min-height: 400px;
        }

        .d3-glass-box {
            flex: 1;
            background-color: rgba(255, 255, 255, 0.55);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.6);
            border-radius: 1.5rem;
            padding: 3rem;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05);
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .d3-text-content {
            font-size: 1.05rem;
            line-height: 1.6;
            color: #6B6B6B;
            text-align: justify;
        }

        .d3-text-highlight {
            color: #899702;
            font-weight: 700;
        }

        .d3-image-box {
            flex: 1;
            border-radius: 1.5rem;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05);
        }

        .d3-image-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.6s ease;
        }
        
        .d3-image-box:hover img {
            transform: scale(1.03);
        }

        @media (max-width: 1024px) {
            .d3-grid-row {
                flex-direction: column;
                min-height: auto;
            }
            .d3-grid-row.reverse-mobile {
                flex-direction: column-reverse; 
            }
            .d3-image-box {
                min-height: 300px;
            }
        }

        @media (max-width: 768px) {
            .section-dobra-3 {
                padding: 4rem 1.5rem;
                gap: 2.5rem;
            }
            .d3-content-wrapper {
                gap: 2.5rem;
            }
            .d3-glass-box {
                padding: 2rem;
            }
        }

"""

idx1 = html.find(css_start)
idx2 = html.find(css_end_pattern)

if idx1 != -1 and idx2 != -1:
    html = html[:idx1] + css_new + html[idx2:]
else:
    print("Failed to find CSS block")

# 2. Replace HTML
html_start = '    <!-- Dobra 3 -->\n    <section id="primeira-fase" class="section-dobra-3">'
html_end_pattern = '    <!-- ══════════════════════════════════════════════════\n         DOBRA 4 — POR QUE O PROJETO EXISTE'

html_new = """    <!-- Dobra 3 -->
    <section id="terceira-dobra" class="section-dobra-3">
        <!-- Background Wavy Paralax -->
        <!-- Substitua pelo nome correto da imagem de fundo orgânico enviada -->
        <img src="assets/images/textura_papel_organico_1780619777884.png" alt="Fundo Orgânico" class="d3-bg-parallax" id="dobra3-bg-parallax">

        <div class="d3-content-wrapper">
            
            <!-- Título Superior -->
            <!-- Substitua pelo nome correto da imagem do título "E SE ESTIVERMOS..." -->
            <img src="assets/images/novo_titulo_1.png" alt="E se estivermos fazendo a pergunta errada?" class="d3-title-img">

            <!-- Linha 1: Texto Esquerda / Imagem Direita (Menino) -->
            <div class="d3-grid-row reverse-mobile">
                <!-- Caixa de Vidro -->
                <div class="d3-glass-box">
                    <p class="d3-text-content">
                        Durante muito tempo ouvimos a mesma mensagem:<br>
                        <span class="d3-text-highlight">"Precisamos salvar o planeta."</span> Mas existe uma verdade incômoda que raramente aparece nas conversas. O planeta já provou que sobreviveu a meteoros e a eras glaciais. Nós não somos a primeira ameaça — e, longe disso, precisamos usar toda a nossa inteligência coletiva para decidir como queremos viver aqui, aceitando de uma vez por todas os limites físicos dessa nossa estadia.
                    </p>
                </div>
                <!-- Caixa de Imagem -->
                <div class="d3-image-box">
                    <!-- Substitua pelo nome correto da imagem do menino olhando para a cidade -->
                    <img src="assets/images/doc_dobra3_montanha_1780617433197.png" alt="Menino olhando para a cidade">
                </div>
            </div>

            <!-- Linha 2: Imagem Esquerda (Cidade) / Texto Direita -->
            <div class="d3-grid-row">
                <!-- Caixa de Imagem -->
                <div class="d3-image-box">
                    <!-- Substitua pelo nome correto da imagem da rodovia -->
                    <img src="assets/images/doc_dobra3_cidades_1780617454941.png" alt="Rodovia da cidade grande">
                </div>
                <!-- Caixa de Vidro -->
                <div class="d3-glass-box">
                    <p class="d3-text-content">
                        A questão real é outra:<br>
                        <span class="d3-text-highlight">"Nós sobreviveremos ao modelo de crescimento que construímos?"</span><br>
                        Enquanto discutimos pequenos hábitos de consumo, uma transformação estrutural acontece — ou deveria acontecer — a partir dos nossos atos. Em apenas 300 anos, passamos de 600 milhões para 8 bilhões de pessoas. Produzimos mais, consumimos mais, extraímos mais. E exigimos de um planeta finito algo impossível: crescimento infinito.
                    </p>
                </div>
            </div>

            <!-- Título Inferior -->
            <!-- Substitua pelo nome correto da imagem do título "NÓS SOBREVIVEREMOS..." -->
            <img src="assets/images/novo_titulo_2.png" alt="Nós sobreviveremos ao modelo de crescimento que construímos?" class="d3-title-img">

        </div>
    </section>

"""

idx3 = html.find(html_start)
idx4 = html.find(html_end_pattern)

if idx3 != -1 and idx4 != -1:
    html = html[:idx3] + html_new + html[idx4:]
else:
    print("Failed to find HTML block")


# 3. Replace GSAP
gsap_start = '            // Animação Bento Box Dobra 3'
gsap_end_pattern = '            // Animação Dobra 5'

gsap_new = """            // Parallax e Animação Dobra 3
            gsap.to("#dobra3-bg-parallax", {
                scrollTrigger: {
                    trigger: ".section-dobra-3",
                    start: "top bottom",
                    end: "bottom top",
                    scrub: true
                },
                yPercent: 20,
                ease: "none"
            });
            
            gsap.from(".d3-glass-box, .d3-image-box", {
                scrollTrigger: {
                    trigger: ".section-dobra-3",
                    start: "top 80%",
                },
                y: 40, opacity: 0, duration: 0.8, stagger: 0.15, ease: "power3.out"
            });
            
            gsap.from(".d3-title-img", {
                scrollTrigger: {
                    trigger: ".section-dobra-3",
                    start: "top 90%",
                },
                y: 30, opacity: 0, duration: 0.8, stagger: 0.3, ease: "power3.out"
            });

"""

idx5 = html.find(gsap_start)
idx6 = html.find(gsap_end_pattern)

if idx5 != -1 and idx6 != -1:
    html = html[:idx5] + gsap_new + html[idx6:]
else:
    print("Failed to find GSAP block")


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated index.html via python")
