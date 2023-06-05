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
    

with open(clean_json_prefix+filenames[2]) as file:
    k = json.load(file)
    print(len(k))