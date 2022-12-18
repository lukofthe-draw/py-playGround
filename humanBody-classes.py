#template for modeling an organ of the human body
class Organ:
    def __init__(self, name, function, location):
        self.name = name
        self.function = function
        self.location = location

liver = Organ("liver", "filters blood and produces bile", "upper right abdomen")


# including the chemical structure in a different class
class ChemicalStructure:
    def __init__(self, name, function, structure):
        self.name = name
        self.function = function
        self.structure = structure

class Organ:
    def __init__(self, name, function, location, chemical_structures):
        self.name = name
        self.function = function
        self.location = location
        self.chemical_structures = chemical_structures

liver = Organ("liver", "filters blood and produces bile", "upper right abdomen", [ChemicalStructure("bile", "helps digest fats", "C24H40O5")])


#model the atomic weight of elements in order to tie in later.
class Element:
    def __init__(self, name, atomic_weight):
        self.name = name
        self.atomic_weight = atomic_weight

carbon = Element("carbon", 12.0107)
oxygen = Element("oxygen", 15.999)
hydrogen = Element("hydrogen", 1.008)


#create an appendage class, followed by limbs, extremeties, etc.
class Appendage:
    def __init__(self, name, location):
        self.name = name
        self.location = location

eye = Appendage("eye", "face")
ear = Appendage("ear", "side of head")
nose = Appendage("nose", "face")
mouth = Appendage("mouth", "face")

### add variations of this class to encompass the whole
class Hand:
    def __init__(self, name, location, fingers):
        self.name = name
        self.location = location
        self.fingers = fingers

left_hand = Hand("left hand", "left arm", [])
right_hand = Hand("right hand", "right arm", [])


class Finger:
    def __init__(self, name, location):
        self.name = name
        self.location = location

thumb = Finger("thumb", "left hand")
index_finger = Finger("index finger", "left hand")
middle_finger = Finger("middle finger", "left hand")
ring_finger = Finger("ring finger", "left hand")
pinkie = Finger("pinkie", "left hand")


left_hand.fingers.append(thumb)
left_hand.fingers.append(index_finger)
left_hand.fingers.append(middle_finger)
left_hand.fingers.append(ring_finger)
left_hand.fingers.append(pinkie)



