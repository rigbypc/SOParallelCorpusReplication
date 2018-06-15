# Links to Data

## [C0: Raw data approach (Data, alignment and usages)](https://drive.google.com/file/d/1M3TRvdhZbLnfX_8363wdmvbsGGSpl1B3/view?usp=sharing)
## [C1: Thread title approach (Data, alignment and usages)](https://drive.google.com/file/d/1bNg16x1jJQZAKYdScsbEpfNQ_Tc4aCcu/view?usp=sharing)
## [C2: Standard NLP approach (Data, alignment and usages)](https://drive.google.com/file/d/1Y9Lg5S-KigY1jspaHOTe2tvCPOUk0pFY/view?usp=sharing)
## [C3: Software engineering task approach (Data, alignment and usages)](https://drive.google.com/file/d/1X52lrEyKNKdMuSmX-1edvpFmm5FYmNpG/view?usp=sharing)

## [Code used for Evaluation](https://github.com/mrsumitbd/SOParallelCorpusReplication/tree/master/SourceCode)


# Processing Data with [OpenNMT](http://opennmt.net/)
cd ~/OpenNMT
1. For tokenization run from command line:
th tools/tokenize.lua -mode space -nparallel 4 < ~/data/eng.txt > ~/data/eng.tok
th tools/tokenize.lua -mode space -nparallel 4 < ~/data/code.txt > ~/data/code.tok

2. For creating the dictionary run from the command line:
th preprocess.lua -train_src ~/data/eng.tok -train_tgt ~/data/code.tok -keep_frequency true -save_data ~/data/dictionary

Besides creating the dictionary previous command creates a binrary file with .t7 extension. For our purpose we do not need that file.

rm ~/data/*.t7
