import scraperwiki
#next line imports the lxml.html library
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
#
# # Find something on the page using css selectors
#use the .fromstring function to turn html into a lxml 'object', a variable called root
root = lxml.html.fromstring(html)
#use .cssselect method on root to grab 'td' tags and put into tds
tds = root.cssselect('td')
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
