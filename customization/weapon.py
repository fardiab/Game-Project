class Weapon:
    def __init__(self, muzzle="culverins", barrel="long", scope="ACOG", magazine="fully_capacity", stock="waffle", color="black"):
        self.muzzle = muzzle
        self.barrel = barrel
        self.scope = scope
        self.magazine = magazine
        self.stock = stock
        self.color = color

    def get_info(self):
        return """Muzzle(1) - culverins, falconets, sakers, demi-cannon, rifled muzzle-loaders, Parrott rifles
Barrel(2) - short, long, standart
Scope(3) - holo, ACOG, red dot, reflex
Magazine(4) - toxic, fire, multiple-capacity
Stock(4) - waffle, M4
Color(5) - (Every color)"""

    def muzzle_part(self):
        return f"Muzzle is {self.muzzle}"

    def barrel_part(self):
        return f"Barrel is {self.barrel}"

    def scope_part(self):
        return f"Scope is {self.scope}"

    def magazine_part(self):
        return f"Magazine is {self.magazine}"

    def stock_part(self):
        return f"Stock is {self.magazine}"

    def change_parts(self):
        return """Muzzle - 1
Barrel - 2
Scope - 3
Magazine - 4
Stock - 5"""

class M4A1(Weapon):
    def __init__(self, muzzle="falconets", barrel="long", scope="Holo", magazine="fully_capacity", stock="M4", color="dark blue"):
        super().__init__(muzzle=muzzle, barrel=barrel, scope=scope, magazine=magazine, stock=stock, color=color)

    def restore_M4A1_muzzle(self, other):
        changed = self.muzzle.replace(f"{self.muzzle}", f"{other}")
        return f"Muzzle - {changed}"

    def restore_M4A1_barrel(self, other):
        changed = self.barrel.replace(f"{self.barrel}", f"{other}")
        return f"Barrel - {changed}"
    
    def restore_M4A1_scope(self, other):
        changed = self.scope.replace(f"{self.scope}", f"{other}")
        return f"Scope - {changed}"
    
    def restore_M4A1_magazine(self, other):
        changed = self.magazine.replace(f"{self.magazine}", f"{other}")
        return f"Magazine - {changed}"

    def restore_M4A1_stock(self, other):
        changed = self.stock.replace(f"{self.stock}", f"{other}")
        return f"Stock - {changed}"

class AK_47(Weapon):
    def __init__(self, muzzle="compensatory", barrel="long", scope="nothing", magazine="standart_capacity", stock="AK_47-stock", color="brown-black"):
        super().__init__(muzzle=muzzle, barrel=barrel, scope=scope, magazine=magazine, stock=stock, color=color)

    def restore_AK_47_muzzle(self, other):
        changed = self.muzzle.replace(f"{self.muzzle}", f"{other}")
        return f"Muzzle - {changed}"

    def restore_AK_47_barrel(self, other):
        changed = self.barrel.replace(f"{self.barrel}", f"{other}")
        return f"Barrel - {changed}"
    
    def restore_AK_47_scope(self, other):
        changed = self.scope.replace(f"{self.scope}", f"{other}")
        return f"Scope - {changed}"
    
    def restore_AK_47_magazine(self, other):
        changed = self.magazine.replace(f"{self.magazine}", f"{other}")
        return f"Magazine - {changed}"

    def restore_AK_47_stock(self, other):
        changed = self.stock.replace(f"{self.stock}", f"{other}")
        return f"Stock - {changed}"

class LightMachineGun(Weapon):
    def __init__(self, muzzle="compensatory", barrel="long", scope="nothing", magazine="standart_capacity", color="standart"):
        super().__init__(muzzle=muzzle, barrel=barrel, scope=scope, magazine=magazine, color=color)

    def restore_Light_Machine_Gun_muzzle(self, other):
        changed = self.muzzle.replace(f"{self.muzzle}", f"{other}")
        return f"Muzzle - {changed}"

    def restore_Light_Machine_Gun_barrel(self, other):
        changed = self.barrel.replace(f"{self.barrel}", f"{other}")
        return f"Barrel - {changed}"
    
    def restore_Light_Machine_Gun_scope(self, other):
        changed = self.scope.replace(f"{self.scope}", f"{other}")
        return f"Scope - {changed}"
    
    def restore_Light_Machine_Gun_magazine(self, other):
        changed = self.magazine.replace(f"{self.magazine}", f"{other}")
        return f"Magazine - {changed}"

    def change_parts(self):
        return """Muzzle - 1
Barrel - 2
Scope - 3
Magazine - 4"""

class DesertEagle(Weapon):
    def __init__(self, muzzle="muffler-muzzle", scope="nothing", magazine="toxic",  color="yellow-black"):
        super().__init__(muzzle=muzzle, scope=scope, magazine=magazine, color=color)

    def restore_desert_eagle_muzzle(self, other):
        changed = self.muzzle.replace(f"{self.muzzle}", f"{other}")
        return f"Muzzle - {changed}"

    def restore_desert_eagle_scope(self, other):
        changed = self.scope.replace(f"{self.scope}", f"{other}")
        return f"Scope - {changed}"
    
    def restore_desert_eagle_magazine(self, other):
        changed = self.magazine.replace(f"{self.magazine}", f"{other}")
        return f"Magazine - {changed}"

    def change_parts(self):
        return """Muzzle - 1
Scope - 2
Magazine - 3"""

class WeaponList:
    def __str__(self):
        return """M4A1 - 1
AK-47 - 2
Light Machine Gun - 3
Desert Eagle - 4"""

