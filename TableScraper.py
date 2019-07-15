import pandas as pd
import requests
import lxml.html as lh

def ScrapeTableByRowCount(url, column_count):

    page = requests.get(url)

    doc = lh.fromstring(page.content)

    tr_elements = doc.xpath('//tr')
    content = []
    for tr in tr_elements:
        if len(tr) != column_count:
            tr_elements.remove(tr)
            continue
        row_content = []
        for element in tr:
            if element.text_content() == '':
                break
            row_content.append(element.text_content())
        if len(row_content) == column_count:
            content.append(row_content)

    return content
