car1 = input()
car2 = input()
car3 = input()

if car1 == "vertebrado":
    if car2 == "ave":
        if car3 == "carnivoro":
            print("aguia")
        if car3 == "onivoro":
            print("pomba")
    if car2 == "mamifero":
        if car3 == "onivoro":
            print("homem")
        if car3 == "herbivoro":
            print("vaca")
if car1 == "invertebrado":
    if car2 == "inseto":
        if car3 == "hematofago":
            print('pulga')
        if car3 == 'herbivoro':
            print('lagarta')
    if car2 == "anelideo":
        if car3 == 'hematofago':
            print('sanguessuga')
        if car3 == 'onivoro':
            print('minhoca')
