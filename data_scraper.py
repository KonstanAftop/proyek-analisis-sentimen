from google_play_scraper import app, reviews_all, Sort
import csv
scrapreview = reviews_all(
    'com.gojek.partner',         
    lang='id',             
    country='id',         
    sort=Sort.MOST_RELEVANT, 
    count=12000           
)

with open('ulasan_aplikasi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review']) 
    for review in scrapreview:
        writer.writerow([review['content']]) 