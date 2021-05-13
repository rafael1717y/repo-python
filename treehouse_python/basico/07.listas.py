languages = ["Python", "JavaScript", "Java"]
len(languages)

banner = list("Congratulations")
print(banner)

attendees = ["Ken", "Alena", "Ray"]
attendees.append("Ashley")
attendees.extend(["James", "Gull"])
optional_invites = ["Ben" , "Jave"]
potential_attendees = attendees + optional_invites


print("There are", len(potential_attendees), "potential attendees currently.")

temperatures = []
temperatures.append(98.6)
temperatures.append(99.4)
print(temperatures)

er_temps = [102.2, 103.5, 101.1, 99.9]

temperatures.extend(er_temps)
print(temperatures)

primary_care_doctors = ["Dr. Scholls", "Dr. Popper"]
er_doctors = ["Doug", "Susan"]

all_doctors = primary_care_doctors + er_doctors
print(all_doctors)

temperatures.append("burning up")
print(temperatures)

for attendees in attendees:
    print(attendees)

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invites)
print("To: " + to_line)
print("Cc: " + cc_line)

print(to_line).split(", ")





