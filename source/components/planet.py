
import GameObject,RigidBody


class Planet(RigidBody.RigidBody):

    def collide_with_player(self,player):
        print("Colisão com planeta")
        print("Derrota")
        player.got_hit(self)

    def __init__(self, name, image, mass, pos, G):
        RigidBody.RigidBody.__init__(self, name, image, mass, pos, G)
