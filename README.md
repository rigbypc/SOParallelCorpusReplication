# [Link](https://doi.org/10.6084/m9.figshare.7673927.v2) to Data


# Processing Data with [OpenNMT](http://opennmt.net/)
cd ~/OpenNMT
1. For tokenization run from command line:
th tools/tokenize.lua -mode space < ~/data/eng.txt > ~/data/eng.tok
th tools/tokenize.lua -mode space < ~/data/code.txt > ~/data/code.tok

2. For creating the dictionary run from the command line:
th preprocess.lua -train_src ~/data/eng.tok -train_tgt ~/data/code.tok -keep_frequency true -save_data ~/data/dictionary

For each corpus there will be a dictionary with three columns (tab separated):

token | 1-indexed token id | Occurance frequency

The first four tokens of each dictionary contains:

`<blank>`

`<unk>`

`<s>`

`</s>`

Besides creating the dictionary previous command creates a binrary file with .t7 extension. For our purpose we do not need that file.

rm ~/data/*.t7

# Align the corpora with Berkeley Aligner
1. From command line run: cd ~/SOParallelCorpusReplication/BerkeleyAligner
2. Split your corpus into two parts: 80% for training and 20% for testing
3. Run the following commands one after another:

mkdir -p ~/SOParallelCorpusReplication/BerkeleyAligner/data/train

mkdir ~/SOParallelCorpusReplication/BerkeleyAligner/data/test

4. Populate the BerkeleyAligner/data/train folder with train.en and train.cd
5. Populate the BerkeleyAligner/data/test folder with test.en and test.cd
6. run java -Xms2g -Xmx4g -jar berkeleyaligner.jar ++.conf configuration.conf

The last command will create a folder ~/SOParallelCorpusReplication/BerkeleyAligner/output and fill in the folder with many files. Among the files we need only stage2.1.params.txt. This file is the first argument for [AlignmentEntropyStat.py](https://github.com/mrsumitbd/SOParallelCorpusReplication/blob/master/SourceCode/AlignmentEntropyStat.py).
