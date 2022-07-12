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

    real_word_re = re.compile(r'[a-zA-Z]+')

    real_words = [ w for w in words if real_word_re.match(w) ]

    print(f'words = {words}')
    print(f'real_words = {real_words}')
    print(f"Le nombre de mots dans {args.file} est {len(words)}")
    print(f"Le nombre de vrais mots dans {args.file} est {len(real_words)}")

if __name__ == '__main__':
    main()
