import os
import shutil
import requests
import time

# Diretório onde o LeetSync salva os arquivos
SOURCE_DIR = "leetcode_solutions" 

# Diretórios de destino
DEST_DIRS = {
    "Easy": "easy",
    "Medium": "medium",
    "Hard": "hard"
}

# Cria pastas de destino se não existirem
for dir_name in DEST_DIRS.values():
    os.makedirs(dir_name, exist_ok=True)

def extract_slug(filename):
    parts = filename.split("_", 1)
    if len(parts) < 2:
        return None
    return parts[1].rsplit(".", 1)[0]

def get_difficulty(slug):
    url = "https://leetcode.com/graphql"
    query = {
        "query": """
        query getQuestion($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            difficulty
          }
        }
        """,
        "variables": {"titleSlug": slug}
    }
    try:
        response = requests.post(url, json=query)
        response.raise_for_status()
        data = response.json()
        return data["data"]["question"]["difficulty"]
    except:
        return None

# Processa todos os arquivos na pasta de origem
for filename in os.listdir(SOURCE_DIR):
    file_path = os.path.join(SOURCE_DIR, filename)

    if not os.path.isfile(file_path):
        continue

    slug = extract_slug(filename)
    if not slug:
        print(f"Ignorando (nome inesperado): {filename}")
        continue

    difficulty = get_difficulty(slug)
    if not difficulty:
        print(f"Problema não encontrado na API: {slug}")
        continue

    dest_folder = DEST_DIRS.get(difficulty)
    if not dest_folder:
        print(f"Dificuldade não reconhecida: {difficulty}")
        continue

    dest_path = os.path.join(dest_folder, filename)
    shutil.move(file_path, dest_path)
    print(f" {filename} → {dest_folder}/")

    time.sleep(0.5)
