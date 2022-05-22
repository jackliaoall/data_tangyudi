from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split


def naive_bayes():
    news = fetch_20newsgroups()

    # 进行数据分割
    X_train, X_test, y_train, y_test = train_test_split(news.data, news.target)

    # 对数据集进行特征抽取
    td = TfidfVectorizer()
    #在训练集和测试集数据预处理时，需要对数据进行标准化
    # 训练集使用fit_transform
    # 测试集使用transform
    X_train = td.fit_transform(X_train)

    X_test = td.transform(X_test)

    #实例化贝叶斯
    nb = MultinomialNB(alpha=1)

    nb.fit(X_train, y_train)

    y_predict = nb.predict(X_test)
    #输出预测精度
    print('The accuracy of Navie Bayes Classifier is', nb.score(X_test, y_test))
    print(classification_report(y_test, y_predict, target_names=news.target_names))


if __name__ == '__main__':
    naive_bayes()
