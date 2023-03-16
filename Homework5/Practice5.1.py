def down (string):
	return string.lower()


def up (string):
	return string.upper()


list_str = "HDHDH figHt".split()
print(list(map(down, list_str)))
print(list(map(up, list_str)))

