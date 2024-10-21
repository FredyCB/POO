def eliminar_signos(cadena: str) -> str:
    return cadena.replace(".", "").replace(";", "") \
        .replace("?", "").replace("!", "").replace("(", "") \
        .replace(")", "").replace(",", "").replace("-", "")