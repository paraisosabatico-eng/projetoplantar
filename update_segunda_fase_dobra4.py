import sys

file_path = 'pages/segunda-fase.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
except FileNotFoundError:
    print(f"Error: {file_path} not found.")
    sys.exit(1)

css_new = """
        /* ──────────────────────────────────────────────
           DOBRA 4 (A FRIEZA DOS NÚMEROS)
        ────────────────────────────────────────────── */
        .section-dobra-4 {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 8rem 2rem;
            gap: 4rem;
            overflow: hidden;
            background-color: #1A2E1C; /* Dark Green background */
        }

        .d4-content-wrapper {
            position: relative;
            z-index: 1;
            width: 100%;
            max-width: 85rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4rem;
        }

        .d4-header {
            text-align: center;
        }

        .d4-title {
            font-family: 'Montserrat', serif;
            font-size: 3.5rem;
            font-weight: 700;
            color: #EAE9E2;
            margin: 0;
            line-height: 1.1;
        }

        .d4-grid-row {
            display: flex;
            width: 100%;
            gap: 2rem;
            align-items: stretch;
        }

        /* Glass Box Dark Mode */
        .d4-glass-box-dark {
            background-color: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 1.5rem;
            padding: 3.5rem;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .d4-text-side {
            flex: 5;
            gap: 2rem;
        }

        .d4-text-side p {
            font-size: 1.15rem;
            line-height: 1.7;
            color: #B0B5A7;
            margin: 0;
            text-align: justify;
        }
        
        .d4-text-side p:first-child {
            margin-bottom: 1.5rem;
        }

        .d4-text-highlight {
            color: #A3C69C;
            font-weight: 600;
        }

        /* Infographic Bento Grid */
        .d4-info-side {
            flex: 4;
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: auto auto;
            gap: 1.5rem;
        }

        .d4-info-card {
            background-color: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 1.5rem;
            padding: 2.5rem 2rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            justify-content: center;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }

        .d4-info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            border-color: rgba(255, 255, 255, 0.2);
        }

        .d4-info-card.wide {
            grid-column: span 2;
        }

        .d4-info-number {
            font-family: 'Montserrat', serif;
            font-size: 4.5rem;
            font-weight: 800;
            color: #899702; /* Bright Green */
            line-height: 1;
            margin-bottom: 0.5rem;
            letter-spacing: -0.03em;
        }

        .d4-info-subtitle {
            font-size: 1.1rem;
            font-weight: 600;
            color: #EAE9E2;
            margin-bottom: 0.5rem;
            margin-top: 0;
        }

        .d4-info-desc {
            font-size: 0.95rem;
            color: #8B9483;
            line-height: 1.5;
            margin: 0;
        }

        @media (max-width: 1024px) {
            .d4-grid-row {
                flex-direction: column;
            }
            .d4-title {
                font-size: 2.8rem;
            }
        }

        @media (max-width: 768px) {
            .section-dobra-4 {
                padding: 5rem 1.5rem;
            }
            .d4-info-side {
                grid-template-columns: 1fr;
            }
            .d4-info-card.wide {
                grid-column: span 1;
            }
            .d4-glass-box-dark {
                padding: 2rem;
            }
            .d4-title {
                font-size: 2.3rem;
            }
        }

    </style>
"""

