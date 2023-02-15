from bs4 import BeautifulSoup
import requests
response=requests.get("https://news.ycombinator.com/")
yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,'html.parser')
soup_title=soup.find_all(name="span",class_="titleline")
# soup_upvote=soup.find_all(name='span', class_="subline").get_text()
# print(soup_upvote)
article_text=[]
article_links=[]
article_votes=[]

for a in soup_title:
    text=a.get_text()
    article_text.append(text)
    link=a.a.get("href")
    article_links.append(link)

votes=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
    # votes=vote.split()
    # votes=int(votes[0])
    

    
    
# print(votes)
highest_votes=max(votes)

largest_index=votes.index(highest_votes)
print(f"Article with highest upvotes: {article_text[largest_index]}")
print(f"Link of article with highest upvotes: {article_links[largest_index]}")
print(f'highest votes: {highest_votes}')


# print(soup_link)

# with open("website.html") as file:
#     contents=file.read()
# soup=BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title.text)
# # all_anchor_tags=soup.find_all(name="a")
# # # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     #  print(tag.get("href"))
# #     # print(soup.find(name="h1",id="name"))
# #     # section_heading=soup.find(name="h3", class_="heading")
# #     # print(section_heading.getText())
# company_url=soup.select_one(selector="p a")
# company_url_id=soup.select_one(selector="#name")
# print(company_url)
# print(company_url_id)
# headings=soup.select(".heading")