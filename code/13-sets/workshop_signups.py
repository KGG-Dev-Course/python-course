python_signups = ["maya", "Leo", "sam", "Maya", "ana", "leo"]
web_signups = ["Sam", "ana", "Zoe", "ana", "Kai"]

# Clean up names and remove duplicates in one go
python_group = set()
for name in python_signups:
    python_group.add(name.strip().title())

web_group = set()
for name in web_signups:
    web_group.add(name.strip().title())

print(f"Python workshop ({len(python_group)}): {sorted(python_group)}")
print(f"Web workshop ({len(web_group)}): {sorted(web_group)}")

both = python_group & web_group
everyone = python_group | web_group
python_only = python_group - web_group

print(f"Signed up for both: {sorted(both)}")
print(f"Total people: {len(everyone)}")
print(f"Python only: {sorted(python_only)}")

cancel = input("Who wants to cancel? ").strip().title()
python_group.discard(cancel)
web_group.discard(cancel)
print(f"Python workshop now: {sorted(python_group)}")
print(f"Web workshop now: {sorted(web_group)}")
