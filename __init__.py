import csv

class Krontos:
    def __init__(self):
        self.all_mechants = [] #All available merchants.
        self.all_pincodes = [] #All available pincodes(no duplicates).
        self.Mer_Pin = {} #Dict consisting of merchants with respect to their available merchants.

        #Table
        self.Table = []
    
    def getDataset(self, file):
        data = {}
        with open(file, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the header 
            for header in headers:
                data[header] = []  # empty list for header
            for row in reader:
                for index, value in enumerate(row):
                    data[headers[index]].append(int(value))
        self.Mer_Pin = data
        return 0 #if no error.

    def getDataset(self, filename):
        data = {}
        with open(filename, "r") as file_object:
            rows = csv.reader(file_object)
            for row in rows:
                data[row[0]] = [int(ele) for ele in row[1:]]
        return 0 #if no error.

    def pincodeStat(self, merchant, pincode):
        #To find weather a pincode is positive.
        #Fetching from universal list and into Table.
        merID = self.all_mechants.index(merchant) #Getting merchant's index number representing as ID.
        pinID = self.all_pincodes.index(pincode) #Getting pincode's index number representing as ID.
        stat = self.Table[merID][pinID]
        return stat #1 if exists, 0 not exists.

    def createTable(self):
        print("[ TABLE ] Getting data information.")
        #Organize all the information.
        merchants = self.Mer_Pin.keys() #Getting all the merchants.
        pincodes = self.Mer_Pin.values() #Getting all the pincodes.

        #Add all merchants to a universal list and sort it.
        for merchant in merchants:
            self.all_mechants.append(merchant)
        self.all_mechants.sort()

        #All all the pincodes to universal list and sort it.
        for pincode in pincodes:
            self.all_pincodes += pincode
        self.all_pincodes.sort()
        x = []
        for i in self.all_pincodes:
            if i not in x:
                x.append(int(i))
        x.sort()
        self.all_pincodes = x

        #Create a empty table with all cells as None value.
        print("[ TABLE ] Empty rows and columns creating... ")
        no_of_merchants = len(self.all_mechants)
        no_of_pincodes = len(self.all_pincodes)

        for m in range(no_of_merchants):
            mer = []
            for p in range(no_of_pincodes):
                mer.append(None)
            self.Table.append(mer)
            print(f"[ TABLE ] Merchant {m+1} created.")
        print("[ TABLE ] Created empty table.")
        return 0 #0 if no error.
    
    def updateTable(self):
        print("[ TABLE UPDATION ] Updating table...")
        for i in range(len(self.all_mechants)):
            for j in range(len(self.all_pincodes)):
                if self.all_pincodes[j] in self.Mer_Pin[self.all_mechants[i]]:
                    self.Table[i][j] = 1
                else:
                    self.Table[i][j] = 0
            print(f"[ TABLE UPDATION ] merchant {i+1} Done.")
        print("[ TABLE UPDATION ] Updated table successfully.")
        return 0 #if no error.

    def getTable(self):
        return self.Table

#if __name__ == "__main__":
    #Main program runs here.
    #Creating instance of the class.
    #instance1 = Krontos()

    #Convert csv file to dict data format.
    #instance1.getDataset("sample.csv")

    #Creating table.
    #instance1.createTable()
    
    #Get table.
    #print(instance1.getTable())

    #Updating table with metadata.
    #instance1.updateTable()
    #print(instance1.getTable())

    #Checking wheather a pincode is available to ship respective to its merchant.
    #status = instance1.pincodeStat("m1", 3)
    #if status:
    #    print("Available.")
    #else:
    #    print("Not Available.")


#aimrrs
