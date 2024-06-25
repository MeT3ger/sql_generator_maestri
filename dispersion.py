result = []
with open("json_info__100000_fuzzy.txt", 'r') as f:
    json_services = [float(i) for i in f]

with open("simple_info_100000_fuzzy.txt", 'r') as f:
    simple_services = [float(i) for i in f]

with open("table_info_100000_fuzzy.txt", 'r') as f:
    table_services = [float(i) for i in f]
    
averages = [json_services.pop(0), simple_services.pop(0), table_services.pop(0)]
tables = [json_services, simple_services, table_services]
result = ["json", "simple", "table"]

for j in range(3):
    deviation = 0
    for i in tables[j]:
        deviation += (i - averages[j])**2

    deviation/=(len(tables[j]) - 1)
    deviation = deviation ** (1.0/2.0)
    print(result[j] + " " + str(deviation))