import xlrd
import requests
import json
from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('demo1234.xlsx')
worksheet = workbook.add_worksheet()
line_count = 0


page = 1

while page<2:

    print ('https://maker2u.com/store-listing-2/page/' + str(page) + '/')

    response1 = requests.get('https://maker2u.com/store-listing-2/page/' + str(page) + '/')
    html = BeautifulSoup(response1.content, 'html.parser')



    columns = html.find_all('div',{'class':'store-wrapper'})



    for col in columns:
        name = ''
        storeaddress = ''
        storephone = ''
        about = ''
        image = ''
        sociallinks = ''

        j = 0


        try:
            name = col.find('h2')
            name = name.text.strip()

            worksheet.write(line_count, j, name)
            j = j+1


        except:
            worksheet.write(line_count, j, '')
            j = j+1
            print ("Head Error")

        try:

            storeaddress = col.find('p',{'class':'store-address'})
            storeaddress = storeaddress.text.strip()
            worksheet.write(line_count, j, storeaddress)
            j = j+1


        except:
            worksheet.write(line_count, j, '')
            j = j+1
            print ("Address Error")

        try:

            storephone = col.find('p', {'class': 'store-phone'})
            storephone = storephone.text.strip()

            worksheet.write(line_count, j, storephone)
            j = j+1


        except:
            worksheet.write(line_count, j, '')
            j = j+1
            print ("Phone error")


        try:

            avatar = col.find('div', {'class': 'seller-avatar'})
            avatar = avatar.find('img')

            print (avatar.get('src'))

            worksheet.write(line_count, j, avatar.get('src'))
            j = j+1


        except:
            worksheet.write(line_count, j, '')
            j = j+1
            print ("Phone error")


        print (name)
        print (storeaddress)
        print (storephone)


        try:



            link= col.find('a')
            link = link.get('href')

            print (link)

            response2 = requests.get(link)
            html2 = BeautifulSoup(response2.content, 'html.parser')



            try:
                social_link = html2.find('ul',{'class':'store-social'})

                links = social_link.find_all('li')

                for link in links:
                    link_a = link.find('a')
                    print (link_a.get('href'))

                    worksheet.write(line_count, j, link_a.get('href'))
                    j = j + 1


            except:
                print ("Social Error")



        except:
            print ("Main Link Error")







        line_count = line_count + 1



    page = page + 1

workbook.close()

