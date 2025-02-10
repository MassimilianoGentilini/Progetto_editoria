import re #importiamo la libreria per la gestione delle espressioni regolari
def modify_markdown(file_path, output_path, rules):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()    
    content = font_css + "\n" + content  # Inserisce il CSS all'inizio del documento
    for rule in rules:
        pattern = rule.get("pattern")
        replace = rule.get("replace")
        content = re.sub(pattern, replace, content)
    with open(output_path, "w", encoding="utf-8") as file: #viene salvato il nuovo file con il contenuto modificato
        file.write(content)
    print(f"File modificato salvato in '{output_path}'.")
# Regole di esempio
rules = [
    {
        "pattern": r"(## .+)",  
        "replace": r"\n<div style=\"page-break-before:always\"></div>\n\1"
    }
]
#File di input e File di output
input_file = "DSA.md"
output_file = "DSAProgetto.md"
modify_markdown(input_file, output_file, rules)

