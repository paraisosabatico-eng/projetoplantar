import sys

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's check where the string 'DOBRA 3 (BENTO BOX SÓLIDO - REFERÊNCIA)' is.
idx = html.find('DOBRA 3 (BENTO BOX SÓLIDO - REFERÊNCIA)')

if idx != -1:
    # Find the start of the comment block which is slightly before this.
    idx_start = html.rfind('/* ───', 0, idx)
    
    # Find the start of DOBRA 4
    idx_end = html.find('DOBRA 4 — POR QUE O PROJETO EXISTE', idx)
    idx_end = html.rfind('/* ───', 0, idx_end)

    if idx_start != -1 and idx_end != -1:
        css_new = """/* ──────────────────────────────────────────────
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
        html = html[:idx_start] + css_new + html[idx_end:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("CSS Replaced.")
    else:
        print("Found DOBRA 3 but failed to find start/end comments.")
else:
    print("Could not find 'DOBRA 3 (BENTO BOX SÓLIDO - REFERÊNCIA)'")

