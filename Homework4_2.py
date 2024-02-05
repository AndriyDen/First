def get_cats_info(path: str):

    try:
        with open(path, 'r', encoding = "utf-8") as anim:
            all_lines = [line.strip() for line in anim.readlines()]
       
    except Exception:
        print("Oopsie, the file is missing or damaged")
        quit()
    
    cats_data = []

    for el in all_lines:
        a = el.split(",")
        cats_data.append({"id": a[0], "name": a[1], "age": a[2]})
    
    return cats_data

# cats_info = get_cats_info("animals.txt")
# print(cats_info)
