required_skills={
    "Python",
    "SQL",
    "Git"
}
employee_skills={
    "Python",
    "Git",
    "SQL",
    "Docker",
    "AWS"
}
missing_skills=required_skills-employee_skills
extra_skills=employee_skills-required_skills
if required_skills.issubset(employee_skills):
    print("Employee meets all requirements.")

else:
    print("Employee is missing required skills:",missing_skills)

print("Missing skills:",missing_skills)
print("Extra skills:",extra_skills)