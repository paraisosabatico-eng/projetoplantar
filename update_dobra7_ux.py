import sys

file_path = "pages/segunda-fase.html"
with open(file_path, "r") as f:
    content = f.read()

# Extract CSS section to replace
css_start = content.find("/* DOBRA 7: O COLAPSO INEVITÁVEL */")
css_end = content.find("</style>")
if css_start == -1 or css_end == -1:
    print("Error finding CSS")
    sys.exit(1)

new_css = """/* DOBRA 7: O COLAPSO INEVITÁVEL (UX Redesign) */
        .section-dobra-7 {
            position: relative;
            z-index: 2;
            background-color: #0F1612;
            color: #FFFFFF;
            padding: 8rem 0;
            overflow: hidden;
        }
        .d7-container {
            width: 100%;
            max-width: 85rem;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6rem;
            padding: 0 2rem;
            align-items: start;
        }
        
        .d7-image-side {
            position: relative;
            height: 100%;
        }
        .d7-image-wrapper {
            position: relative;
            width: 100%;
            border-radius: 4px;
            overflow: hidden;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }
        .d7-main-image {
            width: 100%;
            height: auto;
            display: block;
            filter: contrast(1.1) brightness(0.9);
        }
        .d7-image-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to top, rgba(15, 22, 18, 0.8) 0%, transparent 40%);
        }

        .d7-text-side {
            display: flex;
            flex-direction: column;
            gap: 4rem;
            padding-top: 2rem;
            padding-bottom: 6rem;
        }
        
        .d7-title {
            font-family: 'Montserrat', serif;
            font-size: 3.5rem;
            font-weight: 800;
            color: #FFFFFF;
            line-height: 1.1;
            margin: 0;
            text-transform: uppercase;
        }

        .d7-cards-wrapper {
            display: flex;
            flex-direction: column;
            gap: 3.5rem;
        }

        .d7-card {
            border-left: 2px solid rgba(255, 255, 255, 0.1);
            padding-left: 2rem;
            position: relative;
            transition: border-color 0.3s ease;
        }
        
        .d7-card::before {
            content: '';
            position: absolute;
            left: -2px;
            top: 0;
            width: 2px;
            height: 0;
            background-color: #638A55;
            transition: height 0.8s ease;
        }
        .d7-card.active::before {
            height: 100%;
        }

        .d7-card-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #638A55;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .d7-card-text {
            font-size: 1.25rem;
            line-height: 1.6;
            color: #A3A3A3;
        }
        
        .d7-final-call {
            font-size: 1.5rem;
            color: #FFFFFF;
            font-weight: 500;
            margin-top: 2rem;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 4px;
            border-left: 4px solid #638A55;
        }
        .d7-final-call strong {
            color: #638A55;
        }

        @media (max-width: 992px) {
            .d7-container {
                grid-template-columns: 1fr;
                gap: 4rem;
            }
            .d7-title {
                font-size: 2.5rem;
            }
            .d7-text-side {
                padding-bottom: 0;
            }
        }
        @media (max-width: 768px) {
            .section-dobra-7 {
                padding: 4rem 0;
            }
            .d7-title {
                font-size: 2.2rem;
            }
            .d7-card-text {
                font-size: 1.1rem;
            }
            .d7-final-call {
                font-size: 1.2rem;
                padding: 1.5rem;
            }
        }
    """
content = content[:css_start] + new_css + content[css_end-4:]

# Extract HTML section
html_start = content.find("<!-- DOBRA 7: O COLAPSO INEVITÁVEL -->")
html_end = content.find("<!-- ══════════════════════════════════════════════════\n         DOBRA 10 — ETAPAS DO PROJETO")
if html_start == -1 or html_end == -1:
    print("Error finding HTML")
    sys.exit(1)

new_html = """<!-- DOBRA 7: O COLAPSO INEVITÁVEL (UX Redesign) -->
    <section id="colapso-inevitavel" class="section-dobra-7">
        <div class="d7-container">
            <!-- Imagem (Lado Esquerdo - Pinado no Desktop) -->
            <div class="d7-image-side">
                <div class="d7-image-wrapper">
                    <img src="/projetoplantar/assets/images/piramide-invertida.png" alt="Pirâmide Invertida - Colapso" class="d7-main-image">
                    <div class="d7-image-overlay"></div>
                </div>
            </div>

            <!-- Textos (Lado Direito - Scroll com Cards) -->
            <div class="d7-text-side">
                <div class="d7-text-header">
                    <h2 class="d7-title">O COLAPSO INEVITÁVEL</h2>
                </div>
                
                <div class="d7-cards-wrapper">
                    <!-- Card 1 -->
                    <div class="d7-card">
                        <h4 class="d7-card-title">01. O Paradoxo</h4>
                        <p class="d7-card-text">A solução mais óbvia esconde a sua própria armadilha. Acreditamos que a redução da nossa taxa de natalidade preservaria os recursos do planeta. Mas, ao tentar salvar a Terra, destruímos a base do nosso sistema.</p>
                    </div>

                    <!-- Card 2 -->
                    <div class="d7-card">
                        <h4 class="d7-card-title">02. A Inversão</h4>
                        <p class="d7-card-text">Nosso modelo de sociedade funciona como uma pirâmide viciada em crescimento constante. Quando decidimos ter menos filhos, causamos uma inversão rápida nessa pirâmide etária. O resultado é implacável: mais idosos, e cada vez menos jovens para sustentar a máquina.</p>
                    </div>

                    <!-- Card 3 -->
                    <div class="d7-card">
                        <h4 class="d7-card-title">03. O Vazio Urbano</h4>
                        <p class="d7-card-text">Espaços urbanos gigantescos, criados para o consumo vibrante da juventude, tendem a ficar vazios, dando lugar a um envelhecimento silencioso. A grande ironia é que precisaremos aceitar o colapso do próprio sistema financeiro que nos sustenta.</p>
                    </div>
                    
                    <div class="d7-final-call">
                        A conta exige sacrifícios. <strong>Você está pronto para essa escolha?</strong>
                    </div>
                </div>
            </div>
        </div>
    </section>

    """
content = content[:html_start] + new_html + content[html_end:]


# Extract JS section
js_start = content.find("// Setup Pirâmide Dobra 7")
js_end = content.find("    });\n    </script>")
if js_start == -1 or js_end == -1:
    print("Error finding JS")
    sys.exit(1)

new_js = """// Animação Dobra 7 - UX Redesign
        ScrollTrigger.matchMedia({
            "(min-width: 993px)": function() {
                // Pin da Imagem
                ScrollTrigger.create({
                    trigger: ".d7-image-wrapper",
                    start: "top 20%",
                    endTrigger: ".section-dobra-7",
                    end: "bottom 80%",
                    pin: true,
                    pinSpacing: false
                });
            }
        });

        // Fade Up nos Cards
        gsap.utils.toArray(".d7-card").forEach(card => {
            gsap.from(card, {
                scrollTrigger: {
                    trigger: card,
                    start: "top 80%",
                    toggleClass: "active"
                },
                y: 40, opacity: 0, duration: 1, ease: "power2.out"
            });
        });
        
        gsap.from(".d7-final-call", {
            scrollTrigger: {
                trigger: ".d7-final-call",
                start: "top 85%"
            },
            y: 30, opacity: 0, duration: 1, delay: 0.2, ease: "power2.out"
        });

"""
content = content[:js_start] + new_js + content[js_end:]

with open(file_path, "w") as f:
    f.write(content)
print("Updated successfully")
