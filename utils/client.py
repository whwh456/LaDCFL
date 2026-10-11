class Client:

    def __init__(self,id,data=None):
        self.id=id
        self.data=data
        self.latency=(id%10)+1

    def train(self,model,epochs):
        return model