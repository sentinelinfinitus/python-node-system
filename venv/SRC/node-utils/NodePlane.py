

def node_plane () :
    scatter = Scatter(do_rotation=False)


def node_plane_background ():

    def build(self):
        self.texture = Image(source='NodePlaneBG.png').texture
        self.texture.wrap = 'repeat'
        self.texture.uvsize = (8, 8)

