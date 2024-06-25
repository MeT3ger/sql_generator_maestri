from Database import *
from Inserter import *
from Searcher import *


database = Database()
database.connect()
database.database_creator()

# result_simple_ser = []
# result_json = []
# result_table = []

# for i in range(0, 110000, 100000):
#     inserter = Inserter(database=database)
#     database.database_deleter()
#     database.database_creator()

#     for _ in range(i):
#         inserter.service()
#         inserter.service_jsonb()
#         inserter.service_table()
#     searcher = Searcher(database=database)

#     services_times = []
#     titles_times = []
#     services_jsonb = []

#     for j in range(100):
#         services_times.append(
#             searcher.service(word="dxlwcqbzfo", fuzzy=True, similarity=0.1)[0]
#         )
#         titles_times.append(
#             searcher.titles(word="dxlwcqbzfo", fuzzy=True, similarity=0.1)[0]
#         )
#         services_jsonb.append(
#             searcher.service_jsonb(word="dxlwcqbzfo", fuzzy=True, similarity=0.1)[0]
#         )
    
#     # result_simple_ser.append([i, sum(services_times)/len(services_times)])
#     # result_json.append([i, sum(services_jsonb)/len(services_jsonb)])
#     # result_table.append([i, sum(titles_times)/len(titles_times)])
#     result_simple_ser += [sum(services_times)/len(services_times)] + services_times 
#     result_table += [sum(titles_times)/len(titles_times)] + titles_times
#     result_json += [sum(services_jsonb)/len(services_jsonb)] + services_jsonb

# with open('simple_info_100000_fuzzy.txt', 'w') as f:
#     f.writelines(f"{item}\n" for item in result_simple_ser)

# with open('table_info_100000_fuzzy.txt', 'w') as f:
#     f.writelines(f"{item}\n" for item in result_table)

# with open('json_info__100000_fuzzy.txt', 'w') as f:
#     f.writelines(f"{item}\n" for item in result_json)


# result_simple_ser = []
# result_json = []
# result_table = []

# inserter = Inserter(database=database)
# database.database_deleter()
# database.database_creator()

# for _ in range(100000):
#     inserter.service()
#     inserter.service_jsonb()
#     inserter.service_table()
# searcher = Searcher(database=database)

# services_times = []
# titles_times = []
# services_jsonb = []

# for j in range(0,21):
#     for _ in range(0,100):
#         services_times.append(
#             searcher.service(word="dxlwcqbzfo", fuzzy=True, similarity=(j/20.0))[0]
#         )
#         titles_times.append(
#             searcher.titles(word="dxlwcqbzfo", fuzzy=True, similarity=(j/20.0))[0]
#         )
#         services_jsonb.append(
#             searcher.service_jsonb(word="dxlwcqbzfo", fuzzy=True, similarity=(j/20.0))[0]
#         )
    
#     result_simple_ser.append([(j/20.0), sum(services_times)/len(services_times)])
#     result_json.append([(j/20.0), sum(services_jsonb)/len(services_jsonb)])
#     result_table.append([(j/20.0), sum(titles_times)/len(titles_times)])

# with open('simple_services_only_fuzzy_100000.txt', 'w') as f:
#     f.writelines(f"{item}\n" for item in result_simple_ser)

# with open('table_services_only_fuzzy_100000.txt', 'w') as f:
#     f.writelines(f"{item}\n" for item in result_table)

# with open('json_services_only_fuzzy_100000.txt', 'w') as f:
#     f.writelines(f"{item}\n" for item in result_json)

