
def earliest_ancestor(ancestors, starting_node):
    ancestry = {}

    for person in ancestors:
        if person[1] not in ancestry:
            ancestry[person[1]] = set()

    for person in ancestors:
        ancestry[person[1]].add(person[0])

    print(f'ancestry: {ancestry}')

    def dfs_recursive(starting_person, visited=[], distance=0, family=[]):

        visited.append(starting_person)

        if starting_person not in ancestry:
            family.append({starting_person: (starting_person, distance)})
        else:
            for person in ancestry[starting_person]:
                if person not in visited:
                    family.append(
                        {starting_person: (starting_person, distance)})
                    dfs_recursive(
                        person, visited, distance + 1, family)
        return family

    family = dfs_recursive(starting_node)
    print(f'family: {family}')
    earliest = 0
    i = 0
    tupple_family = []
    for person in family:
        for key in person:
            tupple_family.append(person[key])
    for person in tupple_family:
        if person[1] == 0 and len(family) == 1:
            return -1
        else:
            earliest = i
        i += 1

    return tupple_family[earliest][0]
