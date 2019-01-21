import json
from mlask import MLAsk
emotion_analyzer = MLAsk()

# # non-formatted response
# print(emotion_analyzer.analyze('彼のことは嫌いではない！(;´Д`)'))

# # json formatted response
# res = json.dumps(emotion_analyzer.analyze('彼のことは嫌いではない！(;´Д`)'), ensure_ascii=False)
# print(res)

# beautifiered json formatted response
# res = json.dumps(emotion_analyzer.analyze('彼のことは嫌いではない！(;´Д`)'), sort_keys=True, indent=4, ensure_ascii=False)
# print(res)
# print(emotion_analyzer.analyze('彼のことは嫌いではない！(;´Д`)')['emotion'])

result = {}
message = ["ゲームをするのが楽しいです", "好きなことは本を読むことです", "今後も頑張ります。"]

for index, line in enumerate(message):
	temp = emotion_analyzer.analyze(line)
	if temp["emotion"] != None:
		result[str(index)] = {"message" : temp["text"], "emotion" : temp["emotion"], "intension" : temp["intension"], "orientation" : temp["orientation"]}
	else:
		result[str(index)] = {"message" : temp["text"], "emotion" : False, "intension" : False, "orientation" : False}
print(result)