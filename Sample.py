import json
msg = "Interpreter Test"
demoVar = "DemoVar"
print(msg)
print("Test success")
# testVar = input()
# print(testVar)
sampleJson='{"name":"John","age":30,"cars":[ "Ford", "BMW", "Fiat" ]}'
jsonData = json.loads(sampleJson)
print(jsonData)

if jsonData == 2:
    print(True)
else:
    print(False)

