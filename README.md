# text_summarization
various ways to summarise text using the libraries available
  1. pyteaser
  2. sumy
  3. gensim
  4. pytldr
  
## INSTALL
pip install sumy
pip install gensim
pip install pyteaser
pip install pytldr

## Pyteaser
Pyteaser has two function:
  Summarize: that takes title and text and summarizes them
  SummarizeURL: that takes the url and summarizes the content of the url
  
## Sumy
Summy has various preprocessing libraries and summarizer libraries
  sumytoken: for tokenizing the text
  get_stop_words: to remove the stop words from the text
  stemmer: to stemp the words
  LexRankSummarizer: summarizes based on lexical ranking
  LsaSummarizer: summarizes based on semantic
  LuhnSummarizer: summarizes based on Luhn's algorithm

## Gensim
  gensim has a summarize library which can be imported and used directly.
  
## pytldr
 pytldr is also like sumy where they have various nlp libraries like tokenizer.
 Here we have used TextRankSummarizer, RelevanceSummarzer, LsaSummarizer from pytldr
