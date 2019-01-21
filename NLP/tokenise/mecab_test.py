import MeCab

text = 'Pythonを使って、機械学習を勉強する。'

tagger = MeCab.Tagger("-ochasen")

#str型で、単語が空白で別れる
str_output = tagger.parse(text)
print(str_output)
print(type(str_output))

#listに変換する
list_output = str_output.split(' ')
print(list_output)
print(type(list_output))