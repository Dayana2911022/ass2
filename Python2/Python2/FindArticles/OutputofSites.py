from Sites import findsites

scrapper = findsites()
lists = scrapper.findArticle("bitcoin")
for i in lists: print(i)
print("\n sites: " + str(len(lists)))