from bs4 import BeautifulSoup
import requests as rq

#https://eg.indeed.com/jobs?q=python


class Search:


    """
    What we need is 
        Job title
        Place
        Salary
        Description
        Duration
        link
    """
    def __init__(self , filter) :
        self.needs = filter.split()
        print(self.needs)
        self.jobs = []
        self.__searchIndeed()

    def __searchIndeed(self):
        link = 'https://eg.indeed.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-'

        for feature in self.needs: ## this will loop on all needs
            print(f'Feature is {feature}')

            html_text=rq.get(link+feature).text
            soup = BeautifulSoup(html_text , 'lxml')
            # head = soup.find('div' , class_= 'jobsearch-SerpJobCard unifiedRow row result clickcard')
            job_titles = soup.find_all("div" , class_ = "jobsearch-SerpJobCard")
            print(len(job_titles))
            for job in job_titles:
                print(job.prettify())
                title = job.h2.a.text
                link = job.h2.a['href']

                location = job.find('div' , class_ = 'sjcl')
                the_place = location.find_all('span')
                place = ''
                for x in the_place:
                    place += x.text


                salary = job.find('span' , class_ = "salaryText")
                print(salary)
                salary = salary.text

                print(f'{title}:\n\t{place}\n\t{salary}\n\t{link}')
                input('Press any key to continue')

                self.__addJob(title,link,place,salary)
    
    def __addJob(self ,title,link,place,salary):
        job = f'{title}:\n\t{place}\n\t{salary}\n\t{link}'
        print(job)
        self.jobs.append(job)

x = Search('python')








