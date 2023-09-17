from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import string
import re

nltk.download('punkt')
nltk.download('vader_lexicon')

#creating a Class WordAnalyser so i can easily pass the text files get the values easily

class WordAnalyser:
    def __init__(self, textfile, StopWords, pos_words, neg_words):
        self.StopWords = StopWords
        self.pos_words = pos_words
        self.neg_words = neg_words

        sia = SentimentIntensityAnalyzer()

        #opening the passes file and content, sentences,words
        with open(textfile, 'r',encoding='ISO-8859-1') as f:
            content = f.read()
        self.content = content
        self.sentences = nltk.sent_tokenize(content)
        self.words = nltk.word_tokenize(content)
        

    #  positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, wordCount using formulas
    def analyse(self):
        cleaned_words = [
            word.lower()
            for word in self.words
            if word.lower() not in self.StopWords and word not in string.punctuation
        ]

        positive_score = 0
        negative_score = 0

        for word in cleaned_words:
            if word in self.pos_words:
                positive_score += 1
            elif word in self.neg_words:
                negative_score -= 1
        negative_score = -(negative_score)

        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        subjectivity_score = (positive_score + negative_score) / (len(cleaned_words) + 0.000001)

        avg_sentence_length = len(self.words) / (len(self.sentences)+0.000001)

        return max(positive_score,0), max(negative_score,0), max(polarity_score,0), max(subjectivity_score,0), max(avg_sentence_length,0), max(len(cleaned_words),0)


    # this method will gives th complex_word_count, percentage_of_complex_words, fog_index, avg_words_per_sentences values with their respective formulas
    def complex_word(self):
        def is_complex_word(word):
            return len(word) > 3

        complex_word_count = sum(1 for word in self.words if is_complex_word(word))

        percentage_of_complex_words = complex_word_count / (len(self.words)+0.000001)

        avg_sentence_length=len(self.words) / (len(self.sentences)+0.000001)

        fog_index = 0.4 * (avg_sentence_length + percentage_of_complex_words)

        avg_words_per_sentences = len(self.words) / (len(self.sentences)+0.000001)

        return max(complex_word_count,0), max(percentage_of_complex_words,0), max(fog_index,0), max(avg_words_per_sentences,0)

    # this function will generate the syllable_count_per_word
    def syllableCount(self):
        
        def count_syllables(word):
            vowels = "aeiouAEIOU"
            count = 0
            prev_char = ''
            for char in word:                #counting the vowels without allowing the duplicate vowels in a single word
                if char in vowels and prev_char not in vowels:
                    count += 1
                prev_char = char

            if word.endswith(("es", "ed")) and count > 1: #decreasing the count if the word ends with "es" or "ed"
                count -= 1
            return max(count, 1)
        syllabels=[count_syllables(word) for word in self.words]
        return syllabels

    # generates the personal Pronouns count
    def personalPronouns(self):
        personal_pronouns = ["I", "we", "my", "ours", "us"]
        pattern = r'\b(?:' + '|'.join(personal_pronouns) + r')\b'
        personal_pronoun_count = len(re.findall(pattern, self.content, flags=re.IGNORECASE))
        return max(personal_pronoun_count,0)
    
    
    # Generating the average word length
    def averageWordLength(self):
        total_chars = sum(len(word) for word in self.words)
        avg_word_length = total_chars / (len(self.words)+0.000001)
        return max(avg_word_length,0)
