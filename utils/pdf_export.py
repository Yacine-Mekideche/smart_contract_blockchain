# utils/pdf_export.py

from fpdf import FPDF

def _to_latin1(text: str) -> str:
    """Filtre les caractères non codables en Latin-1."""
    return text.encode('latin-1', 'ignore').decode('latin-1')

class PDF(FPDF):
    def header(self):
        # Titre en haut de chaque page
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, _to_latin1("Résumé de l'Analyse de Smart Contract"), ln=True, align="C")
        self.ln(5)

    def footer(self):
        # Numéro de page en bas
        self.set_y(-15)
        self.set_font("Arial", size=8)
        self.cell(0, 10, _to_latin1(f"Page {self.page_no()}"), align="C")

    def section(self, num: int, title: str, body: str):
        # Titre de section numéroté
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, _to_latin1(f"{num}. {title}"), ln=True)
        self.ln(1)
        # Contenu
        self.set_font("Arial", size=11)
        for line in _to_latin1(body).split("\n"):
            self.multi_cell(0, 6, line)
        self.ln(4)


def render_pdf(description: str, badges: str, market_data: dict, source_code: str, summary: str) -> bytes:
    """
    Génère un PDF structuré en 5 sections :
    1. Description
    2. Badges fonctionnels
    3. Données marché
    4. Résumé global
    5. Extrait du code source
    """
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # 1. Description complète
    pdf.section(
        1,
        "Description détaillée du projet",
        description
    )

    # 2. Badges fonctionnels
    pdf.section(
        2,
        "Badges fonctionnels détectés",
        badges
    )

    # 3. Données marché
    if market_data:
        body = "\n".join(f"- {k}: {v}" for k, v in market_data.items())
    else:
        body = "Aucune donnée marché disponible."
    pdf.section(
        3,
        "Données marché (CoinGecko)",
        body
    )

    # 4. Résumé global
    pdf.section(
        4,
        "Résumé global du contrat",
        summary
    )

    # 5. Extrait du code source (tronqué)
    excerpt = source_code[:1500] + ("\n...\n" if len(source_code) > 1500 else "")
    pdf.section(
        5,
        "Extrait du code source (tronqué)",
        excerpt
    )

    return pdf.output(dest="S").encode("latin-1")
