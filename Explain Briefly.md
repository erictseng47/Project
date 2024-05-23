### Questions:

1. **How did you vectorize the comments? / Is the algorithm you chose reasonable?**

2. **How do you calculate the accuracy of the sentiment predictor?**

3. **How do you calculate the inference speed?**

4. **What steps will you take next to improve this solution?**

---

### Answers:

1. I utilized TextBlob for sentiment analysis, a library capable of converting textual comments into sentiment polarity scores, where polarity values range from -1 to 1, representing the degree of negativity to positivity in sentiment. This approach is reasonable as TextBlob employs rule-based machine learning techniques and performs well in the field of natural language processing.

2. I calculate the accuracy of the sentiment predictor through the following steps:
   - Firstly, I fetch a review from IMDb.
   - Then, I perform sentiment analysis on this review using TextBlob to obtain its sentiment polarity score.
   - Finally, I can compute accuracy by comparing with manually labeled sentiment labels. For instance, if the sentiment polarity score is greater than 0, we classify it as a positive review; if it's less than 0, it's classified as a negative review. Then, I compare the model's prediction with the actual sentiment label to calculate prediction accuracy.

3. The calculation of inference speed depends on the length of the text and the performance of the library. In this script, the inference speed is primarily influenced by the sentiment analysis function of TextBlob. Typically, the inference speed of TextBlob is fast, completing sentiment analysis in milliseconds.

4. To improve this solution, I could take the following measures:
   - Consider using more complex sentiment analysis models, such as deep learning models, to enhance prediction accuracy.
   - Gather more training data to improve the model's generalization ability.
   - Optimize the code to improve inference speed, such as utilizing parallel processing or using more efficient libraries for sentiment analysis.
   - Add more features, such as text preprocessing or feature extraction, to enhance the accuracy and robustness of sentiment analysis.
