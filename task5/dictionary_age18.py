people = {
    "pooja": 18,
    "xxx": 25,
    "yyyy": 18,
    "zzzz": 20,
    "jenefa": 18,
    "joziah": 17
}

if not all(isinstance(age, int) for age in people.values()):
    raise ValueError("All ages must be integers.")

# Use filter with lambda to get only entries where age == 18
filtered_dict = dict(filter(lambda item: item[1] == 18, people.items()))

# Output the result
print("People with age 18:", filtered_dict)