from bs4 import BeautifulSoup
import requests as rq

class Processor:

    def __init__(self , name , price , link):
        self.name = name
        self.price = price
        self.link = link

    def getData(self):
        x = f'Name : {self.name}\n'
        x = x+ f'Price is : {self.price}\n'
        x = x+ f'Link is : {self.link}\n'  
        return x  


processors = []

def getFromegPrices(proc):
    link = 'https://www.egprices.com/en/category/computers/components/processors?&page='
    page = 1
    while page < 4 :
        html_text=rq.get(link+str(page)).text
        soup = BeautifulSoup(html_text,'lxml')
        contents = soup.find_all('div' , class_="row align-middle collapse")
        if contents is None:
            break
        for content in contents:
            div_of_name = content.find('div' , class_='small-9 medium-7 columns')
            name = div_of_name.a.text.replace('\n' , '')
            the_link = link+str(page)+div_of_name.a['href']
            # print(f'name is {name} and link is {the_link}')
            div_of_price = content.find('div' , class_ = "small-12 show-for-medium medium-3 text-center columns")
            divs_in_price = div_of_price.find_all('div' , class_="small-6 medium-12 text-left medium-text-center columns")
            # print(divs_in_price)
            price = divs_in_price[0].text.replace('\n','')
            # print(f'Price is {price}')

            proc.append(Processor(name , price , the_link))
        page = page+1       
if __name__ == "__main__":
    getFromegPrices(processors)

    with open('processors.txt' , 'w') as file:
        for processor in processors:
            file.write(processor.getData())
            file.write('__'*100+'\n')
    print('Done')        