from common.libs import (
    pd,np,plt
)

def read_data(dataPath):
    data = pd.read_csv(dataPath)
    return data