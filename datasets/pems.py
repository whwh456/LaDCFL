import pandas as pd

def load_pems(path):
    data=pd.read_csv(path)
    return data


def partition_clients(data, num_clients):
    size=len(data)//num_clients
    return [
        data[i*size:(i+1)*size]
        for i in range(num_clients)
    ]