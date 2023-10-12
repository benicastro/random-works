requests = [
    # "https://api.example.com/resource2/id/resource3/id2",
    # "https://api.example.com/resource3",
    # "https://api.example.com/resource2/id/",
    # "https://api.example.com/resource1/id/resource3/id2",
    "https://api.example.com/resource6/resource21",
    "https://api.example.com/resource951/id60/resource115",
    "https://api.example.com/resource535/id52/id57/id53",
]

result = []

for request in requests:
    start_index = request.index("r")
    mod_request = request[start_index:]
    split_request = mod_request.split("/")

    initial_result = []

    for elem in split_request:
        if "resource" in elem:
            initial_result.append(elem)

    result.append("/".join(initial_result))

final_result = []
num_slash = 0

while len(final_result) != len(result):
    temp_list = []
    for elem in result:
        if elem.count("/") == num_slash:
            temp_list.append(elem)
    temp_list.sort()
    final_result.extend(temp_list)
    num_slash += 1

print(final_result)
