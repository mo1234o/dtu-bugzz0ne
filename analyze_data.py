import json

with open('db.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

programs = set()
years = set()
levels = set()

for student in data.values():
    for year_key, year_info in student.get('years', {}).items():
        programs.add(year_info.get('p', ''))
        levels.add(year_info.get('l', ''))
        years.add(year_key)

print('Programs:', sorted(programs))
print('Levels:', sorted(levels))
print('Years:', sorted(years))
print('Total students:', len(data))
