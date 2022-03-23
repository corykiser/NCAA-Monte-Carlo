import csv


with open('wpw.csv', newline='') as f:
    reader2 = csv.reader(f)
    wpwdata = list(reader2)
#wpw_raw = np.array(data)[2:]
    
wpwlist = []
for i in range(len(wpwdata)):
    wpwlist.append(wpwdata[i][0])

print(wpwlist)