import openpyxl

creds=openpyxl.load_workbook("SeleniumProject.xlsx")
login_creds=creds["login_creds"]
credentials=[]
for row in range(1,4):
    nested_creds=[]
    for column in range(1,3):
        data=login_creds.cell(row,column)
        nested_creds.append(data.value)

    credentials.append(nested_creds)


print(credentials)