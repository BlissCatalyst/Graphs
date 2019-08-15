
def earliest_ancestor(ancestors, starting_node):
    ancestry = {}

    for person in ancestors:
        if person[1] not in ancestry:
            ancestry[person[1]] = set()

    for person in ancestors:
        ancestry[person[1]].add(person[0])

    # print(f'ancestry: {ancestry}')

    def dfs_recursive(starting_person, visited=[], distance=0, family=[]):
        # print(f'STARTING_PERSON: {starting_person}')
        visited.append(starting_person)

        if starting_person not in ancestry:
            family.append({starting_person: (starting_person, distance)})
        else:
            for person in ancestry[starting_person]:
                if person not in visited:
                    family.append(
                        {person: (person, distance)})
                    if person in ancestry:
                        dfs_recursive(
                            person, visited, distance + 1, family)
                    else:
                        dfs_recursive(person, visited, distance)
                elif person in visited and person not in family:
                    family.append({person: (person, distance)})

        return family

    family = dfs_recursive(starting_node)
    # print(f'family: {family}')
    earliest = 0
    i = 0
    distance = 0
    lower_person = 11
    tupple_family = []
    for person in family:
        for key in person:
            tupple_family.append(person[key])
    # print(f'tupple_family: {tupple_family}')
    for person in tupple_family:
        if person[1] == 0 and len(family) == 1:
            return -1
        elif person[1] >= distance:
            distance = person[1]
            if person[0] <= lower_person:
                earliest = i
                lower_person = person[0]
            else:
                earliest = i

        i += 1

    # print(f'***** ANSWER ***** = {tupple_family[earliest][0]}\n')
    return tupple_family[earliest][0]
