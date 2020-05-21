import pandas as pd
import random


def setOfTags(file):
    """
    This function takes a text file of tags and transform it into set of tags,
    making sure there is no duplicates
    """
    with open(file, encoding='utf-8') as file:
        f = file.readlines()
        f = [i.strip().lower() for i in f]
        f = [j.replace('#','') for j in f]
        content = sorted(set(f))
        return content


def produceCsv(tags, filename):
    """
    This function takes a set of tags and the filename you want and produce a csv file
    """
    df = pd.DataFrame(columns=['tags'], data=tags)
    df.to_csv(filename)


def main():
    """
    The main function. Takes 4 inputs the species name, date, content, 
    bird or animal hashtag
    """
    species = input('SPECIES\n').strip()
    date = input('DATE\n').strip()
    content = input('CONTENT\n').split('\\n')
    content = [line.rstrip().lstrip()+'\n' for line in content]
    footer = ['.\n','.\n','.\n','\\/\n','Nature is all around us!\n', 
            'So #OpenYourMind #BeCurious #CareMore\n', '/\\\n','Hashtags:\n']
    hashTable = input('HASHTAGS\n')
    hashTable = pd.read_csv(hashTable)
    hashtags = ['#'+random.choice(hashTable['tags'])+' ' for i in range(23)]
    
    with open('post.txt','w',encoding='utf-8') as file:
        file.write('#' + species + '\n')
        file.write('Date: ' + date + '\n')
        file.writelines(content)
        file.writelines(footer)
        file.writelines(hashtags)