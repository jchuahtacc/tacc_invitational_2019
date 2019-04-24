input = open("../sample_data/oversubscribed.txt", "r")
lines = input.readlines()
hour_totals = [{"Stampede2": 4200, "LoneStar5": 1252, "Hikari": 432} for i in range(1, 24)]
oversubscribed = []

for line in lines[1:]:
    parts = [l.strip() for l in line.split(',')]
    system = parts[0]
    start_hour = int(parts[1].split(':')[0])
    end_hour = start_hour + int(parts[2])
    sus = int(parts[3])
    for i in range(start_hour, end_hour):
        hour_totals[i-1][system] -= sus

for d in hour_totals:
    for k, v in d.items():
        if v < 0 and k not in oversubscribed:
            oversubscribed.append(k)

for i in oversubscribed:
    print(i)