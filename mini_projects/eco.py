import requests
link = requests.get("https://web.stanford.edu/class/ee380/Abstracts/140129-slides-Machine-Learning-and-Econometrics.pdf")
print(link)
with open("econmetrics+machinelearningSTANFORD.pdf", 'wb') as pd:   # use 'wb' since we're downloading from the net
    pd.write(link.content)