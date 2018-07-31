import re
def auto_complete(str, qStrings):
    toSearch = ""
    result=[]
    for query in qStrings:
        toSearch+=query+"\n"
    matches=re.compile(str+'.*').finditer(toSearch)
    for match in matches:
        result.append(match.group())
    return result
print(auto_complete('de',['dog', 'deer', 'deal']))
