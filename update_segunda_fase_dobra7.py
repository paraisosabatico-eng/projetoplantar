import sys

file_path = "pages/segunda-fase.html"
with open(file_path, "r") as f:
    content = f.read()

# CSS Insertion
css_injection = """
        /* DOBRA 7: O COLAPSO INEVITÁVEL */
        .section-dobra-7 {
            position: relative;
            z-index: 2;
            background-color: #0F1612;
            color: #FFFFFF;
            padding: 8rem 0;
            overflow-x: clip;
        }
        .d7-container {
            width: 100%;
            max-width: 85rem;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
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
            min-height: 60vh;
        }
        .d7-pyramid-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }
        .d7-pyramid-container {
            position: relative;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            transform-origin: center center;
        }
        .d7-row {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }
        .d7-human {
            width: 1.8rem;
            height: 1.8rem;
            transition: all 0.3s ease;
        }
        .row-idoso .d7-human {
            color: #FFFFFF;
        }
        .row-adulto .d7-human {
            color: #FFFFFF;
        }
        .row-jovem .d7-human {
            color: #638A55;
        }
        
        /* Status labels */
        .d7-pyramid-header {
            text-align: center;
            margin-bottom: 3rem;
            height: 4rem; /* Fix height to avoid layout shift */
        }
        .d7-pyramid-title {
            font-size: 1.2rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
            transition: color 0.5s ease;
        }
        .d7-pyramid-desc {
            font-size: 0.9rem;
            color: #A3A3A3;
        }
        
        @media (max-width: 992px) {
            .d7-container {
                grid-template-columns: 1fr;
                gap: 6rem;
            }
            .d7-title {
                font-size: 2.5rem;
            }
            .d7-pyramid-side {
                min-height: 40vh;
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
            .d7-human {
                width: 0.8rem;
                height: 0.8rem;
            }
            .d7-row {
                gap: 0.2rem;
                margin-bottom: 0.2rem;
            }
        }
    </style>"""

content = content.replace("    </style>", css_injection)

# HTML Insertion
html_injection = """
    <!-- DOBRA 7: O COLAPSO INEVITÁVEL -->
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

            <!-- Pirâmide (Lado Direito - Animação) -->
            <div class="d7-pyramid-side">
                <div class="d7-pyramid-wrapper">
                    <div class="d7-pyramid-header">
                        <div class="d7-pyramid-title" id="d7-title-ui">PIRÂMIDE SAUDÁVEL</div>
                        <div class="d7-pyramid-desc" id="d7-desc-ui">Nascem mais. Sustenta o sistema.</div>
                    </div>
                    <div class="d7-pyramid-container" id="d7-pyramid">
                        <!-- Gerado via JS -->
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         DOBRA 10 — ETAPAS DO PROJETO"""

content = content.replace("    <!-- ══════════════════════════════════════════════════\n         DOBRA 10 — ETAPAS DO PROJETO", html_injection)

# JS Insertion
js_injection = """
        // Setup Pirâmide Dobra 7
        const pyramidStructure = [
            { count: 2, type: 'idoso' },
            { count: 4, type: 'idoso' },
            { count: 6, type: 'idoso' },
            { count: 8, type: 'adulto' },
            { count: 10, type: 'adulto' },
            { count: 12, type: 'jovem' },
            { count: 14, type: 'jovem' },
        ];
        const pyramidContainer = document.getElementById('d7-pyramid');
        if (pyramidContainer) {
            let pyramidHTML = '';
            pyramidStructure.forEach(row => {
                let iconsHTML = '';
                for(let i = 0; i < row.count; i++) {
                    iconsHTML += '<svg class="d7-human"><use href="#icon-human"></use></svg>';
                }
                pyramidHTML += `<div class="d7-row row-${row.type}">${iconsHTML}</div>`;
            });
            pyramidContainer.innerHTML = pyramidHTML;
        }

        // Animação Dobra 7
        ScrollTrigger.matchMedia({
            "(min-width: 993px)": function() {
                // Pin dos textos
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

        // Animação da Inversão da Pirâmide
        const tlDobra7 = gsap.timeline({
            scrollTrigger: {
                trigger: ".section-dobra-7",
                start: "top 40%",
                end: "bottom 80%",
                scrub: 1,
                onUpdate: function(self) {
                    const titleUI = document.getElementById("d7-title-ui");
                    const descUI = document.getElementById("d7-desc-ui");
                    if (self.progress > 0.6) {
                        titleUI.innerText = "PIRÂMIDE INVERTIDA";
                        titleUI.style.color = "#638A55";
                        descUI.innerText = "Nascem menos. Sistema entra em colapso.";
                    } else {
                        titleUI.innerText = "PIRÂMIDE SAUDÁVEL";
                        titleUI.style.color = "#FFFFFF";
                        descUI.innerText = "Nascem mais. Sustenta o sistema.";
                    }
                }
            }
        });

        // Passo 1: Jovens (base) começam a sumir (opacidade)
        tlDobra7.to(".row-jovem .d7-human", {
            opacity: 0.1,
            scale: 0.5,
            stagger: { amount: 0.5, from: "edges" },
            duration: 2
        });

        // Passo 2: A pirâmide vira
        tlDobra7.to("#d7-pyramid", {
            rotate: 180,
            duration: 3,
            ease: "power2.inOut"
        });

        // Passo 3: O Topo (agora base invertida) pesa e treme
        tlDobra7.to("#d7-pyramid", {
            x: 10,
            duration: 0.1,
            repeat: 5,
            yoyo: true
        });

    });
    </script>"""

content = content.replace("    });\n    </script>", js_injection)

with open(file_path, "w") as f:
    f.write(content)
print("Updated successfully")
