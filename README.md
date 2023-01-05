# ANLY-580 Final Project: Identifying Market Sentiment for Financial Market Signals
This project is in fulfillment of ANLY-580 Natural Lagunage Processing of MS Data Science & Analytics at Georgetown University in Fall 2022.

<b>Team members:</b>\
Yuejiao Qiu\
Ruoting Shen\
Yuening Wang\
Xiana Zhang

## Introduction
This project performs sentiment classifications on the financial tweets, trying out different methodologies and architectures, such as Bag-of-Words (BOW) model and fine-tuned BERT model. In addition, we also build a LSTM model to incorporate Reddit sentiments and techinical indicators to predict stock price movement.

## Dataset
The various datasets used for sentiment analysis and price movement prediction are located in [/data](/data).

## Code
### Sentiment Analysis
For sentiment analysis, the models we deployeda are:
1. [Bag-of-words](/code/1_bag_of_words.ipynb)
2. [BERT w/o fine tuning](code/2_fin_sentiment_bert_w_o_fine_tune.ipynb)
3. [BERT w/ fine tuning](code/3_fin_sentiment_bert_w_fine_tune.ipynb)
4. [Pre-tuned BERT w/o fine tuning](code/4_pre-tuned_bert_wo_fine_tune.ipynb)
5. [Pre-tuned BERT w/ fine tuning](code/5_pre-tuned_bert_w_fine_tune.ipynb)

Among which 4. and 5. are based on the pre-trained BERT mode on Sentiment140 which contains 120,000 general tweets ([pre-tuned BERT](code/fine_tune_bert_with_Sentiment140.ipynb)).

### Stock Price Movement Prediction
Model evaluation are done with the GME historic prices and Reddit submissions, where a LSTM is established, as well as other analysis, i.e. correlation. The primary code is accessible at [code/gme_eval.ipynb](code/gme_eval.ipynb).

## Summary
Detailed summary of this project can be accessed at either [presentation_slides](/presentation_slides.pdf) or [final_report](/final_report.pdf).