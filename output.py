import sentiment  # importing th sentiment.py to analyse the data
import pandas as pd
import pathlib
import nltk

df=pd.read_excel('Input.xlsx')

# creating a windows filepath object so that i can access differnt files easily
file_dir=pathlib.Path("C:/Users/balij/OneDrive/Desktop/webscrapping project")

#saving all the stopwords file paths in list to iterate over file paths
stopword_files=list(file_dir.glob('StopWords/*'))
stopwords=[]

# Cobining all the stopwords
for txt in stopword_files:
    with open(txt,'r') as f:
        matter=f.read()
        tokens=nltk.word_tokenize(matter)

    stopwords=stopwords+tokens

# getting the positive words
with open("MasterDictionary\positive-words.txt",'r',encoding='ISO-8859-1') as f:
    positive_words=nltk.word_tokenize(f.read())

# Getting the negative words
with open("MasterDictionary/negative-words.txt",'r',encoding='ISO-8859-1') as f:
    negative_words=nltk.word_tokenize(f.read())


## Empty lists to append respective values and to create dataframe later
POSITIVE_SCORE = []
NEGATIVE_SCORE = []
POLARITY_SCORE = []
SUBJECTIVITY_SCORE = []
AVG_SENTENCE_LENGTH = []
PERCENTAGE_OF_COMPLEX_WORDS = []
FOG_INDEX = []
AVG_NUMBER_OF_WORDS_PER_SENTENCE = []
COMPLEX_WORD_COUNT = []
WORD_COUNT = []
SYLLABLE_PER_WORD = []
PERSONAL_PRONOUNS = []
AVG_WORD_LENGTH = []


# appending the values of above lists using the WordAnalyser

for file in df.URL_ID:
    wa=sentiment.WordAnalyser(str(f"textfiles/{file}.txt"),stopwords,positive_words,negative_words)

    positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, wordCount=wa.analyse()
    POSITIVE_SCORE.append(positive_score)
    NEGATIVE_SCORE.append(negative_score)
    POLARITY_SCORE.append(polarity_score)
    SUBJECTIVITY_SCORE.append(subjectivity_score)
    AVG_SENTENCE_LENGTH.append(avg_sentence_length)
    WORD_COUNT.append(wordCount)

    complex_word_count, percentage_of_complex_words, fog_index, avg_words_per_sentences =wa.complex_word()
    COMPLEX_WORD_COUNT.append(complex_word_count)
    PERCENTAGE_OF_COMPLEX_WORDS.append(percentage_of_complex_words)
    AVG_NUMBER_OF_WORDS_PER_SENTENCE.append(avg_words_per_sentences)
    FOG_INDEX.append(fog_index)

    syllable_count_per_word=wa.syllableCount()
    SYLLABLE_PER_WORD.append(syllable_count_per_word)

    personal_pronoun_count=wa.personalPronouns()
    PERSONAL_PRONOUNS.append(personal_pronoun_count)

    avg_word_length=wa.averageWordLength()
    AVG_WORD_LENGTH.append(avg_word_length)

#creating the dict with coloum values for dataframe as mentioned in objective.docx 

new_coloums={
    'POSITIVE_SCORE' :POSITIVE_SCORE,
    'NEGATIVE_SCORE' :NEGATIVE_SCORE,
    'POLARITY_SCORE' :POLARITY_SCORE,
    'SUBJECTIVITY_SCORE' : SUBJECTIVITY_SCORE,
    'AVG_SENTENCE_LENGTH' :AVG_SENTENCE_LENGTH,
    'PERCENTAGE_OF_COMPLEX_WORDS' :PERCENTAGE_OF_COMPLEX_WORDS,
    'FOG_INDEX' :FOG_INDEX,
    'AVG_NUMBER_OF_WORDS_PER_SENTENCE' :AVG_NUMBER_OF_WORDS_PER_SENTENCE,
    'COMPLEX_WORD_COUNT' :COMPLEX_WORD_COUNT,
    'WORD_COUNT' :WORD_COUNT,
    'SYLLABLE_PER_WORD' :SYLLABLE_PER_WORD,
    'PERSONAL_PRONOUNS' :PERSONAL_PRONOUNS,
    'AVG_WORD_LENGTH' :AVG_WORD_LENGTH
    }

#unpacking and adding coloums to dataframe
df=df.assign(**new_coloums)

#exproting the dataframe to csv file as output.csv
df.to_csv('output.csv', index=False)
