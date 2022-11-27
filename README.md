# Summary of the project 

Create a parallel corpus of Bashkir and English for training a translator. A quick search on the internet shows that there are non-parallel Bashkir corpora. Those I could find are listed below under Resources, Bashkir corpora. I could not find a parallel corpus, let alone an English-Bashkir one, lying around freely avaiable on the internet.
The resulting parallel corpus including 2838 Bashkir-English sentence pairs was extracted from a Wiktionary dump https://dumps.wikimedia.org/enwiktionary/ of 2022-10-21 of the English Language Wiktionary.

# Other resources and ideas for the future

## Making a corpus  
https://www.clarin.eu/resource-families/parallel-corpora  
https://ufal.mff.cuni.cz/czeng

## Bashkir corpora  

This http://web-corpora.net/bashcorpus/search/?interface_language=en is a corpus created by Bashkir State University from a collection of Bashkir poetry starting from Soviet era. It claims to have over 1.8 million word usage instances. One issue is that I haven't found a way to download the whole corpus, rather a limited number of search results can be downloaded.  
This https://corpora.uni-leipzig.de/en?corpusId=bak_wikipedia_2021 one is from Uni Leipzig, several time snapshots of several online sources, icluding news outlets and Wikipedia. The data are downloadable. I noticed that some sentences are actually in Russian, probably they automatically crawled the web.  
And then there are two random things on Github, https://github.com/nevmenandr/bashkir-corpus and https://github.com/LingConLab/Bashkir_corpus, for the first one the corpus appears to be very small, for the second one, I haven't found the data at all.

## Translation work done before

Here's a page that mentions English-Kazakh translation https://www.statmt.org/wmt19/translation-task.html.

# Work

## Data sets

### Corpus
To start, it's maybe a good idea to use the Uni Leipzig corpus because of its CC-BY licence.
Attribution: © 2022 Abteilung Automatische Sprachverarbeitung, Universität Leipzig, accessed at https://wortschatz.uni-leipzig.de/en.
I also cite the following paper:  
D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.
In: Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012

## Unicode data set
Constructed manually combining a Wikipedia page https://en.wikipedia.org/wiki/Bashkir_alphabet about Bashkir alphabet and a Unicode table https://unicodeplus.com/.
