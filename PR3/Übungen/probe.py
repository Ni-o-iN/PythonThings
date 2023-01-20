from textblob import TextBlob

text = "Hallo ich bin nico und das ist ein test hallo nico hallo hallo hallo nico test und das"
blob = TextBlob(text)
print(blob)
print(blob.words)


