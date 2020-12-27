def bag_of_words(code):
 keywords = (
  'printf', 'scanf', 'else:', 'Scanner', 'Static', 'print', '%d', 'import', 'def', '%f', 'println', 'public', 'range',
  'int', 'String', 'in', 'for', 'args[]', 'elif', 'main', 'sizeof', 'numpy', 'System', 'out', 'pandas', 'Integer',
  'while', 'as', 'from', 'void', 'return')


 code = code.replace('(', ' ')

 code = code.replace('.', ' ')

 splitted = code.split(" ");

 vector1 = [];
 while '' in splitted: splitted.remove('')
 for x in splitted:
  if (x in keywords):
   vector1.append(x)

 vector2 = []
 for x in range(len(keywords)):
  vector2.append(0)

 i = 0
 for i in range(len(keywords)):
  if keywords[i] in splitted:
   x = keywords.index(keywords[i])
   vector2[x] = vector2[x] + 1
   i = i + 1

 return vector2




def function2(op):
    import numpy as np
    import pandas as pd
    Z = pd.read_csv("home/D1.csv")

    # int  main void Scanner #include<stdio.h> System public import printf scanf
    # 1 is java and 0 is c
    #  X = np.array([[2,1,0,0,1,0,0,0,1,3],[1,1,1,4,0,2,2,1,0,0],[2,1,0,0,1,0,0,0,3,1],[2,3,1,1,0,2,2,1,0,0],[2,1,0,0,1,0,0,0,3,1]])
    # y = np.array([0,1,0,1,0])
    # print(X)
    # print(y)

    xsam = Z[
        ['printf', 'scanf', 'else:', 'Scanner', 'Static', 'print', '%d', 'import', 'def', '%f', 'println', 'public',
         'range', 'int', 'String', 'in', 'for', 'args[]', 'elif', 'main', 'sizeof', 'numpy', 'System', 'out', 'pandas',
         'Integer', 'while', 'as', 'from', 'void', 'return']]
    ysam = Z['output']
    print("xasm")
    print(xsam)
    print("yasm")
    print(ysam)

    X = np.array(xsam)
    X.reshape(1, -1)
    print("X")
    print(X)
    y = np.array(ysam)
    y.reshape(1, -1)
    print("y")
    print(y)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb.fit(X_train, y_train)

    print("op")
    print(op)
    op=np.array([op])
    y_pred = gnb.predict(op);

    print(y_pred)

    if (y_pred == 0):
        ans="This is c."
    elif (y_pred == 1):
        ans="This is java  Program."
    else:
        ans="This is python."

    return (ans)

def function1():
    import numpy as np
    import pandas as pd
    Z = pd.read_csv("home/D1.csv")

    xsam = Z[
        ['printf', 'scanf', 'else:', 'Scanner', 'Static', 'print', '%d', 'import', 'def', '%f', 'println', 'public',
         'range', 'int', 'String', 'in', 'for', 'args[]', 'elif', 'main', 'sizeof', 'numpy', 'System', 'out', 'pandas',
         'Integer', 'while', 'as', 'from', 'void', 'return']]
    ysam = Z['output']
    print(xsam)
    print(ysam)

    X = np.array(xsam)
    X.reshape(1, -1)
    print(X)
    y = np.array(ysam)
    y.reshape(1, -1)
    print(y)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb.fit(X_train, y_train)

    y_pred = gnb.predict(X_test);

    print(y_pred)
    from sklearn import metrics
    return ("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred) * 100)


