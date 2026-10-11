class FiMoDA:

    def __init__(self,cfg):
        self.cfg=cfg
        self.loss=1.0

    def update(self,loss):
        self.loss=loss

    def schedule(self):

        ratio=max(self.loss,0.01)

        E=int(
            self.cfg['E_max']*ratio
        )

        H=int(
            self.cfg['H_max']*ratio
        )

        return max(E,1),max(H,1)