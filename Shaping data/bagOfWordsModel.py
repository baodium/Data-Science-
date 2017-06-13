from sklearn.datasets import fetch_20newsgroups
import sklearn.feature_extraction.text as ext

categories = ['comp.graphics', 'misc.forsale','rec.autos','sci.space']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

count_vect = ext.CountVectorizer()
x_train_counts = count_vect.fit_transform(twenty_train.data)

print(x_train_counts.shape)
