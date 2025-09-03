# W8_Task:8 - Mini Project 8
# Custom Data Serialization Tool
# Format Example: person{name:Ekta;age:25;address{city:Delhi;pin:110001;}}

def serialize(data, name="root"):
    """Convert dictionary data into custom serialized string format."""
    if isinstance(data, dict):
        return f"{name}{{" + "".join(serialize(v, k) for k, v in data.items()) + "}}"
    else:
        return f"{name}:{data};"

def deserialize(text):
    """Convert custom serialized string back into dictionary format."""
    stack, curr = [], {}
    key, val, reading_key, reading_val = "", "", True, False

    for ch in text:
        if ch == "{":
            stack.append((curr, key))
            curr = {}
            key = ""
        elif ch == "}":
            parent, pname = stack.pop()
            parent[pname] = curr
            curr = parent
        elif ch == ":":
            reading_key, reading_val = False, True
        elif ch == ";":
            curr[key] = val
            key, val, reading_key, reading_val = "", "", True, False
        elif reading_key:
            key += ch
        elif reading_val:
            val += ch
    return curr

# ------------------ Example Run ------------------
if __name__ == "__main__":
    # Original dictionary data
    data = {
        "person": {
            "name": "Ekta",
            "age": 25,
            "address": {
                "city": "Delhi",
                "pin": 110001
            }
        }
    }

    # Serialize dictionary -> string
    serialized_str = serialize(data, "root")
    print("Serialized Data:")
    print(serialized_str)

    # Deserialize string -> dictionary
    deserialized_dict = deserialize(serialized_str)
    print("\nDeserialized Data:")
    print(deserialized_dict)
