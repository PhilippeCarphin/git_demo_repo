import argparse
import re

def get_args():
    p = argparse.ArgumentParser(description="Compte le nombre de mots dans un fichier texte")
    p.add_argument('file', help="Chemin pour un fichier texte")
    return p.parse_args()

def main():
    args = get_args()

    with open(args.file) as f:
        text = f.read()

    words = text.split()
    nb_real_words = 0
    for w in words:
        if re.match(r'[a-zA-Z]+', w):
            nb_real_words += 1

    print(f"Le nombre de vrais mots dans {args.file} est {nb_real_words}")
    print(f"Le nombre de mots dans {args.file} est {len(words)}")

if __name__ == '__main__':
    main()
