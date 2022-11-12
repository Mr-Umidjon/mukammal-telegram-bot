import wikipedia

wikipedia.set_lang('uz')

print(wikipedia.summary('odam', sentences=10))