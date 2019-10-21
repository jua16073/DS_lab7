#import pillow
import wordcloud

file = open('data.txt', 'r+')
data = file.readlines()
file.close()

data = data[0].split(";")
print(len(data))
# for line in data:
#   print(line)