import argparse

def get_args():
    p = argparse.ArgumentParser(description="Compte le nombre de mots dans un fichier texte")
    p.add_argument('file', help="Chemin pour un fichier texte")
    return p.parse_args()

def main():
    args = get_args()

    with open(args.file) as f:
        text = f.read()

    words = text.split()

    print(f"Le nombre de mots dans {args.file} est {len(words)}")

if __name__ == '__main__':
    main()
