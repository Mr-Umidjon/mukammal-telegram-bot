import wikipedia

wikipedia.set_lang('uz')

# print(wikipedia.search('Sharqiy Turkiston'))
response = wikipedia.summary('odam')

for x in range(0, len(response), 4095):
    print(response[x:x+4095])