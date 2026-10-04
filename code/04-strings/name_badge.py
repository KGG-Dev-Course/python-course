raw_name = "   ada LOVELACE  "
role = "guest speaker"

name = raw_name.strip().title()
initials = name[0] + name[4]
badge_line = f"{name} - {role.upper()}"

print(badge_line)
print("-" * len(badge_line))
print(f"Initials: {initials}")
print(f"Name length: {len(name)} characters")
print(f"First name: {name[:3]}")
print(f"Short role: {role.replace('guest ', '')}")
