import requests

class Scraper:
    def __init__(self):
        self.people = [] #will be a 1d list of a person's name

    def findMediaTitle(self, url: str, name: str):
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).json()

        dictOfMedia = res["query"]["categorymembers"]

        for media in dictOfMedia:
            if name.lower() in media["title"].lower():
                text = media["title"].replace(" ", "%20")
                return text
        return None

    def findPeople(self, url: str):
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).json()

        data = res["query"]["pages"][0]["revisions"][0]["content"]
        lines = data.split("\n")
        for line in lines:
            if "Trivia" in line:
                break
            if line != "" and line[0] == "*" and "revived" not in line:
                line = (
    line.replace("(", "!")
        .replace(")", "!")
        .replace("[", "!")
        .replace("]", "!")
        .replace("{", "!")
        .replace("}", "!")
        .replace("*", "!")
        ).split("!")
                line = [x for x in line if x != ""]
                line = [x for x in line if x != " "]

                #print(line)
                if len(line) == 1:
                    return False #assume actor name, dont allow
                else:
                    self.people.append(line[1])
                    #return True

        return True

    def removeDuplicates(self):
        seen = [] #temporary hashmap

        for person in self.people:
            if person not in seen and "None" not in person:
                seen.append(person)

        for i, person in enumerate(seen):
            seen[i] = person.replace("'", "")
        self.people = seen

def main1(category, name):
    scraper = Scraper()
    nextUrl = scraper.findMediaTitle(f"https://cinemorgue.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:{category}&cmsort=sortkey&cmstartsortkeyprefix={name[0].upper()}&cmlimit=max&format=json",
                      name)
    if nextUrl != None:
        if scraper.findPeople(f"https://cinemorgue.fandom.com/api.php?action=query&titles={nextUrl}&prop=revisions&rvprop=content&formatversion=2&format=json"):
            scraper.removeDuplicates()

        else:
            print("Invalid format, choose a different film")
            #scraper.people = []
    else:
        print("not on there")
    #print(scraper.people)
    return scraper.people
if __name__ == "__main__":
    main1("Films", "john wick")