import json

with open('1bac-reader/data/boite/dictionary.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

vocab_words = list(d.keys())
print('Total Boite vocab keys:', len(vocab_words))

sample_p = """Non! Tu ne pourras jamais le deviner! Les gens qui n'ont pas de pudeur, les va-nu-pieds de mauvaise foi, ceux-là qui offensent Dieu et son Envoyé par leurs agissements malhonnêtes auront à rendre compte de leurs mauvaises actions le jour de la Balance. Abdelkader a nié, il n'a pas simplement nié, il a même prétendu avoir versé la moitié du capital de l'affaire de Moulay Larbi pour l'achat du matériel, des cuirs et du fil d'or. Le Pacha ne pouvait pas connaître tous les détails de cette histoire."""

matched = [w for w in vocab_words if w.lower() in sample_p.lower()]
print('Words matched in screenshot paragraph:', matched)
