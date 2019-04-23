import GameObject



class Platform(GameObject.GameObject):
    def collide_with_player(self,player):
        print("Colisão com plataforma")
        if(self.platFinal==True):
            player.final=True
            print("Vitória")
            player.collide_with_solid()


    def __init__(self,name,image,pos,platFinal = False):
        GameObject.GameObject.__init__(self,name,image,pos)
        self.platFinal = platFinal

