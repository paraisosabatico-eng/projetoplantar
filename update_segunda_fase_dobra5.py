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
           DOBRA 5 (A CONTA SIMPLES)
        ────────────────────────────────────────────── */
        .section-dobra-5 {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 8rem 2rem;
            background-color: #F3F4F0; /* Light organic background */
            color: #1F2D21;
        }

        .d5-content-wrapper {
            position: relative;
            z-index: 1;
            width: 100%;
            max-width: 75rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        .d5-title {
            font-family: 'Montserrat', serif;
            font-size: 3.5rem;
            font-weight: 700;
            color: #1F2D21;
            margin: 0 0 2rem 0;
            line-height: 1.1;
        }

        .d5-intro {
            font-size: 1.25rem;
            line-height: 1.7;
            color: #3A3A3A;
            max-width: 55rem;
            margin-bottom: 5rem;
        }

        .d5-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 3rem;
            width: 100%;
            margin-bottom: 5rem;
        }

        .d5-col {
            background-color: #FFFFFF;
            border-radius: 1.5rem;
            padding: 3rem 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: transform 0.4s ease;
        }
        
        .d5-col:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }

        .d5-dot-matrix {
            display: grid;
            grid-template-columns: repeat(10, 1fr);
            gap: 4px;
            width: 100%;
            max-width: 140px;
            margin: 0 auto 2rem auto;
        }

        .d5-dot {
            width: 100%;
            aspect-ratio: 1;
            border-radius: 50%;
            background-color: #E0E2D8;
        }

        .d5-percent {
            font-family: 'Montserrat', serif;
            font-size: 3.5rem;
            font-weight: 800;
            color: #899702;
            line-height: 1;
            margin-bottom: 0.5rem;
            letter-spacing: -0.05em;
        }

        .d5-col-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #1F2D21;
            margin-bottom: 1rem;
        }

        .d5-col-desc {
            font-size: 0.95rem;
            color: #555555;
            line-height: 1.5;
            margin: 0;
        }

        .d5-quote-box {
            background-color: #EAE9E2;
            border-left: 5px solid #899702;
            padding: 2.5rem 3rem;
            border-radius: 0 1rem 1rem 0;
            max-width: 60rem;
            text-align: left;
        }

        .d5-quote-box p {
            font-size: 1.15rem;
            line-height: 1.7;
            color: #3A3A3A;
            margin: 0;
        }

        @media (max-width: 992px) {
            .d5-grid {
                grid-template-columns: 1fr;
                max-width: 25rem;
                margin-left: auto;
                margin-right: auto;
            }
            .d5-title {
                font-size: 2.8rem;
            }
        }

    </style>
"""

def make_matrix(percent):
    html_str = '                    <div class="d5-dot-matrix">\n'
    empty_count = 100 - percent
    for i in range(100):
        if i < empty_count:
            html_str += '                        <div class="d5-dot"></div>\n'
        else:
            html_str += '                        <div class="d5-dot filled"></div>\n'
    html_str += '                    </div>'
    return html_str

matrix_75 = make_matrix(75)
matrix_50 = make_matrix(50)
matrix_25 = make_matrix(25)

html_new = f"""

    <!-- ══════════════════════════════════════════════════
         DOBRA 5 — A CONTA SIMPLES
    ══════════════════════════════════════════════════ -->
    <section id="a-conta-simples" class="section-dobra-5">
        <div class="d5-content-wrapper">
            
            <h2 class="d5-title">A Conta Simples Que Ninguém Quer Fazer</h2>
            
            <p class="d5-intro">A matemática demográfica é clara e irrefutável. A taxa de fertilidade determina o destino da população humana — e, consequentemente, a pressão sobre os recursos finitos da Terra. Não há escapatória dessa equação: ela não é opinião, é demografia e ecologia aplicada. Sem discutir natalidade, não há sustentabilidade possível. Sem reduzir gradualmente o ritmo de crescimento da população, qualquer discurso sobre salvar o planeta é, no máximo, uma fantasia confortável.</p>
            
            <div class="d5-grid">
                
                <div class="d5-col">
{matrix_75}
                    <div class="d5-percent">75%</div>
                    <h3 class="d5-col-title">Crescimento</h3>
                    <p class="d5-col-desc">Casais com três ou mais filhos. A população cresce exponencialmente. A demanda por recursos se torna insustentável e a pressão sobre o meio ambiente aumenta de forma acelerada a cada geração.</p>
                </div>

                <div class="d5-col">
{matrix_50}
                    <div class="d5-percent">50%</div>
                    <h3 class="d5-col-title">Estabilidade</h3>
                    <p class="d5-col-desc">Casais com dois filhos. A população se mantém no mesmo patamar. O índice já é excessivamente alto para a capacidade de regeneração dos recursos naturais — o impacto ambiental continua crítico.</p>
                </div>

                <div class="d5-col">
{matrix_25}
                    <div class="d5-percent">25%</div>
                    <h3 class="d5-col-title">Redução</h3>
                    <p class="d5-col-desc">Casais com um filho. A população começa a reduzir. A real regeneração só começa a acontecer com essa média — um desafio cultural, social e ético que frequentemente leva ao silêncio.</p>
                </div>

            </div>

            <div class="d5-quote-box">
                <p>A redução real só começa a acontecer quando, em média, cada casal tem apenas um filho — um cenário que, embora matematicamente simples, envolve complexas questões culturais, sociais e éticas. Discutir isso é crucial, mas a delicadeza do tema frequentemente leva ao silêncio, agravando o problema.</p>
            </div>

        </div>
    </section>

    <!-- ══════════════════════════════════════════════════
         DOBRA 10 — ETAPAS DO PROJETO
"""

gsap_new = """
        // Animação Dobra 5
        gsap.from(".d5-title, .d5-intro", {
            scrollTrigger: {
                trigger: ".section-dobra-5",
                start: "top 80%",
            },
            y: 30, opacity: 0, duration: 0.8, stagger: 0.2, ease: "power3.out"
        });

        gsap.from(".d5-col", {
            scrollTrigger: {
                trigger: ".d5-grid",
                start: "top 75%",
            },
            y: 50, opacity: 0, duration: 0.8, stagger: 0.15, ease: "power3.out"
        });

        gsap.utils.toArray('.d5-col').forEach(col => {
            let filledDots = col.querySelectorAll('.d5-dot.filled');
            ScrollTrigger.create({
                trigger: col,
                start: "top 75%",
                onEnter: () => {
                    gsap.to(filledDots, {
                        backgroundColor: "#2A3318",
                        duration: 0.05,
                        stagger: {
                            amount: 1,
                            from: "end"
                        }
                    });
                }
            });
        });

        gsap.from(".d5-quote-box", {
            scrollTrigger: {
                trigger: ".d5-quote-box",
                start: "top 85%",
            },
            x: -40, opacity: 0, duration: 0.8, ease: "power3.out"
        });
    });
    </script>
"""

html = html.replace('    </style>', css_new)
html = html.replace('    <!-- ══════════════════════════════════════════════════\n         DOBRA 10 — ETAPAS DO PROJETO', html_new)
html = html.replace('    });\n    </script>', gsap_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Injected Dobra 5 HTML, CSS, and GSAP successfully.")
