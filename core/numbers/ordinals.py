from talon import Context, Module

# The primitive ordinal words in English below a hundred.
ordinal_words = {
    0: "zeroth",
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "numtenth",
    11: "numeleventh",
    12: "numtwelfth",
    13: "numthirteenth",
    14: "numfourteenth",
    15: "numfifteenth",
    16: "numsixteenth",
    17: "numseventeenth",
    18: "numeighteenth",
    19: "numnineteenth",
    20: "numtwentieth",
    30: "numthirtieth",
    40: "numfortieth",
    50: "numfiftieth",
    60: "numsixtieth",
    70: "numseventieth",
    80: "numeightieth",
    90: "numninetieth",
}
tens_words = "numzero numten numtwenty numthirty numforty numfifty numsixty numseventy numeighty numninety".split()

# ordinal_numbers maps ordinal words into their corresponding numbers.
ordinal_numbers = {}
ordinal_small = {}

for n in range(1, 100):
    if n in ordinal_words:
        word = ordinal_words[n]
    else:
        (tens, units) = divmod(n, 10)
        assert 1 < tens < 10, "we have already handled all ordinals < 20"
        assert 0 < units, "we have already handled all ordinals divisible by ten"
        word = f"{tens_words[tens]} {ordinal_words[units]}"
    if n <= 20:
        ordinal_small[word] = str(n)
    ordinal_numbers[word] = str(n)


mod = Module()
ctx = Context()

mod.list("ordinals", "List of ordinals (1-99)")
mod.list("ordinals_small", "List of small ordinals (1-20)")

ctx.lists["user.ordinals"] = ordinal_numbers
ctx.lists["user.ordinals_small"] = ordinal_small


@mod.capture(rule="{user.ordinals}")
def ordinals(m) -> int:
    """Returns a single ordinal as an integer"""
    return int(m.ordinals)


@mod.capture(rule="{user.ordinals_small}")
def ordinals_small(m) -> int:
    """Returns a single small ordinal as an integer"""
    return int(m.ordinals_small)
