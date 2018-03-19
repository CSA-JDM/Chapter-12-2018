# Jacob Meadows
# 4th Period, Computer Programming
# March 2nd, 2018
"""
General Solution: Counting All Letters
Now we will generalize the counting problem and consider how to count the number of times each letter appears in a given
string. In order to do this we need to realize that writing a function that returns a single integer will no longer
work. Instead we will need to return some kind of collection that holds the counts for each character.

Although there may be many possible ways to do this, we suggest a dictionary where the keys of the dictionary will be
the letters in the string and the associated values for each key will be the number of times that the letter appeared.

What about a letter that does not appear in the string? It will never be placed in the dictionary. By assumption, any
key that is not in the dictionary has a count of 0.
"""


def count_all(given):
    letter_count = {}
    lines = given.split("\n")
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] in letter_count:
                if x in letter_count[lines[x][y]][1]:
                    letter_count[lines[x][y]] = [letter_count[lines[x][y]][0] + 1, letter_count[lines[x][y]][1]]
                    letter_count[lines[x][y]][1][x].append(y)
                elif x not in letter_count[lines[x][y]][1]:
                    letter_count[lines[x][y]] = [letter_count[lines[x][y]][0] + 1, letter_count[lines[x][y]][1]]
                    letter_count[lines[x][y]][1][x] = [y]
            elif lines[x] not in letter_count:
                letter_count[lines[x][y]] = [1, {x : [y]}]
    new_string = ""
    t = 0
    while new_string != given:
        for x in letter_count:
            for y in letter_count[x][1]:
                if y == new_string.count("\n"):
                    for u in range(len(letter_count[x][1][y])):
                        if new_string.count("\n") == 0:
                            if letter_count[x][1][y][u] == len(new_string):
                                new_string += x
                                if x == ".":
                                    new_string += "\n"
                        elif new_string.count("\n") > 0:
                            r = new_string.find("\n")
                            if y != 1:
                                for _ in range(y):
                                    r = new_string.find("\n", r+1)
                            if letter_count[x][1][y][u] == len(new_string[r+1:]):
                                new_string += x
                                if x == ".":
                                    new_string += "\n"
        t += 1
        if t > 999:
            break
    print(letter_count)
    print(new_string)


count_all("""Prior to 1871 unification, the German states lacked naval power and had no direction towards the development of a navy, thus preventing any German participation in earlier imperial conquests of colonial territories.
Weltpolitik, or “place in the sun,” was an imperial foreign policy adopted by the German Empire to combat the procurement of a small navy and colonies; its purpose was to transform Germany into a global power.
The defensive policy that the Weltpolitik caused the separation of was the Realpolitik: politics or diplomacy based primarily on considerations of given circumstances and factors, rather than explicit ideological notions or moral and ethical premises.
For both the colonizing power of Germany and the colonized regions it controlled, extreme changes and consequences were forced upon them.
In Germany’s case, it had the heavy task of handling, controlling, and “investing” into the territories it dominated.
The invaded lands experienced major changes and alterations of their culture, language, geography, and way of life that they were so used to.
In Germany’s conquest of Africa and Asia, it discovered and documented new areas and geographic landmarks that were previously unknown to the rest of Europe.""")
