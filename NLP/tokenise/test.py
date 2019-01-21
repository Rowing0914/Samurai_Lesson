# japanese
# https://qiita.com/haruhiko28/items/3ac9b9ab3a2d522d5877
import MeCab

text = 'Pythonを使って、機械学習を勉強する。'

tagger = MeCab.Tagger("-Owakati")

#str型で、単語が空白で別れる
str_output = tagger.parse(text)
print(str_output)
print(type(str_output))

#listに変換する
list_output = str_output.split(' ')
print(list_output)
print(type(list_output))


# english
# https://qiita.com/okayu9/items/a123d1a2ef3a9a90fd66
import nltk

sentence = "You have eaten lunch, haven't you?"
print(nltk.word_tokenize(sentence))