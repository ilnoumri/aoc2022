def open_file(path, strip=True):
    with open(path) as f:
        lines = f.readlines()
    return [line.strip() if strip else line.replace("\n", "") for line in lines]