thondef clean_text(text):
    return " ".join(text.split())

def save_to_file(data, file_path):
    with open(file_path, "w") as file:
        file.write(data)