# Emoji-Prediction_NeuralNetworks
# Introduction
People use emoji every day. 
Emoji has become a new language that allows us to express ideas and emotions more effectively. 
Right now, the keyboard on iOS/Android can predict emojis but only base on certain keywords and tags that are associated with emojis.
# Problem statement
Emoji prediction, which estimates an upcoming emoji based on the given text, is considered to be one of the most important NLP tasks concerning emojis.

Our aim is to predict the most relevant emoji by considering the emotion detection task. Consider a tweet, and with the help of emotion detection - our model will predict emojis related to that text.

Emoji prediction is useful in multiple domains such as for sentiment analysis, emotion recognition, irony detection and hate-speech recognition.

For better understanding refer to the ppt attached.
# Dataset
TWITTER DATASET:
Dataset has been taken from github repo of MultiEmo:[ Multi-task framework for emoji prediction research paper](https://github.com/sange1104/MultiEmo).
Each row represents a twitter post including at least one emoji of the top 64 emojis. The data we used for training includes posts with only one emoji.
Number of examples : 1,069,910.
Number of labels : 1

GOEMOTION DATASET :
Dataset has been taken from github repo of Google Research GoEmotion: https://github.com/google-research/google-research/tree/master/goemotions
GoEmotions is a corpus of 58k carefully curated comments extracted from Reddit, with human annotations to 27 emotion categories or Neutral.
Number of examples: 58,009.
Number of labels: 27 + Neutral.
Maximum sequence length in training and evaluation datasets: 30.


