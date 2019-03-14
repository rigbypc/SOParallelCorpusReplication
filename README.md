We downloaded the StackOverflow dump which is hosted on this [link](https://archive.org/details/stackexchange). The data are in XML format. We parsed the XML files and dumped the data into a database using the [DumpSO.py](https://github.com/mrsumitbd/SOParallelCorpusReplication/blob/master/SourceCode/DumpSO.py) script. This corpus contains only Android posts. For another paper, we created a similar corpus of [general Java posts](https://github.com/CESEL/CodeEntropyReplication).


# Links to Data
## [C0: Raw data approach (Data, alignment and usages)](https://drive.google.com/file/d/1M3TRvdhZbLnfX_8363wdmvbsGGSpl1B3/view?usp=sharing)	
## [C1: Thread title approach (Data, alignment and usages)](https://drive.google.com/file/d/1bNg16x1jJQZAKYdScsbEpfNQ_Tc4aCcu/view?usp=sharing)	
## [C2: Standard NLP approach (Data, alignment and usages)](https://drive.google.com/file/d/1Y9Lg5S-KigY1jspaHOTe2tvCPOUk0pFY/view?usp=sharing)	
## [C3: Software engineering task approach (Data, alignment and usages)](https://drive.google.com/file/d/1X52lrEyKNKdMuSmX-1edvpFmm5FYmNpG/view?usp=sharing)

Each data set consists of three folders: Alignment, Corpora and Usages. Contents in each folder are as follows:

| Folder | Content |
| ------ | -------- |
| Alignment | CSV file containing the Per-word entropy values plotted in Figure 2 in the paper. |
| Corpora | Two text files: eng.txt and code.txt. These files contain the english and code corpora. |
| Usages | Two files with .dict extensions. Each file contains the usage frequencies for every English and code tokens. There are three columns in the files. The columns are explained in the following section. |



# Processing Data with [OpenNMT](http://opennmt.net/)
cd ~/OpenNMT
1. For tokenization run from command line:
th tools/tokenize.lua -mode space < ~/data/eng.txt > ~/data/eng.tok
th tools/tokenize.lua -mode space < ~/data/code.txt > ~/data/code.tok

2. For creating the dictionary run from the command line:
th preprocess.lua -train_src ~/data/eng.tok -train_tgt ~/data/code.tok -keep_frequency true -save_data ~/data/dictionary

For each corpus there will be a dictionary with three columns (tab separated).

Example:

| token | 1-indexed token id | Occurance frequency |
| ------------- | ------------- | ------------- |
| Drawable.Drawable |	5 |	658 |

The first four tokens of each dictionary contains:

`<blank>`

`<unk>`

`<s>`

`</s>`

So, we remove them.

Besides creating the dictionary (the .dict files) previous command creates a binrary file with .t7 extension. For our purpose we do not need that file.

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
