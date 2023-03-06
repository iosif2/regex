import re

data = [
    "abcd 010-1234-5678",
    "acs 010-1234-5678",
    "asbv 010-1234-5678",
]


# pat = re.compile("(\d{3})-(\d{4})-(\d{4})")
pat = re.compile(pattern=r"[a-z]")
for i in data:
    print(pat.sub("\g<1>-****-\g<3>", i))
