class CoLogDyn:

    def __init__(self,K,threshold=0.2):
        self.K=K
        self.threshold=threshold

    def imbalance(self,groups):
        latency=[
            max(c.latency for c in g)
            for g in groups
        ]
        return max(latency)/sum(latency)*len(latency)-1

    def cluster(self,clients):
        clients=sorted(
            clients,
            key=lambda x:x.latency
        )

        groups=[[] for _ in range(self.K)]

        for i,c in enumerate(clients):
            groups[i%self.K].append(c)

        return groups