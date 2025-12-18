from text_analizer import unique_words, word_frequency, longer_word, shorter_word, word_filter, count_by_lenght

# unique_words
assert len(unique_words("hola hola mundo")) == 2, "unique_words failed and not returned the correct number of words..."
assert unique_words("hola hola mundo") == {"hola", "mundo"}, "unique_words failed and not returned the correct words..."

# word_frequency
assert word_frequency("Hola hola mundo")["hola"] == 2, "word_frequency failed and not count words correctly..."
assert word_frequency("Hola hola mundo")["mundo"] == 1, "word_frequency failed and not count words correctly..."

# longer_word
assert longer_word("Me llamo Noemí y vivo en Huesca") == "Huesca", "longer_word failed and not returned the longest word..."

# shorter_word
assert shorter_word("Me llamo Noemí y vivo en Huesca") == "y", "shorter_word failed and not returned the shortest word..."

# word_filter
assert word_filter(["Hola", "que", "tal"], ["que"]) == ["Hola", "tal"], "word_filter failed and not filtered the words correctly..."

# count_by_lenght
assert count_by_lenght("Hola que tal")[4] == 1, "count_by_lenght failed and not count words correctly..."
assert count_by_lenght("Hola que tal")[3] == 2, "count_by_lenght failed and not count words correctly..."

print("All tests passed successfully!")