library(vioplot)
library(devtools)
library(digest)

#Generating usage frequency

title_eng_vocab <- read.csv("Data/C1_Title_Data/Usages/eng.dict", header = FALSE, sep='\t')
title_code_vocab <- read.csv("Data/C1_Title_Data/Usages/code.dict", header = FALSE, sep='\t')

freq_title_eng_vocab <- subset(title_eng_vocab, title_eng_vocab$V3 > 1) #Ignoring tokens used only once
freq_title_code_vocab <- subset(title_code_vocab, title_code_vocab$V3 > 1)

length(freq_title_eng_vocab$V3)
length(freq_title_code_vocab$V3)

summary(freq_title_eng_vocab$V3)
summary(freq_title_code_vocab$V3)

title_alignment <- read.csv("Data/C1_Title_Data/Alignment/eng2code_alignment_entropy.csv", header = FALSE, sep='\t')

summary(title_alignment$V1)


rake_eng_vocab <- read.csv("Data/C2_StandardNLP/Usages/eng.dict", header = FALSE, sep='\t')
rake_code_vocab <- read.csv("Data/C2_StandardNLP/Usages/code.dict", header = FALSE, sep='\t')

freq_rake_eng_vocab <- subset(rake_eng_vocab, rake_eng_vocab$V3 > 1)
freq_rake_code_vocab <- subset(rake_code_vocab, rake_code_vocab$V3 > 1)

length(freq_rake_eng_vocab$V3)
length(freq_rake_code_vocab$V3)

summary(freq_rake_eng_vocab$V3)
summary(freq_rake_code_vocab$V3)


rake_alignment <- read.csv("Data/C2_StandardNLP/Alignment/eng2code_alignment_entropy.csv", header = FALSE, sep='\t')

summary(rake_alignment$V1)


raw_eng_vocab <- read.csv("Data/C0_Raw/Usages/eng.dict", header = FALSE, sep='\t')
raw_code_vocab <- read.csv("Data/C0_Raw/Usages/code.dict", header = FALSE, sep='\t')

freq_raw_eng_vocab <- subset(raw_eng_vocab, raw_eng_vocab$V3 > 1)
freq_raw_code_vocab <- subset(raw_code_vocab, raw_code_vocab$V3 > 1)

length(freq_raw_eng_vocab$V3)
length(freq_raw_code_vocab$V3)

summary(freq_raw_eng_vocab$V3)
summary(freq_raw_code_vocab$V3)



raw_alignment <- read.csv("Data/C0_Raw/Alignment/eng2code_alignment_entropy.csv", header = FALSE, sep='\t')

summary(raw_alignment$V1)

task_eng_vocab <- read.csv("Data/C3_SETask/Usages/eng.dict", header = F, sep='\t')
task_code_vocab <- read.csv("Data/C3_SETask/Usages/code.dict", header = F, sep='\t')

freq_task_eng_vocab <- subset(task_eng_vocab, task_eng_vocab$count > 1)
freq_task_code_vocab <- subset(task_code_vocab, task_code_vocab$count > 1)

length(freq_task_eng_vocab$V3)
length(freq_task_code_vocab$V3)

summary(freq_task_eng_vocab$V3)
summary(freq_task_code_vocab$V3)

task_alignment <- read.csv("Data/C3_SETask/Alignment/eng2code_alignment_entropy.csv", header = FALSE, sep='\t')
summary(task_alignment)

summary(task_alignment$V1)


#Generating violinplot


source_url("https://gist.githubusercontent.com/mbjoseph/5852613/raw/1f4c940b703b0e2d2b480abaed25a896a10ef92d/vioplot2")

png(filename="per-word_alignment.png")
par(cex.lab=1.2,cex.axis=1.05)

plot(x=NULL, y=NULL,
     xlim = c(0.6, 4.4),
     ylim = c(0,max(raw_alignment$V1)),
     type="n", ann=FALSE, axes=F)
axis(1, at=c(1,2,3,4),  labels=c("Raw Corpus", "Title Corpus", "Standard NLP", "SE Task Copus"))
axis(2)


vioplot2(raw_alignment$V1,at = 1, col = 'white', add = T)


vioplot2(title_alignment$V1, at = 2, col = 'white' , add = T)


vioplot2(rake_alignment$V1, at = 3, col = 'white' , add = T)

vioplot2(task_alignment$V1, at = 4, col = 'white' , add = T)


title("", xlab="", ylab = "Per-word alignment entropy")

dev.off()

