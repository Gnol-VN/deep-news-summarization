from pyvi.pyvi import ViTokenizer

def tokenizeAndWritefile(sentence):
    file = open("testfile.txt","a")
    list = ViTokenizer.tokenize(sentence).split()
    # for i in list:
    #     file.write(i+"\n")
    # file.close()

inputFile = open("article.txt",'r')
for line in inputFile:
    tokenizeAndWritefile("Bữa trưa có mỗi cái gỏi cuốn mà cũng phải chụp ảnh đẹp xong mới đc ăn ")

uniqlines = set(open('testfile.txt').readlines())
bar = open('aftertest.txt', 'w').writelines(set(uniqlines))

bar.close()