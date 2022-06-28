import itertools
card = "5133-3467-8912-3456"

if (len(card.split('-')) == 1 and len(card) == 16) or (len(card.split('-')) == 4 and
                                                       all(len(i) == 4 for i in card.split("-"))):

    card = card.replace("-", "")
    try:
        int(card)
        if max(len(list(g)) for _, g in itertools.groupby(card)) > 3:
            print("Failed: 4+ repeated digits")
        else:
            print("Passed")
    except ValueError as e:
        print("Failed: non-digit characters")
else:
    print("Failed: bad hyphens or length")
