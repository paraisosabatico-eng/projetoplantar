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

new_css = """/* DOBRA 7: O COLAPSO INEVITÁVEL */
        .section-dobra-7 {
            position: relative;
            z-index: 2;
            background-color: #0F1612;
            color: #FFFFFF;
            padding: 8rem 0;
            overflow-x: hidden;
        }
        .d7-container {
            width: 100%;
            max-width: 95rem; /* Bem largo para acomodar o gráfico duplo */
            margin: 0 auto;
            display: grid;
            grid-template-columns: 32% 64%;
            justify-content: space-between;
            gap: 4rem;
            padding: 0 2rem;
        }
        .d7-text-side {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            height: fit-content;
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
        .d7-subtitle {
            font-size: 1.5rem;
            font-weight: 500;
            color: #A3A3A3;
            line-height: 1.4;
            margin-bottom: 2rem;
        }
        .d7-paragraph {
            font-size: 1.25rem;
            line-height: 1.6;
            color: #FFFFFF;
            margin-bottom: 1.5rem;
        }
        .d7-final-text strong {
            color: #638A55;
            font-weight: 700;
        }
        
        .d7-pyramid-side {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
        }
        
        .d7-dual-pyramids {
            display: flex;
            align-items: stretch;
            justify-content: center;
            width: 100%;
            gap: 2rem;
        }

        .d7-pyramid-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            flex: 1;
        }

        .d7-pyramid-header {
            text-align: center;
            margin-bottom: 2rem;
            height: 4rem;
        }

        .d7-pyramid-title {
            font-size: 1.1rem;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }
        
        .d7-pyramid-desc {
            font-size: 0.85rem;
            color: #A3A3A3;
        }

        .d7-pyramid-flex {
            display: flex;
            align-items: stretch;
            gap: 1rem;
            height: 100%;
        }

        .d7-labels {
            display: flex;
            flex-direction: column;
            font-size: 0.95rem;
            color: #FFFFFF;
            font-weight: 500;
        }
        
        .d7-labels-left {
            text-align: right;
        }
        .d7-labels-right {
            text-align: left;
        }
        
        .d7-label-idosos { height: 43%; display: flex; align-items: center; justify-content: flex-end; }
        .d7-label-adultos { height: 28%; display: flex; align-items: center; justify-content: flex-end; }
        .d7-label-jovens { height: 29%; display: flex; align-items: center; justify-content: flex-end; }
        
        .d7-labels-right .d7-label-idosos, 
        .d7-labels-right .d7-label-adultos, 
        .d7-labels-right .d7-label-jovens {
            justify-content: flex-start;
        }

        .d7-pyramid-structure {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .d7-arrow-divider {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            width: 40px;
        }
        
        .d7-divider-line {
            width: 1px;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.2);
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
        }

        .d7-arrow-circle {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.3);
            background-color: #0F1612;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #FFFFFF;
            z-index: 2;
        }
        
        .d7-arrow-circle svg {
            width: 20px;
            height: 20px;
        }

        .d7-row {
            display: flex;
            justify-content: center;
            gap: 0.3rem;
            margin-bottom: 0.3rem;
        }
        .d7-human {
            width: 1.4rem;
            height: 1.4rem;
        }
        .row-idoso .d7-human { color: #FFFFFF; }
        .row-adulto .d7-human { color: #FFFFFF; }
        .row-jovem .d7-human { color: #638A55; }
        
        /* O Topo da invertida tem linha sublinhada verde sutil como na imagem */
        .inverted-pyramid .d7-row:first-child {
            border-top: 2px solid #638A55;
            padding-top: 0.5rem;
        }

        @media (max-width: 1100px) {
            .d7-container {
                grid-template-columns: 1fr;
                gap: 4rem;
            }
            .d7-human {
                width: 1.2rem;
                height: 1.2rem;
            }
        }
        
        @media (max-width: 768px) {
            .section-dobra-7 {
                padding: 4rem 0;
            }
            .d7-title {
                font-size: 2.2rem;
            }
            .d7-subtitle {
                font-size: 1.25rem;
            }
            .d7-paragraph {
                font-size: 1.1rem;
            }
            .d7-dual-pyramids {
                flex-direction: column;
                align-items: center;
                gap: 3rem;
            }
            .d7-arrow-divider {
                width: 100%;
                height: 40px;
            }
            .d7-divider-line {
                width: 100%;
                height: 1px;
                top: 50%;
                left: 0;
                transform: translateY(-50%);
            }
            .d7-arrow-circle {
                transform: rotate(90deg); /* Seta aponta pra baixo no mobile */
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

new_html = """<!-- DOBRA 7: O COLAPSO INEVITÁVEL -->
    <svg width="0" height="0" class="hidden" style="display:none;">
        <symbol id="icon-human" viewBox="0 0 24 24">
            <path fill="currentColor" d="M12,2C13.1,2 14,2.9 14,4C14,5.1 13.1,6 12,6C10.9,6 10,5.1 10,4C10,2.9 10.9,2 12,2M11,19.5V13H6V8.5C6,7.67 6.67,7 7.5,7H16.5C17.33,7 18,7.67 18,8.5V13H13V19.5H11Z"/>
        </symbol>
    </svg>
    
    <section id="colapso-inevitavel" class="section-dobra-7">
        <div class="d7-container">
            <!-- Textos (Lado Esquerdo - Pinado no Desktop) -->
            <div class="d7-text-side">
                <h2 class="d7-title">O COLAPSO INEVITÁVEL</h2>
                <h3 class="d7-subtitle">Quem espera que este documentário entregue uma resposta fácil e redentora, vai se deparar com um paradoxo brutal.</h3>
                
                <p class="d7-paragraph">
                    A solução mais óbvia para preservar os recursos do planeta é a redução da nossa taxa de natalidade, mas essa escolha esconde a sua própria armadilha. Mesmo que mudemos nossas atitudes de forma repentina, ainda assim entraremos em um colapso.
                </p>
                <p class="d7-paragraph">
                    O nosso modelo de sociedade funciona como uma pirâmide econômica viciada em crescimento constante. Quando decidimos ter menos filhos para não esgotar a Terra, causamos uma inversão rápida nessa pirâmide etária. O resultado é uma crise estrutural implacável: inevitavelmente, teremos uma população com mais idosos e cada vez menos jovens para sustentar a máquina social e econômica.
                </p>
                <p class="d7-paragraph d7-final-text">
                    Os espaços urbanos gigantescos, que antes foram criados para o consumo vibrante da juventude, tendem a ficar vazios, dando lugar a um envelhecimento silencioso das grandes cidades. A grande ironia do nosso tempo é que, para salvar a natureza, precisaremos aceitar o colapso do próprio sistema financeiro que nos sustenta. A conta, mais uma vez, exige sacrifícios. <strong>Você está pronto para essa escolha?</strong>
                </p>
            </div>

            <!-- Pirâmides Lado a Lado (Estático) -->
            <div class="d7-pyramid-side">
                <div class="d7-dual-pyramids">
                    
                    <!-- Pirâmide Saudável -->
                    <div class="d7-pyramid-box">
                        <div class="d7-pyramid-header">
                            <div class="d7-pyramid-title">PIRÂMIDE SAUDÁVEL</div>
                            <div class="d7-pyramid-desc">Nascem mais. Sustenta o sistema.</div>
                        </div>
                        <div class="d7-pyramid-flex">
                            <div class="d7-labels d7-labels-left">
                                <span class="d7-label-idosos">Idosos</span>
                                <span class="d7-label-adultos">Adultos</span>
                                <span class="d7-label-jovens">Jovens</span>
                            </div>
                            <div class="d7-pyramid-structure healthy-pyramid" id="d7-pyramid-healthy">
                                <!-- Gerado via JS -->
                            </div>
                        </div>
                    </div>

                    <!-- Divisor -->
                    <div class="d7-arrow-divider">
                        <div class="d7-divider-line"></div>
                        <div class="d7-arrow-circle">
                            <svg viewBox="0 0 24 24"><path fill="currentColor" d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z" /></svg>
                        </div>
                    </div>

                    <!-- Pirâmide Invertida -->
                    <div class="d7-pyramid-box">
                        <div class="d7-pyramid-header">
                            <div class="d7-pyramid-title" style="color: #638A55;">PIRÂMIDE INVERTIDA</div>
                            <div class="d7-pyramid-desc">Nascem menos. Sistema entra em colapso.</div>
                        </div>
                        <div class="d7-pyramid-flex">
                            <div class="d7-pyramid-structure inverted-pyramid" id="d7-pyramid-inverted">
                                <!-- Gerado via JS -->
                            </div>
                            <div class="d7-labels d7-labels-right">
                                <span class="d7-label-idosos">Idosos</span>
                                <span class="d7-label-adultos">Adultos</span>
                                <span class="d7-label-jovens">Jovens</span>
                            </div>
                        </div>
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

