
class AnalystUtility :

    # Complex words are words in the text that contain more than two syllables.
    # We count the number of Syllables in each word of the text by counting the vowels present in each word.
    # We also handle some exceptions like words ending with "es","ed" by not counting them as a syllable.
    @staticmethod
    def is_complex_word(word : str) -> bool :
        
        word = word.removesuffix("ES").removesuffix("ED")
        vowel_count = 0
        for i in word :
            if i in ['A', 'E', 'I', 'O', 'U'] : vowel_count+=1
        if vowel_count > 2 : return True
        return False
    
    @staticmethod
    def percent_of_complex_words(no_of_complex_words : int, total_no_of_words : int) -> float :
        return round(no_of_complex_words/(total_no_of_words+0.000001), 3)
    

    #====================| This is the score that determines if a given text is positive or negative in nature.
    # Range is from -1 to +1.
    @staticmethod
    def calculate_polarity_score(positive_score : int, negative_score : int) -> float :
        return round((positive_score - negative_score)/(0.000001+ positive_score+negative_score),3)
    

    #====================| This is the score that determines if a given text is objective or subjective.
    # Range is from 0 to +1.
    @staticmethod
    def calculate_subjectivity_score(positive_score : int, negative_score : int, total_word_after_cleaning : int) -> float :
        return round((positive_score+negative_score)/(total_word_after_cleaning),3) if total_word_after_cleaning != 0 else (positive_score+negative_score)
    

    #====================| Analysis of Readability is calculated using the Fox index.
    @staticmethod
    def calculate_fog_index(avg_sentence_length : float, percent_of_complex_words : float) :
        return round((0.4*(avg_sentence_length+percent_of_complex_words)),3)
    
    
    @staticmethod
    def calculate_average_sentence_length(total_no_of_words : int, no_of_sentence : int) -> float :
        return round((total_no_of_words/(no_of_sentence)),3) if no_of_sentence != 0 else total_no_of_words
    
    @staticmethod
    def calculate_percent_of_complex_words(no_of_complex_word : int , no_of_word : int) -> float :
        return round((no_of_complex_word/(no_of_word*100)) , 3) if no_of_word != 0 else no_of_complex_word
    
    @staticmethod
    def calculate_average_word_length(total_no_of_character : int, no_of_word : int) -> float :
        return round((total_no_of_character/(no_of_word+0.00001)), 3)