## ReQuest: Indirect Supervision for Relation Extraction Using Question-Answer Pairs

Source code and data for WSDM'18 paper *[Indirect Supervision for Relation Extraction Using Question-Answer Pairs](https://arxiv.org/abs/1710.11169)*. 


* Put the below library under `ReQuest/code/DataProcessor/'.
[stanford coreNLP 3.7.0](http://stanfordnlp.github.io/CoreNLP/) and its [python wrapper](https://github.com/stanfordnlp/stanza). 


Example:
```
$ cd code/DataProcessor/
$ git clone https://github.com/stanfordnlp/stanza
$ cd stanza
$ pip install -e .
$ wget http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip
$ unzip stanford-corenlp-full-2016-10-31.zip
```
* [eigen 3.2.5](http://bitbucket.org/eigen/eigen/get/3.2.5.tar.bz2) (already included). 


## Data
We [process](https://github.com/shanzhenren/StructMineDataPipeline) (using our [data pipeline](https://github.com/shanzhenren/StructMineDataPipeline)) a public RE datasets to our JSON format. We ran [Stanford NER](https://nlp.stanford.edu/software/CRF-NER.shtml) on training set to detect entity mentions, and performed distant supervision using [DBpediaSpotlight](https://github.com/dbpedia-spotlight/dbpedia-spotlight) to assign type labels:

   * **NYT** ([Riedel et al., 2011](https://pdfs.semanticscholar.org/db55/0f7af299157c67d7f1874bf784dca10ce4a9.pdf)): 1.18M sentences sampled from 294K New York Times news articles. 395 sentences are manually annotated with 24 relation types and 47 entity types. ([Download JSON](https://drive.google.com/drive/folders/0B--ZKWD8ahE4UktManVsY1REOUk?usp=sharing))
  

Please put the data files in corresponding subdirectories under `ReQuest/data/source`

We use the [answer sentence selection dataset](https://github.com/xuchen/jacana/tree/master/tree-edit-data/answerSelectionExperiments/data) from TREC QA as our source of indirect supervision. We ran Stanford NER to extract entity mentions on both question and answer sentences and process the dataset into JSON format containing QA-pairs.
([Download JSON](https://drive.google.com/file/d/0B--ZKWD8ahE4dEZTQzI1UlRUeGc/view?usp=sharing))



## Makefile
Compile `request.cpp` under your own g++ environment
```
$ cd ReQuest/code/Model/request; make
```

## Default Run & Parameters
Run ReQuest for the task of *Relation Extraction* on the NYT dataset

Start the Stanford corenlp server for the python wrapper.
```
$ java -mx4g -cp "code/DataProcessor/stanford-corenlp-full-2016-10-31/*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer
```

Feature extraction, embedding learning on training data, and evaluation on test data.
```
$ ./run_nyt.sh  
```
The hyperparamters for embedding learning are included in the run_nyt.sh script.

## Evaluation
Evaluates relation extraction performance (precision, recall, F1): produce predictions along with their confidence score; filter the predicted instances by tuning the thresholds.
```
$ python code/Evaluation/emb_test.py extract NYT request cosine 0.0
$ python code/Evaluation/tune_threshold.py extract NYT emb request cosine
```


## Performance
Performance comparison with several *relation extraction* systems (**sentence-level extraction**). 

Method | Precision | Recall | F1 
-------|-----------|--------|----
CoType-RM ([Ren et al., 2017](https://arxiv.org/pdf/1610.08763v1.pdf)) | 0.342 | 0.339 | 0.340
ReQuest ([Wu et al., 2018](https://arxiv.org/abs/1710.11169)) | 0.386 | 0.410 | **0.397**

