"""Find if note can be composed using all words in magazine."""


def check_magazine(magazine, note):
    words = {}

    for i, m in enumerate(magazine):
        if not m in words:
            words[m] = [i]
        else:
            words[m].append(i)

    for n in note:
        if n in words:
            if len(words[n]) == 0:
                print("No")
                return
            else:
                words[n].pop()
        else:
            print("No")
            return

    print("Yes")
