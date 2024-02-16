arvore = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}

entrada1 = input()
entrada2 = input()
entrada3 = input()

if entrada1 in arvore and entrada2 in arvore[entrada1] and entrada3 in arvore[entrada1][entrada2]:
    animal = arvore[entrada1][entrada2][entrada3]
    print(animal)
else:
    print("Nao encontrado")