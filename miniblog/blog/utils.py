import nltk
from django.utils.html import strip_tags
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def generate_summary(text, sentence_count=5):
    if not text:
        return ""
    
    plain_text = strip_tags(text)
    parser = PlaintextParser.from_string(plain_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary_sentences = summarizer(parser.document, sentence_count)
    summary = " ".join(str(sentence) for sentence in summary_sentences)
    print('➡ miniblog/blog/utils.py:21 summary:', summary)

    # agar summarizer fail kare ya blank ho
    if not summary.strip():
        print("summry not generate")
        summary = " ".join(plain_text.split(".")[:sentence_count])

    return summary.strip()