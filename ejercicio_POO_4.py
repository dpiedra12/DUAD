class Head:
    def __init__(self, right_eye, left_eye, nose, mouth): 
        self.right_eye = right_eye
        self.left_eye = left_eye
        self.nose = nose
        self.mouth = mouth


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg,left_leg ):
         
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg =  right_leg
        self.left_leg =  left_leg


class Arm:
    def __init__(self, hand): 
        self.hand= hand

class Hand:
    def __init__(self, fingers): 
        self.fingers = fingers
       


class Leg:
    def __init__(self,thigh, knee, ankle, feet):
        self.thigh = thigh
        self.knee = knee
        self.ankle = ankle
        self.feet =  feet


class Feet:
    def __init__(self, toes, heel): 
        self.toes = toes
        self.heel =  heel
       

class Human():
    def __init__(self, head, torso):
      self.head = head
      self.torso = torso
    

head = Head(right_eye="right_eye",left_eye ="left_eye", nose= "nose", mouth = "mouth")
right_hand = Hand(fingers=5)
left_hand = Hand(fingers=5)
right_arm = Arm(hand= right_hand)
left_arm = Arm(hand= left_hand)
right_feet= Feet(toes=5, heel="heel")
left_feet= Feet(toes=5, heel="heel")
right_leg = Leg(thigh="thigh", knee="knee",ankle="ankle",feet= right_feet)
left_leg = Leg(thigh="thigh", knee="knee",ankle="ankle", feet= left_feet)
torso = Torso(head=head, right_arm=right_arm, left_arm=left_arm,right_leg=right_leg, left_leg=left_leg  )

human = Human(head=head, torso=torso)