new_js = """// Setup Pirâmide Dobra 7
        const healthyStructure = [
            { count: 2, type: 'idoso' },
            { count: 4, type: 'idoso' },
            { count: 6, type: 'idoso' },
            { count: 8, type: 'adulto' },
            { count: 10, type: 'adulto' },
            { count: 12, type: 'jovem' },
            { count: 14, type: 'jovem' },
        ];
        
        const invertedStructure = [
            { count: 14, type: 'idoso' },
            { count: 12, type: 'idoso' },
            { count: 10, type: 'idoso' },
            { count: 8, type: 'adulto' },
            { count: 6, type: 'adulto' },
            { count: 4, type: 'jovem' },
            { count: 2, type: 'jovem' },
        ];

        function renderPyramid(structure, containerId) {
            const container = document.getElementById(containerId);
            if (container) {
                let html = '';
                structure.forEach(row => {
                    let iconsHTML = '';
                    for(let i = 0; i < row.count; i++) {
                        iconsHTML += '<svg class="d7-human"><use href="#icon-human"></use></svg>';
                    }
                    html += `<div class="d7-row row-${row.type}">${iconsHTML}</div>`;
                });
                container.innerHTML = html;
            }
        }

        renderPyramid(healthyStructure, 'd7-pyramid-healthy');
        renderPyramid(invertedStructure, 'd7-pyramid-inverted');

        // Pinning Dobra 7
        ScrollTrigger.matchMedia({
            "(min-width: 1101px)": function() {
                // Pin dos textos se a seção for maior que a viewport
                ScrollTrigger.create({
                    trigger: ".d7-text-side",
                    start: "top 20%",
                    endTrigger: ".section-dobra-7",
                    end: "bottom 80%",
                    pin: true,
                    pinSpacing: true
                });
            }
        });

        // Animacao suave de entrada
        gsap.from(".d7-dual-pyramids", {
            scrollTrigger: {
                trigger: ".section-dobra-7",
                start: "top 60%",
            },
            y: 40, opacity: 0, duration: 1.5, ease: "power3.out"
        });

"""
content = content[:js_start] + new_js + content[js_end:]

with open(file_path, "w") as f:
    f.write(content)
print("Updated successfully")
