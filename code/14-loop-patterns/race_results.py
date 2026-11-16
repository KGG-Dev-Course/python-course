runners = ["Maya", "Leo", "Sam", "Ana", "Kai"]
times = [41.5, 39.2, 0, 44.8, 52.3]  # minutes, 0 means did not finish
limit = 50

print("Race results")
for bib, (name, time) in enumerate(zip(runners, times), start=1):
    if time == 0:
        print(f"#{bib} {name}: did not finish")
        continue
    if time <= limit:
        status = "qualified"
    else:
        status = "over the limit"
    print(f"#{bib} {name}: {time:.1f} min ({status})")

search = input("Find a runner: ").strip().title()
found = False
for name, time in zip(runners, times):
    if name == search:
        found = True
        break
if found:
    print(f"{name} finished in {time:.1f} min")
else:
    print(f"No runner called {search}")
