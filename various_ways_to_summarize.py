'''
pip install sumy
pip install gensim
==> run the code directly
'''

from gensim.summarization import summarize

from sumy.summarizers import luhn
from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.luhn import LuhnSummarizer 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer as sumytoken
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer

from pytldr.nlp.tokenizer import Tokenizer as pltdrtoken
from pytldr.summarize.textrank import TextRankSummarizer
from pytldr.summarize.relevance import RelevanceSummarizer
from pytldr.summarize.lsa import LsaSummarizer, LsaOzsoy, LsaSteinberger


LANGUAGE = "english"
SENTENCES_COUNT = 2

text = 'The contribution of cloud computing and mobile computing technologies lead to the newly emerging mobile cloud com- puting paradigm. Three major approaches have been pro- posed for mobile cloud applications: 1) extending the access to cloud services to mobile devices; 2) enabling mobile de- vices to work collaboratively as cloud resource providers; 3) augmenting the execution of mobile applications on portable devices using cloud resources. In this paper, we focus on the third approach in supporting mobile data stream applica- tions. More specifically, we study how to optimize the com- putation partitioning of a data stream application between mobile and cloud to achieve maximum speed/throughput in processing the streaming data. To the best of our knowledge, it is the first work to study the partitioning problem for mobile data stream applica- tions, where the optimization is placed on achieving high throughput of processing the streaming data rather than minimizing the makespan of executions as in other appli- cations. We first propose a framework to provide runtime support for the dynamic computation partitioning and exe- cution of the application. Different from existing works, the framework not only allows the dynamic partitioning for a single user but also supports the sharing of computation in- stances among multiple users in the cloud to achieve efficient utilization of the underlying cloud resources. Meanwhile, the framework has better scalability because it is designed on the elastic cloud fabrics. Based on the framework, we design a genetic algorithm for optimal computation parti- tion. Both numerical evaluation and real world experiment have been performed, and the results show that the par- titioned application can achieve at least two times better performance in terms of throughput than the application without partitioning.'

parser = PlaintextParser.from_string((text), sumytoken(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

def lexrank_summarizer():
    print ("\n","*"*30, "LEXRANK SUMARIZER", "*"*30)
    summarizer_LexRank = LexRankSummarizer(stemmer)
    summarizer_LexRank.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer_LexRank(parser.document, SENTENCES_COUNT):
        print (sentence)
        
def lsa_summarizer():
    print ("\n","*"*30, "LSA SUMMARIZER", "*"*30)
    summarizer_lsa = Summarizer(stemmer)
    summarizer_lsa.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer_lsa(parser.document, SENTENCES_COUNT):
        print (sentence)
        
def luhn_summarizer():
    print ("\n","*"*30, "LUHN SUMMARIZER", "*"*30)
    summarizer_luhn = LuhnSummarizer(stemmer)
    summarizer_luhn.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer_luhn(parser.document, SENTENCES_COUNT):
        print (sentence)
        
def gensim_summarizer():
    print ("\n","*"*30, "GENSIM SUMMARIZER", "*"*30)
    print (summarize(text))

def pytldr_textrank():
    print ("\n","*"*30, "PYTLDR TEXTRANK", "*"*30)
    tokenizer = pltdrtoken('english')
    summarizer = TextRankSummarizer(tokenizer)
    summarizer = TextRankSummarizer() 
    summary = summarizer.summarize(text, length=4)
    print (summary)

def pytldr_lsa():
    print ("\n","*"*30, "PYTLDR LSA", "*"*30)
    summarizer = LsaOzsoy()
    summarizer = LsaSteinberger()
    summarizer = LsaSummarizer()  # This is identical to the LsaOzsoy object

    summary = summarizer.summarize(
        text, topics=4, length=5, binary_matrix=True, topic_sigma_threshold=0.5
    )
    print (summary)

#----Call all the functions to compare the summaries
lexrank_summarizer()
lsa_summarizer()
luhn_summarizer()
gensim_summarizer()
pytldr_textrank()
pytldr_lsa()

"""
#---OUTPUT---
****************************** LEXRANK SUMARIZER ******************************
Three major approaches have been pro- posed for mobile cloud applications: 1) extending the access to cloud services to mobile devices; 2) enabling mobile de- vices to work collaboratively as cloud resource providers; 3) augmenting the execution of mobile applications on portable devices using cloud resources.
In this paper, we focus on the third approach in supporting mobile data stream applica- tions.
****************************** LSA SUMMARIZER ******************************
We first propose a framework to provide runtime support for the dynamic computation partitioning and exe- cution of the application.
Different from existing works, the framework not only allows the dynamic partitioning for a single user but also supports the sharing of computation in- stances among multiple users in the cloud to achieve efficient utilization of the underlying cloud resources.
****************************** LUHN SUMMARIZER ******************************
Three major approaches have been pro- posed for mobile cloud applications: 1) extending the access to cloud services to mobile devices; 2) enabling mobile de- vices to work collaboratively as cloud resource providers; 3) augmenting the execution of mobile applications on portable devices using cloud resources.
To the best of our knowledge, it is the first work to study the partitioning problem for mobile data stream applica- tions, where the optimization is placed on achieving high throughput of processing the streaming data rather than minimizing the makespan of executions as in other appli- cations.
****************************** GENSIM SUMMARIZER ******************************
More specifically, we study how to optimize the com- putation partitioning of a data stream application between mobile and cloud to achieve maximum speed/throughput in processing the streaming data.
To the best of our knowledge, it is the first work to study the partitioning problem for mobile data stream applica- tions, where the optimization is placed on achieving high throughput of processing the streaming data rather than minimizing the makespan of executions as in other appli- cations.
****************************** PYTLDR TEXTRANK ******************************
['Three major approaches have been pro- posed for mobile cloud applications: 1) extending the access to cloud services to mobile devices; 2) enabling mobile de- vices to work collaboratively as cloud resource providers; 3) augmenting the execution of mobile applications on portable devices using cloud resources.', 'More specifically, we study how to optimize the com- putation partitioning of a data stream application between mobile and cloud to achieve maximum speed/throughput in processing the streaming data.', 'To the best of our knowledge, it is the first work to study the partitioning problem for mobile data stream applica- tions, where the optimization is placed on achieving high throughput of processing the streaming data rather than minimizing the makespan of executions as in other appli- cations.', 'Different from existing works, the framework not only allows the dynamic partitioning for a single user but also supports the sharing of computation in- stances among multiple users in the cloud to achieve efficient utilization of the underlying cloud resources.']
****************************** PYTLDR LSA ******************************
['Three major approaches have been pro- posed for mobile cloud applications: 1) extending the access to cloud services to mobile devices; 2) enabling mobile de- vices to work collaboratively as cloud resource providers; 3) augmenting the execution of mobile applications on portable devices using cloud resources.', 'In this paper, we focus on the third approach in supporting mobile data stream applica- tions.', 'We first propose a framework to provide runtime support for the dynamic computation partitioning and exe- cution of the application.', 'Different from existing works, the framework not only allows the dynamic partitioning for a single user but also supports the sharing of computation in- stances among multiple users in the cloud to achieve efficient utilization of the underlying cloud resources.', 'Both numerical evaluation and real world experiment have been performed, and the results show that the par- titioned application can achieve at least two times better performance in terms of throughput than the application without partitioning.']
"""
