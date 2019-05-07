#!/usr/bin/env python

input = open("../sample_data/elasticsearch.dat", "r")
lines = input.readlines()

shards = [ ]
files = { }

for line in lines:
    line = line.strip()
    if line == "SHARD":
        shards.append(
            { }
        )
    elif line.split()[0] == "SEARCH":
        search_terms = line.split()[1:]
        for term in search_terms:
            score = 0
            for shard in shards:
                for filename, terms in shard.items():
                    if term in terms:
                        score = len(terms) - terms.index(term)
                        files[filename] = files[filename] + score
    else:
        tokens = line.split()
        filename = tokens[0]
        files[filename] = 0
        shards[-1][filename] = tokens[1:]

scored_files = [ ]
for filename, score in files.items():
    scored_files.append( (filename, score) )

scored_files.sort(key=lambda item: item[1], reverse=True)
for scored_file in scored_files:
    print(scored_file[0])

