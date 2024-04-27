import json

FILEPATH = ""


def get_todos():
    data = {
        "text": 0,
        "tooltip": ""
    }

    with open(FILEPATH, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line:
                data['text'] += 1
                data['tooltip'] += f"{line_number}. {line}"

    data["text"] = str(data["text"])
    data["tooltip"] = data["tooltip"].rstrip()

    return data


print(json.dumps(get_todos()))
