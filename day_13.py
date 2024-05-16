
#Given a list with strings. Leave in this list only those lines that begin with http://.
def filter_http_prefix(strings):
    filtered_strings = [s for s in strings if s.startswith("http://")]
    return filtered_strings