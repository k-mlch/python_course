import re


def normalize_text(text):  #normalize text from letter cases point of view
    pattern_first_words = r'(^|\.\s*|\.\n|\:\n)([a-zA-Z]+)'
    normalized_text = re.sub(pattern_first_words, lambda match: match.group(1) + match.group(2).capitalize(), text.lower().strip())
    return normalized_text


def create_sentence_from_last_words(
        text):  #create sentence with last words of each sentence & add it to the end of paragraph
    pattern_last_words = r'\b([a-zA-Z]+)(?=\s*[\.])'
    last_words = re.findall(pattern_last_words, text)
    sentence_from_last_words = ' '.join(last_words).capitalize() + '.'  # generate sentence out of last words
    return sentence_from_last_words


def insert_sentence(text, sentence, after_which_words_insert): #insert sentence with last words into our text
    #after_which_words_insert = 'the end of this paragraph.'
    return text.replace(after_which_words_insert, after_which_words_insert + ' ' + sentence)


def correct_misspelling(text): #correct 'iz' to 'is'
    return text.replace(' iz ', ' is ')


def count_spaces(text):
    spaces_counter = 0
    for char in text:
        if char.isspace():  # check if a character is a whitespace character or newline
            spaces_counter += 1
    return spaces_counter


def generate_final_text(text):
    text_with_normal_letters = normalize_text(text)
    last_words_sentence = create_sentence_from_last_words(text_with_normal_letters)
    text_with_new_sentence = insert_sentence(text_with_normal_letters, last_words_sentence, 'the end of this paragraph.')
    final_text = correct_misspelling(text_with_new_sentence)

    print(final_text)
    print("Number of whitespace characters:", count_spaces(text))


text = '''
homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

#generate & print text
generate_final_text(text)
