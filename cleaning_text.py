import re
import string
import nltk
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Pastikan untuk mendownload stopwords dan punkt dari nltk sebelum digunakan
nltk.download('punkt')  
nltk.download('stopwords')

def cleaningText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#[A-Za-z0-9]+', '', text) 
    text = re.sub(r'RT[\s]', '', text) 
    text = re.sub(r"http\S+", '', text)
    text = re.sub(r'[0-9]+', '', text) 
    text = re.sub(r'[^\w\s]', '', text) 
 
    text = text.replace('\n', ' ') 
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    text = text.strip(' ') 
    return text

def casefoldingText(text):
    text=text.lower()
    return text

url = "https://raw.githubusercontent.com/panggi/pujangga/master/resource/formalization/formalizationDict.txt"
response = requests.get(url)

lines = response.text.strip().split('\n')

formal_dict = {}

for line in lines:
    line = line.strip().replace('\ufeff', '')
    if '\t' in line:
        informal, formal = line.split('\t', 1)
        formal_dict[informal.strip()] = formal.strip()

formal_dict.update(
    {'ngak' : 'tidak',
     'narik' : 'ambil',
     'enteng' : 'gampang',
     'fiture ' : 'fitur',
     'kee': 'ke',
     'yg' : 'yang',
     'mantapppp' : 'mantap',
     'gacor' : 'keren',
     'cancel' :'batal',
     'anyeb' : 'jelek',
     'anyep' : 'jelek',
     'eror' : 'salah',
     'order' : 'pesan',
     'aj' :'saja',
     'ajah' : 'saja',
     'aja' : 'saja',
     'ajj' : 'saja',
     'aje' : 'saja',
     'private' : 'pribadi',
     'message' : 'pesan',
     'bonu' : 'bonus',
     'ajh' : 'saja',
     'ajja' : 'saja',
     'mantab' : 'mantap',
     'nya' : '',
     'driver' : '',
     'orderan' : 'pesanan',
     'bagu' : 'bagus',
     'ga' : 'tidak'
     
     }
)

def normalize_slang(text, slang_dict=formal_dict):
    words = text.split()
    normalized = [slang_dict.get(word.lower(), word) for word in words]
    return ' '.join(normalized)

def tokenize_text(text):
    tokens=nltk.word_tokenize(text)
    return tokens

stop_words=set(stopwords.words('indonesian'))
stop_words.discard('tidak')
def delete_stopwords(text,stop_words=stop_words):
    filtered_words=[word for word in text if word not in stop_words]
    return filtered_words

def merge_list(text):
    sentences=" ".join(text)
    return sentences

def preprocessed_text(text):
    a=cleaningText(text)
    b=casefoldingText(a)
    c=normalize_slang(b)
    d=tokenize_text(c)
    e=delete_stopwords(d)
    f=merge_list(e)
    return f