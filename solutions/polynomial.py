input = open("../sample_data/polynomial.dat", "r")
lines = input.readlines()
polynomial = lines[0]
value = int(lines[1].split('=')[1])

terms = polynomial.split(' ')
total = 0
for term in terms:
    term_coef = 1
    if term[0] == '-':
        term_coef = -1
        term = term[1:]
    elif term[0] == '+':
        term = term[1:]
    exp = 1
    if '^' in term:
        exp = int(term.split('^')[1])
    if 'X' in term:
        try:
            term_coef = term_coef * int(term.split('X')[0])
        except:
            pass
        total = total + term_coef*(value**exp)
    else:
        term_coef = int(term)
        total = total + term_coef

print(total)



