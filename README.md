Created on : 13 Mar 2018

<br> **NOTE**: pytldr and pyteaser doesn't work for python>2.7. <br>
Summarize any language text
<br>
```
run MultiLanguageSummarizer.py
```
<br><br>
# Extractive text summarization
various ways to summarise text using the libraries available for Python
  1. pyteaser
  2. sumy
  3. gensim
  4. pytldr
  5. XLNET
  6. BERT
  7. GPT2
  
## INSTALL
pip install sumy<br>
pip install gensim<br>
pip install pyteaser<br>
pip install pytldr<br>
pip install bert-extractive-summarizer<br>
pip install spacy==2.0.12<br>
pip install transformers==2.2.0<br>
<br>
## Pyteaser
Pyteaser has two function:<br>
  Summarize: that takes title and text and summarizes them<br>
  SummarizeURL: that takes the url and summarizes the content of the url<br>
  
## Sumy
Summy has various preprocessing libraries and summarizer libraries<br>
  sumytoken: for tokenizing the text<br>
  get_stop_words: to remove the stop words from the text<br>
  stemmer: to stemp the words<br>
  LexRankSummarizer: summarizes based on lexical ranking<br>
  LsaSummarizer: summarizes based on semantic<br>
  LuhnSummarizer: summarizes based on Luhn's algorithm<br>

## Gensim
  gensim has a summarize library which can be imported and used directly.
  
## pytldr
 pytldr is also like sumy where they have various nlp libraries like tokenizer.<br>
 Here we have used TextRankSummarizer, RelevanceSummarzer, LsaSummarizer from pytldr

## XLNET
XLNet is an auto-regressive language model which outputs the joint probability of a sequence of tokens based on the transformer architecture with recurrence.

## BERT
Extractive Text summarization refers to extracting (summarizing) out the relevant information from a large document while retaining the most important information. BERT (Bidirectional Encoder Representations from Transformers) introduces rather advanced approach to perform NLP tasks.

## GPT2
GPT-2 model with 1.5 Billion parameters is a large transformer-based language model. It's trained for predicting the next word. So, we can use this specialty to summarize the data.

## PS:
If you are using python2, please run main.py from "for_python2" folder <br>
elif you are using python3,  please run main.py from "for_python3" folder<br>
else you can test by running "various_ways_to_summarize.py" or the notebook named as "Text Summarizer Notebook.ipynb"
