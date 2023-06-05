import json

raw_prefix = "./raw/"
clean_json_prefix = "./clean_json/"
filenames = ["eurusd_1min_data1.txt", "eurusd_1min_data2.txt", "eurusd_1min_data3.txt"]

# with open(raw_prefix+filenames[2]) as file:
#     file = file.read()
#     file = file.replace("'", '"').replace("][", ",")
#     data = json.loads(file)
#     out_file_path = clean_json_prefix + filenames[2]
#     with open(out_file_path, "w") as file2:
#         json.dump(data, file2)

store = []

dates = set()

# for filename in filenames:
#     with open(clean_json_prefix+filename) as file:
#         k = json.load(file)
#         store = store + k


repeated_dates = []
store2 = []

for row in store:
    date = row["date"]
    if date not in dates:
        dates.add(date)
        store2.append(row)
    else:
        print("Fuck!")
        repeated_dates.append(date)

print(len(store))
print(len(store2))

with open("combined_repeated_removed/"+"combined.json", "w") as file3:
    json.dump(store2, file3)
