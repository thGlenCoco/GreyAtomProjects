# Code starts here
# Create the lists
class_1 = ["Geoffrey Hinton", "Andrew Ng", "Sebastian Raschka", "Yoshua Bengio"]
class_2 = ["Hilary Mason", "Carla Gentry", "Corinna Cortes"]

# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)

# Append the list
new_class.append("Peter Warden")

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")

# Print the list
print(new_class)

# Create the Dictionary
courses = dict()

# Slice the dict and stores  the all subjects marks in variable
courses["Math"] = 65
courses["English"] = 70
courses["History"] = 80
courses["French"] = 70
courses["Science"] = 60

# Store the all the subject in one variable `Total`
total = sum(courses.values())

# Print the total
print(total)

# Insert percentage formula
percentage = total/500

# Print the percentage
print(percentage)

# Create the Dictionary
mathematics = dict()
mathematics["Geoffrey Hinton"] = 78
mathematics["Andrew Ng"] = 95
mathematics["Sebastian Raschka"] = 65
mathematics["Yoshua Benjio"] = 50
mathematics["Hilary Mason"] = 70
mathematics["Corinna Cortes"] = 66
mathematics ["Peter Warden"] = 75

# Given string
topper = max(mathematics,key = mathematics.get)

# Create variable first_name
first_name, last_name = topper.split()

# Create variable Last_name and store last two element in the list
# Concatenate the string
full_name = last_name + " " + first_name

# print the full_name
certificate_name = full_name.upper()

# print the name in upper case
print(certificate_name)

# Code ends here
