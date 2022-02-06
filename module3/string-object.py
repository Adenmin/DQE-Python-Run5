import re

basicString = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Create dictionary for text lines.
lines = dict.fromkeys(range(0, 5))

# Shrink whitespaces and split text by lines.
basicString = re.sub(r"\n+", "\n", basicString).strip().split("\n")
basicString = [line.strip().capitalize() for line in basicString if not line.isspace()]
lines = {k: basicString[k] for k in lines}

# Split lines by sentences.
lines = {k: v.split(".") for k, v in lines.items()}

# Cleanup empty "sentences".
for k, v in lines.items():
    for i in range(len(v)):
        if v[i] == "":
            del v[i]

# Split lines to header and main text.
header = {k: v for k, v in lines.items() if k == 0}
mainText = {k: v for k, v in lines.items() if k != 0}

# Create additional sentence.
last_words = []
for v in mainText.values():
    for i in v:
        last_words.append(re.search(r"\s(\w+)$", i).group().strip())
additionalSentence = " ".join(last_words).capitalize()

# Add additional sentence to second paragraph.
mainText[3].append(additionalSentence)

# Find and fix mistakes:
for k, v in mainText.items():
    for i in range(len(v)):
        v[i] = re.sub(r"\siz\s", " is ", v[i])  # iz
        v[i] = re.sub(r"(\stex\s)|(\stex$)", " text ", v[i])  # tex
        v[i] = v[i].replace("fix\u201Ciz\u201D", "fix \u201Ciz\u201D")  # missing space in Fix“iz”

# Build text
for k, v in mainText.items():
    for i in range(len(v)):
        v[i] = v[i].strip().capitalize() + '.'
header.update(mainText)
fullText = header

# Create variables for string format
headerLine = " ".join(fullText[0])
firstParagraph = " ".join(fullText[1])
secondParagraph = " ".join(fullText[2])
thirdParagraph = " ".join(fullText[3])
fourthParagraph = " ".join(fullText[4])

# Create final text
finalText = f"""
 {headerLine}
  {firstParagraph}
  {secondParagraph}
  {thirdParagraph}
  {fourthParagraph}
"""

# Count whitespace in final text
whitespaceCount = len(re.findall(r"\s", finalText))

# Replace whitespace count in final text
finalText = finalText.replace("87", str(whitespaceCount))

print(finalText)
