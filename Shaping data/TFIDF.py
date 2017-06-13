from sklearn.datasets import fetch_20newsgroups
import sklearn.feature_extraction.text as ext

categories = ['sci.space']

twenty_train = fetch_20newsgroups(subset='train',
                                categories = categories,
                                remove=('header','footers','quotes'),
                                shuffle=True,
                                random_state=42)
count_vect = ext.CountVectorizer()
X_train_counts = count_vect.fit_transform(
                    twenty_train.data)


tfidf = ext.TfidfTransformer().fit(X_train_counts)
X_train_tfidf = tfidf.transform(X_train_counts)

print(X_train_tfidf.shape)
