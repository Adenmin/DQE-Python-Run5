import re
from typing import List

basicString = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# Split text by \s+ pattern. Return: String.
def cleanup_raw_text(text: str) -> str:
    return " ".join(re.split(r"\s+", text)).strip()


# Split text by sentences. Return: List of strings.
def split_text_by_sentences(text: str) -> List[str]:
    return re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.?])\s", text)


# Capitalize sentences in list. Return: List of strings.
def capitalize_sentences(sentences: List[str]) -> List[str]:
    return [line.strip().capitalize() for line in sentences]


# Create sentence by last word of sentences in list. Return: String.
def create_sentence_by_last_words(sentences: List[str]) -> str:
    last_words = []
    for sentence in sentences:
        last_words.append(re.search(r"\s(\w+)[.!?]$", sentence).group().replace('.', ''))
    return "".join(last_words).strip().capitalize() + "."


# Add sentence to text by index. Return: String.
def add_sentence(index: int, sentence: str, text: str) -> str:
    sentences = split_text_by_sentences(text)
    sentences.insert(index, sentence)
    return build_text_from_sentences(sentences)


# Fix mistake "iz", "Iz", "iZ". Return: String.
def fix_mistake_iz(text: str) -> str:
    return re.sub(r"\s(iz|Iz|iZ)\s", " is ", text)


# Build text from sentences in list. Return: String.
def build_text_from_sentences(sentences: [str]) -> str:
    return "\n".join(sentences)


# Count whitespaces in text. Return: Int.
def whitespace_count(text: str) -> int:
    return len(re.findall(r"\s", text))


if __name__ == "__main__":
    cleanText = cleanup_raw_text(basicString)
    textSentences = split_text_by_sentences(cleanText)
    textSentences = capitalize_sentences(textSentences)
    addSentence = create_sentence_by_last_words(textSentences)
    textWithAddSentence = add_sentence(3, addSentence, build_text_from_sentences(textSentences))
    correct_text = fix_mistake_iz(textWithAddSentence)

    # Print block.
    print("_____________________")
    print(correct_text)
    print("_____________________")
    print(f"Whitespaces count: {whitespace_count(correct_text)}")
