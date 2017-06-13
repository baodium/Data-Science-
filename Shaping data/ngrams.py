from sklearn.datasets import fetch_20newsgroups
import sklearn.feature_extraction.text as ext


categories = ['sci.space']

twenty_train = fetch_20newsgroups(subset='train',
                                 categories = categories,
                                 remove = ('headers', 'footers', 'quotes'),
                                 shuffle = True,
                                 random_state=42)
count_chars = ext.CountVectorizer(analyzer='char_wb', ngram_range=(3,3),
                                 max_features=10).fit(twenty_train['data'])
count_words = ext.CountVectorizer(analyzer='word', ngram_range=(2,2),
                                 max_features=10,
                                 stop_words='english').fit(twenty_train['data'])

X = count_chars.transform(twenty_train.data)

print(count_words.get_feature_names())
print(X[1].todense())
print(count_words.get_feature_names())
