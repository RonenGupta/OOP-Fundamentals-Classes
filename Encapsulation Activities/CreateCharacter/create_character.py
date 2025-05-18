class CreateCharacter:
    def __init__(self, name, classtype, level, str, dex, con, int, wis):
        self.name = name
        self.classtype = classtype
        self.level = level
        self.strength = str
        self.dexterity = dex
        self.constitution = con
        self.intellect = int
        self.wisdom = wis
    
    def get_name(self):
        return self.name
    
    def get_classtype(self):
        return self.classtype
    
    def get_level(self):
        return self.level
    
    def set_name(self, newname):
        if isinstance(newname, str):
            self.name = newname
        else:
            raise ValueError("New name must be a string.")
    
    def set_classtype(self, newclasstype):
        if isinstance(newclasstype, str):
            self.classtype = newclasstype
        else:
            raise ValueError("New class type must be a string.")
    
    def set_level(self, newlevel):
        if isinstance(newlevel, int):
            self.level = newlevel
        else:
            raise ValueError("New level must be an integer.")
        
    def get_strength(self):
        return self.strength
    
    def get_dexterity(self):
        return self.dexterity
    
    def get_constitution(self):
        return self.constitution
    
    def get_intellect(self):
        return self.intellect
    
    def get_wisdom(self):
        return self.wisdom
    
    def set_strength(self, newstrength):
        if isinstance(newstrength, int):
            self.strength = newstrength
        else:
            raise ValueError("New Strength must be an integer.")
    
    def set_dexterity(self, newdexterity):
        if isinstance(newdexterity, int):
            self.dexterity = newdexterity
        else:
            raise ValueError("New Dexterity must be an integer.")
        
    def set_constitution(self, newconstitution):
        if isinstance(newconstitution, int):
            self.constitution = newconstitution
        else:
            raise ValueError("New Constitution must be an integer.")
    
    def set_intellect(self, newintellect):
        if isinstance(newintellect, int):
            self.intellect = newintellect
        else:
            raise ValueError("New Intellect must be an integer.")
    
    def set_wisdom(self, newwisdom):
        if isinstance(newwisdom, int):
            self.wisdom = newwisdom
        else:
            raise ValueError("New Wisdom must be an integer.")
    
    def upgrade_stats(self):
        choice = 0
        while not (1 <= choice <= 5):
            try:
                choice = int(input("Welcome to the stat bar, choose from strength (1), dexterity (2), constitution (3), intellect (4), or wisdom (5), and upgrade by 2 points each. "))
            except ValueError:
                print("Choice must be between 1 and 5, not a string.")
                choice = 0

        if choice == 1:
            self.strength += 2
            print(f"Upgraded strength by 2 points, your strength is now {self.strength}")
        elif choice == 2:
            self.dexterity += 2
            print(f"Upgraded dexterity by 2 points, your dexterity is now {self.dexterity}")
        elif choice == 3:
            self.constitution += 2
            print(f"Upgraded constitution by 2 points, your constitution is now {self.constitution}")
        elif choice == 4:
            self.intellect += 2
            print(f"Upgraded intellect by 2 points, your intellect is now {self.intellect}")
        elif choice == 5:
            self.wisdom += 2
            print(f"Upgraded wisdom by 2 points, your wisdom is now {self.wisdom}")
            
