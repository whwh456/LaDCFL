def aggregate(models):
    state=models[0].state_dict()

    for k in state:
        state[k]=sum(
            m.state_dict()[k]
            for m in models
        )/len(models)

    return models[0]