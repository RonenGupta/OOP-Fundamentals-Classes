from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def set_stats(self):
        pass

class Sword(Weapon):
    def __init__(self, name, category, damage, melee_type):
        super().__init__(name, category, damage)
        self.melee_type = melee_type

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Melee Type: {self.melee_type}")

    def set_stats(self, new_name, new_category, new_damage, new_melee_type):
        if isinstance(new_name, str):
            if isinstance(new_category, str):
                if isinstance(new_damage, int):
                    if isinstance(new_melee_type, str):
                        self.name = new_name
                        self.category = new_category
                        self.damage = new_damage
                        self.melee_type = new_melee_type
                    else:
                        raise ValueError("Type must be string.")
                else:
                    raise ValueError("Damage must be integer.")
            else:
                raise ValueError("Category must be string.")
        else:
            raise ValueError("Name must be string.")
        
class Bow(Weapon):
    def __init__(self, name, category, damage, range_type):
        super().__init__(name, category, damage)
        self.range_type = range_type

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Range Type: {self.range_type}")

    def set_stats(self, new_name, new_category, new_damage, new_range_type):
        if isinstance(new_name, str):
            if isinstance(new_category, str):
                if isinstance(new_damage, int):
                    if isinstance(new_range_type, str):
                        self.name = new_name
                        self.category = new_category
                        self.damage = new_damage
                        self.range_type = new_range_type
                    else:
                        raise ValueError("Range type must be string.")
                else:
                    raise ValueError("Damage must be integer.")
            else:
                raise ValueError("Category must be string.")
        else:
            raise ValueError("Name must be string.")
