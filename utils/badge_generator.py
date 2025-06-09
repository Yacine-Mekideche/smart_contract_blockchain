def extract_badges(code: str) -> str:
    """
    Détecte les fonctionnalités sensibles ou importantes du contrat
    et retourne une liste formatée en Markdown.
    """
    badges_list = []
    lower = code.lower()

    if "blacklist" in lower:
        badges_list.append("❌ Blacklistable")
    if "pause" in lower:
        badges_list.append("⏸️ Pausable")
    if "mint" in lower:
        badges_list.append("🪙 Mintable")
    if "burn" in lower:
        badges_list.append("🔥 Burnable")
    if "onlyowner" in lower:
        badges_list.append("👑 Ownable")
    if "deprecated" in lower or "upgrade" in lower:
        badges_list.append("🔁 Upgradable")

    if not badges_list:
        return "No specific functional badge detected."
    return "\n".join(f"- {b}" for b in badges_list)
