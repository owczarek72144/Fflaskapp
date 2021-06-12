from AzureDB import AzureDB

AzureDB().azureAddData()

with AzureDB() as a:
    data = a.azureGetAllData();
    for result in data:
        print(result)
