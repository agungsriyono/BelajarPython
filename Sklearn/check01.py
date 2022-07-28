from sklearn.datasets import load_iris
iris = load_iris()
print(iris.keys())

print(iris.DESCR)

x=iris.data
print(x)

y=iris.target
print(y)