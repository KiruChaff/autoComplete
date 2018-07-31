import re
def auto_complete(str, qStrings):
    toSearch = ""
    result=[]
    ## Composing a easier-to-process-String out of the query input (seperated with newlines)
    for query in qStrings:
        toSearch+=query+"\n"
    ## using the regularExpression library re to get result
    matches=re.compile(str+'.*').finditer(toSearch)
    ## matches is an array of objects
    for match in matches:
        result.append(match.group())
    return result
print(auto_complete('de',['dog', 'deer', 'deal']))

##--------------------------------------##
## output:
## >>>['deer', 'deal']
