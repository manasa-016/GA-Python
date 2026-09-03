# Customer Profile Program

# Input
name = input("Enter customer name: ").strip()
email = input("Enter email address: ").strip().lower()
phone = input("Enter phone number: ").strip()

# Format name
name = name.title()

# Validate name
if not name.replace(" ", "").isalpha():
    print("Invalid customer name")
    exit()

# Validate email
if "@" not in email or "." not in email:
    print("Invalid email")
    exit()

# Validate phone
if not phone.isdigit() or len(phone) != 10:
    print("Invalid phone number")
    exit()

# Extract email domain
domain = email.split("@")[1]

# Mask phone number
masked_phone = "******" + phone[-4:]

# Generate customer ID
customer_id = (
    name.replace(" ", "").upper()[:4]
    + phone[-4:]
)

# Display result
print("\n================================")
print("        CUSTOMER PROFILE")
print("================================")

print(f"Customer ID : {customer_id}")
print(f"Name        : {name}")
print(f"Email       : {email}")
print(f"Domain      : {domain}")
print(f"Phone       : {masked_phone}")