"""
tp4.3
Vincent Brouillet
goupe:405
exercie tp4.3
"""

from enum import Enum
from dataclasses import dataclass
import random as r
import colorama as c

print(c.Style.BRIGHT + "")


def dice_roll(dice_type):
    if dice_type == "stat":
        dice_list = []
        for dice in range(4):
            dice = r.randint(1, 6)
            dice_list.append(dice)
        dice_list.remove(min(dice_list))
        roll = sum(dice_list)
    elif dice_type == "armure":
        roll = r.randint(1, 12)
    elif dice_type == "vie":
        roll = r.randint(1, 20)
    elif dice_type == "profession":
        profession_list = ["Guerrier", "Magicien", "Archer", "Voleur", "Healer", "Tank"]
        roll = r.choice(profession_list)
    elif dice_type == "espece":
        espece_list = ["Humain", "Kobold"]
        roll = r.choice(espece_list)
    elif dice_type == "Humain":
        race_list = ["Calishite", "Chondathan", "Damaran", "Illuskan",
                     "Mulan", "Rashemi", "Shou", "Tethyrian", "Turami"]
        roll = r.choice(race_list)
    elif dice_type == "Kobold":
        race_list = [""]
        roll = r.choice(race_list)
    elif dice_type == "name":
        roll = "error"
    else:
        roll = "error"
    return roll


@dataclass
class Alignment(Enum):
    NOT_DEFINED = 0
    LAWFUL_GOOD = 1
    NEUTRAL_GOOD = 2
    CHAOTIC_GOOD = 3
    LAWFUL_NEUTRAL = 4
    TRUE_NEUTRAL = 5
    CHAOTIC_NEUTRAL = 6
    LAWFUL_EVIL = 7
    NEUTRAL_EVIL = 8
    CHAOTIC_EVIL = 9


@dataclass
class DataNpc:
    Force: int
    Agilite: int
    Constitution: int
    Intelligence: int
    Sagesse: int
    Charisme: int
    armure: int
    espece: str
    race: str
    nom: str
    vie: int
    profession: str
    alignment: 0


@dataclass
class DataItem:
    item: list[str]
    nombre: list[int]


class Inventory:
    def __init__(self):
        self.list_item = [[], []]
        self.nombre_item = len(self.list_item[0])
        self.inventorydata = DataItem(self.list_item[0], self.list_item[1])

    def inventory_info(self):
        print(f"Voici votre inventaire:")
        self.nombre_item = len(self.inventorydata.item)
        for i in range(self.nombre_item):
            print(f"{self.inventorydata.item[i-1]} : {self.inventorydata.nombre[i-1]}")

    def inventory_add(self, item, nombre):
        self.nombre_item = len(self.inventorydata.item)
        # cherche pour voir si l'objet est présent dans la liste
        for i in range(self.nombre_item):
            if self.inventorydata.item[0][i-1] == item:
                self.inventorydata.nombre[i-1] += nombre
                return
            else:
                pass
        # si l'objet n'est présent dans la liste, ajouter un nouvelle objet
        self.inventorydata.item.append(item)
        self.inventorydata.nombre.append(nombre)

    def inventory_remove(self, item, nombre):
        self.nombre_item = len(self.inventorydata.item)
        for i in range(self.nombre_item):
            if self.inventorydata.item[i-1] == item:
                self.inventorydata.nombre[i-1] -= nombre
                if self.inventorydata.nombre[i-1] <= 0:
                    self.inventorydata.item.pop(i-1)
                    self.inventorydata.nombre.pop(i-1)
                return
            else:
                pass
        print("no item with this name found")


class Npc:
    def __init__(self):
        self.npcdata = DataNpc(dice_roll("stat"), dice_roll("stat"), dice_roll("stat"),
                               dice_roll("stat"), dice_roll("stat"), dice_roll("stat"), dice_roll("armure"),
                               "Humain", "race", "NPC", dice_roll("vie"), dice_roll("profession"),
                               r.choice(list(Alignment)))
        self.npcdata.race = dice_roll(self.npcdata.espece)
        self.inventory = Inventory()

    def stat_info(self):
        print(f"Nom: {self.npcdata.nom} | Race: {self.npcdata.race} {self.npcdata.espece} | "
              f"Vie: {self.npcdata.vie} | Profession: {self.npcdata.profession}"
              f"\nDefense: {self.npcdata.armure}"
              f"\nForce: {self.npcdata.Force}    | Constitution: {self.npcdata.Constitution}"
              f"\nAgilité: {self.npcdata.Agilite}  | Intelligence: {self.npcdata.Intelligence}"
              f"\nCharisme: {self.npcdata.Charisme} | Sagesse: {self.npcdata.Sagesse} "
              f"\nAlignment: {str(self.npcdata.alignment.name.capitalize().replace("_", " "))}")

    @staticmethod
    def attaque(cible):
        dice = r.randint(1, 20)
        if dice == 20:
            dmg = r.randint(1, 8)
        elif dice > 1:
            dmg = r.randint(1, 6)
        else:
            dmg = 0
        cible.subir_dmg(dmg, dice)

    def subir_dmg(self, dmg, dice):
        if dice == 20:
            self.npcdata.vie -= dmg
            print("attaque critique réussis")
        elif dice > self.npcdata.armure:
            self.npcdata.vie -= dmg
            print("attaque réussis")
        else:
            print("attaque raté")
        self.est_vivant()

    def est_vivant(self):
        if self.npcdata.vie <= 0:
            print(f"{self.npcdata.nom} est mort")


npc = Npc()
