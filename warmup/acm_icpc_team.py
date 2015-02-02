def findTeams(n, m, a):
    max_topics = 0
    max_teams = 0
    for i, topics1 in enumerate(a):
        for _, topics2 in enumerate(a[i+1:]):
            t1 = int(topics1, 2)
            t2 = int(topics2, 2)
            topics = bin(t1 | t2).count("1")
            if (topics > max_topics):
                max_topics = topics
                max_teams = 1
            elif (topics == max_topics):
                max_teams += 1
     
    return max_teams, max_topics

n, m = [int(inp) for inp in input().split(" ")]
a = [input() for i in range(n)]
teams, topics = findTeams(n, m, a)
print(topics)
print(teams)
