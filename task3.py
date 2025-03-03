import re

text = '''
homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

#normalize text from letter cases point of view
normalized_text = text.lower().strip()  #make whole text lower & remove all the spaces at the beginning & end
pattern_first_words = r'(^|\.\s*|\.\n|\:\n)([a-zA-Z]+)'  #pattern to select first word of string & words that placed after dot with space or dot with new line or colon with new line
normalized_text = re.sub(pattern_first_words, lambda match: match.group(1) + match.group(2).capitalize(),
                     normalized_text)  #change all found by pattern strings with normalized capital words

#create sentence with last words of each sentence & add it to the end of paragraph
pattern_last_words = r'\b([a-zA-Z]+)(?=\s*[\.])'  #pattern to select whole words (not numbers) that followed by dot
last_words = re.findall(pattern_last_words, text)
sentence_from_last_words = ' '.join(last_words).capitalize() + '.' #generate sentence out of last words

#insert sentence with last words into our text
normalized_text = normalized_text.replace('the end of this paragraph.',
                                   'the end of this paragraph. ' + sentence_from_last_words)

#correct 'iz' to 'is'
normalized_text = normalized_text.replace(' iz ', ' is ')
print(normalized_text)

#count spaces
spaces_counter = 0
for char in text:
    if char.isspace(): #check if a character is a whitespace character or newline
        spaces_counter += 1

print("Number of spaces: ", spaces_counter)
