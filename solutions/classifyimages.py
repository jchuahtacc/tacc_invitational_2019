# input = open("../student/classifyimages.txt", "r")
input = open("../sample_data/classifyimages2.txt", "r")
lines = input.readlines()
systems = []
TOTAL_SUs = 50000

for line in lines:
    parts = [s.strip() for s in line.split(',')]
    systems.append({'name': parts[0], 'images': int(parts[1]), 'sus': int(parts[2])})

def max_images(systems, idx, balance, nbr_jobs):
    if balance == 0 or idx == 0:
        return 0
    if systems[idx]['sus']*nbr_jobs > balance:
        if nbr_jobs == 1:
            return max_images(systems, idx-1, balance, 3)
        else:
            return max_images(systems, idx, balance, nbr_jobs-1)
    images = systems[idx]['images']
    if nbr_jobs == 1:
        return max(images + max_images(systems, idx-1, balance-systems[idx]['sus'], 3),
                   max_images(systems, idx-1, balance, 3))
    else:
        return max(images + max_images(systems, idx, balance-systems[idx]['sus'], nbr_jobs-1),
                   max_images(systems, idx-1, balance, nbr_jobs-1))

max = max_images(systems, len(systems)-1, TOTAL_SUs, 3)
print(max)