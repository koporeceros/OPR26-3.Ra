import requests
import pprint
import random

urlTrivia = "https://opentdb.com/api.php?amount=10&type=multiple"


kt = requests.get(urlTrivia).json()

rez = kt["results"]

#print(len(rez))
#pprint.pprint(kt["results"][0])
#print(rez)
"""
for r in rez:
    print("-" * 80)
    print(r["question"])
    print(r["correct_answer"])
    pprint.pprint(r["incorrect_answers"])
"""
total = 0

for r in rez:
    print("-" * 80)
    print(r["question"])
    cor = r["correct_answer"]
    together = r["incorrect_answers"]
    together.append(cor)
    print(random.shuffle(together))
    
    odgovor = input("Vnesi odgovor: ")
    if odgovor == cor:
        print("Pravilno")
        total += 1
    else:
        print("narobe")

print(f"Pravilno ste odgovorina na {total}/10 vprašanj")


