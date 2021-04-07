from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    #line_words = line.split()   ### em bytes
    line_words = line.decode('utf8').split()  ## em strings
    for word in line_words:
        story_words.append(word)
story.close()
#transferido bytes ao invés da string. HTTP data is provided as bytes.
print(story_words)




