def classify(features_train, labels_train):
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(features_train, labels_train)
    return clf