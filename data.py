import pickle
import pandas as pd

class Data:
    def __init__(self):
        self.byteData = pickle.dumps([pd.DataFrame({"Website": [], "Email": [], "Username": [], "Password": []}), pd.DataFrame({"Name": [], "Info": []})])
    
    def getByteData(self) -> bytes:
        return self.byteData