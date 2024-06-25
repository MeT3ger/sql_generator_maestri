import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk

def clear(str):
    str = str.replace(',','').replace('[', '').replace(']', '').replace('\n', '')
    return str

filenames = {
    "json": [
        "./nofuzzi/json_services.txt",
        "./nofuzzi/json_services_big.txt",
        "fuzzy/json_services_fuzzy.txt",
        "fuzzy/json_services_big_fuzzy.txt",
        "fuzzy/json_services_only_fuzzy_100000.txt"
        ],
    "simple": [
        "nofuzzi/simple_services.txt",
        "nofuzzi/simple_services_big.txt",
        "fuzzy/simple_services_fuzzy.txt",
        "fuzzy/simple_services_big_fuzzy.txt",
        "fuzzy/simple_services_only_fuzzy_100000.txt"
        ],
    "table": [
        "nofuzzi/table_services.txt",
        "nofuzzi/table_services_big.txt",
        "fuzzy/table_services_fuzzy.txt",
        "fuzzy/table_services_big_fuzzy.txt",
        "fuzzy/table_services_only_fuzzy_100000.txt"
    ]
}

titles = [
    'no fuzzi no big table',
    'no fuzzi big table',
    'fuzzi no big table',
    'fuzzi big table',
    'different similarity'
]

xlabels = [
    'кол-во записей',
    'кол-во записей',
    'кол-во записей',
    'кол-во записей',
    'степень похожести'
]

for i in range(0, 5):
    result = []
    with open(filenames['json'][i], 'r') as f:
        json_services = [list(map(float, (clear(i).split(' ')))) for i in f]

    with open(filenames['simple'][i], 'r') as f:
        simple_services = [list(map(float, (clear(i).split(' ')))) for i in f]

    with open(filenames['table'][i], 'r') as f:
        table_services = [list(map(float, (clear(i).split(' ')))) for i in f]
    
    x = [i[0] for i in simple_services]
    y_json = [i[1] for i in json_services]
    y_simple = [i[1] for i in simple_services]
    y_table = [i[1] for i in table_services]

    with plt.style.context('cyberpunk'):
        plt.plot(x, y_json, '-')
        plt.plot(x, y_simple, '-')
        plt.plot(x, y_table, '-.')
        plt.xlabel(xlabels[i])
        plt.legend(["json", "base", "table"])
        plt.ylabel('длительность поиска ms')
        plt.title(titles[i])
        plt.show()