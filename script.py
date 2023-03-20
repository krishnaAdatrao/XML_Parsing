import gzip
import xml.etree.ElementTree as ET
#import psycopg2

pubmed_file = open('pubmed23n0008.xml', 'r')
tree = ET.parse(pubmed_file)
root = tree.getroot()


PMID_lst, ArticleTitle_lst, Publisher_lst, Date_lst, Author_Name_lst = [], [], [], [], []
for elm in root.findall('.//'):

    if elm.tag == "PMID":
        PMID_lst.append(int(elm.text))
        # print("PMID", elm.text)

    if elm.tag == "ArticleTitle":
        ArticleTitle_lst.append(elm.text)
        # print("ArticleTitle", elm.text)
      
    if elm.tag == "Title":
        Publisher_lst.append(elm.text)
        # print("Publisher", elm.text)

# Find all Date elements in the XML tree
all_dates = root.findall('.//MedlineCitation')
for i, dates_list in enumerate(all_dates):
    # Find the Complete Date Tags in each DateCompleted
    complete_date = dates_list.find('./DateCompleted')
    # Extract the Complete date and print it
    if complete_date is not None:
        date_date = complete_date.findtext('Year', default='') + '-' + complete_date.findtext('Month', default='') + '-' + complete_date.findtext('Day', default='')
        Date_lst.append(date_date)
        # print(i, date_date)

# Find all AuthorList elements in the XML tree
author_lists = root.findall('.//AuthorList')
for i, author_list in enumerate(author_lists):
    # Find the first Author in each AuthorList
    first_author = author_list.find('./Author')
    # Extract the first Author's name and print it
    if first_author is not None:
        first_name = first_author.findtext('LastName', default='') + ' ' + first_author.findtext('ForeName', default='') + ' ' + first_author.findtext('Initials', default='')
        Author_Name_lst.append(first_name)
        # print(i, first_name)

print("Author Names: ", len(Author_Name_lst), "\n\n")
print("PMID: ", len(PMID_lst), "\n\n")
print("Article Names: ", len(ArticleTitle_lst), "\n\n")
print("Date Completed: ", len(Date_lst), "\n\n")
print("Publisher Names: ", len(Publisher_lst))

zipped_list = list(zip(Author_Name_lst, PMID_lst, ArticleTitle_lst, Date_lst, Publisher_lst))
print(zipped_list[:10])