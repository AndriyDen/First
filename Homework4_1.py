def total_salary(path: str):

    try:
        with open(path, 'r', encoding = "utf-8") as sal:
            all_lines = [line.strip() for line in sal.readlines()]
    
    except Exception:
        print("Oopsie, the file is missing or damaged")
        quit()

    salary_values = []

    for el in all_lines:
        a = el.split(",")
        salary_values.append(int(a[1]))
        
    total_salary = sum(salary_values)
    average_salary = int(total_salary / len(salary_values))
        
    return (total_salary, average_salary)

# path_to_file = "salaries.txt"
# salary = total_salary(path_to_file)
# print(f"Загальна сума заробітної плати: {salary[0]}, Середня заробітна плата: {salary[1]}")
