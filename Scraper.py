from BeautifulSoup import BeautifulSoup
import requests

#it tries to see if the given word was found in the idea page of each organization if yes, it prints it out. for any error it just skips that idea page
check_term = 'scraping"

#reads all the orgs details
links = open ("List.txt").read()


listlink = links.split('\n')
for line in listlink[1:]:
    link = line.split(",")[-1]
    print "---" + link
    
    try:
        data = requests.get(link).content
        if check_term in data.lower():
            print "@@@@@@@@@@@Found in : " + link
    except:
        print "#####Errpr in " + link
