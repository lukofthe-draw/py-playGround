# create a face class that is anatomically correct
class Face:
    def __init__(self, eyes, ears, nose, mouth, eyebrows, forehead, cheeks, chin, jaw):
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.mouth = mouth
        self.eyebrows = eyebrows
        self.forehead = forehead
        self.cheeks = cheeks
        self.chin = chin
        self.jaw = jaw

face = Face(["left eye", "right eye"], ["left ear", "right ear"], "nose", "mouth", ["left eyebrow", "right eyebrow"], "forehead", ["left cheek", "right cheek"], "chin", "jaw")

#basic template for the location of face elements
class Eye:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Ear:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Nose:
    def __init__(self, name):
        self.name = name

class Mouth:
    def __init__(self, name):
        self.name = name

class Eyebrow:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Forehead:
    def __init__(self, name):
        self.name = name

class Cheek:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Chin:
    def __init__(self, name):
        self.name = name

class Jaw:
    def __init__(self, name):
        self.name = name

left_eye = Eye("left eye", "left side of face")
right_eye = Eye("right eye", "right side of face")
left_ear = Ear("left ear", "left side of head")
right_ear = Ear("right ear", "right side of head")
nose = Nose("nose")
mouth = Mouth("mouth")
left_eyebrow = Eyebrow("left eyebrow", "left side of face")
right_eyebrow = Eyebrow("right eyebrow", "right side of face")
forehead = Forehead("forehead")
left_cheek = Cheek("left cheek", "left side of face")
right_cheek = Cheek("right cheek", "right side of face")
chin = Chin("chin")
jaw = Jaw("jaw")

face = Face([left_eye, right_eye], [left_ear, right