html_new = """

    <!-- ══════════════════════════════════════════════════
         DOBRA 4 — A FRIEZA DOS NÚMEROS
    ══════════════════════════════════════════════════ -->
    <section id="frieza-dos-numeros" class="section-dobra-4">
        <div class="d4-content-wrapper">
            
            <div class="d4-header">
                <h2 class="d4-title">A Frieza dos Números</h2>
            </div>

            <div class="d4-grid-row">
                <!-- Text Box -->
                <div class="d4-glass-box-dark d4-text-side">
                    <p>O colapso começou muito antes do plástico. Em apenas três séculos, a humanidade passou de 600 milhões para 8 bilhões de pessoas — uma multiplicação vertiginosa que transformou radicalmente a relação entre nossa espécie e os recursos finitos da Terra. <span class="d4-text-highlight">Produzimos mais, consumimos mais e extraímos mais a cada geração</span>, exigindo de um planeta com limites físicos algo matematicamente impossível: crescimento infinito. A linha do tempo é implacável e não admite negociação.</p>
                    
                    <p>Mas o crescimento é apenas parte da história. A matemática demográfica é brutal, mas inegável: a taxa de reposição populacional determina o futuro. Se dois adultos geram três filhos e esses três filhos, no futuro, geram mais três cada um, ocorre uma expansão vertiginosa — aquele crescimento exponencial que mencionamos. Agora, se dois adultos geram dois filhos, a população empata. Para que haja uma redução real que alivie significativamente a pressão sobre os recursos da Terra, é necessário que, em média, a humanidade passe a ter <span class="d4-text-highlight">muito menos de dois filhos por casal</span>. A equação não é opinião — é matemática, é demografia, é ecologia aplicada.</p>
                </div>

                <!-- Infographic Bento -->
                <div class="d4-info-side">
                    <!-- Wide Card -->
                    <div class="d4-info-card wide">
                        <div class="d4-info-number counter" data-target="300" data-suffix=" anos">0 anos</div>
                        <h3 class="d4-info-subtitle">Anos de aceleração</h3>
                        <p class="d4-info-desc">O período em que a curva demográfica se tornou exponencial e insustentável.</p>
                    </div>

                    <!-- Small Card 1 -->
                    <div class="d4-info-card">
                        <div class="d4-info-number counter" data-target="600" data-suffix="M">0M</div>
                        <h3 class="d4-info-subtitle">População em 1700</h3>
                        <p class="d4-info-desc">O ponto de partida antes da aceleração exponencial do crescimento humano.</p>
                    </div>

                    <!-- Small Card 2 -->
                    <div class="d4-info-card">
                        <div class="d4-info-number counter" data-target="8" data-suffix="B">0B</div>
                        <h3 class="d4-info-subtitle">População hoje em dia</h3>
                        <p class="d4-info-desc">Em apenas três séculos, multiplicamos nossa presença no planeta por mais de 13 vezes.</p>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         DOBRA 10 — ETAPAS DO PROJETO
"""

gsap_new = """
        // Animação Dobra 4
        gsap.from(".d4-title", {
            scrollTrigger: {
                trigger: ".section-dobra-4",
                start: "top 85%",
            },
            y: 30, opacity: 0, duration: 0.8, ease: "power3.out"
        });

        gsap.from(".d4-text-side", {
            scrollTrigger: {
                trigger: ".section-dobra-4",
                start: "top 75%",
            },
            x: -40, opacity: 0, duration: 1, ease: "power3.out"
        });

        gsap.from(".d4-info-card", {
            scrollTrigger: {
                trigger: ".section-dobra-4",
                start: "top 75%",
            },
            y: 40, opacity: 0, duration: 0.8, stagger: 0.2, ease: "power3.out"
        });

        // Efeito Contador
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => {
            let targetStr = counter.getAttribute('data-target');
            let target = parseFloat(targetStr);
            let suffix = counter.getAttribute('data-suffix');
            
            ScrollTrigger.create({
                trigger: counter,
                start: "top 85%",
                once: true,
                onEnter: () => {
                    let obj = { val: 0 };
                    gsap.to(obj, {
                        val: target,
                        duration: 2.5,
                        ease: "power2.out",
                        onUpdate: () => {
                            counter.innerHTML = Math.ceil(obj.val) + suffix;
                        }
                    });
                }
            });
        });
    });
    </script>
"""

html = html.replace('    </style>', css_new)
html = html.replace('    <!-- ══════════════════════════════════════════════════\n         DOBRA 10 — ETAPAS DO PROJETO', html_new)
html = html.replace('    });\n    </script>', gsap_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Injected Dobra 4 HTML, CSS, and GSAP successfully.")
