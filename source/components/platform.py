from source import GameObject



class Platform(GameObject.GameObject):
    def collide_with_player(self,player):
        print("Colisão com plataforma")
        if(self.platFinal==True):
            print("Vitória")


    def __init__(self,name,image,pos,platFinal = False):
        GameObject.GameObject.__init__(self,name,image,pos)
        self.platFinal = platFinal

