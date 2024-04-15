# find_longest_word
show longest word in text
#
#
def get_longest_word_idx(string_):
Definiuje funkcję get_longest_word_idx, która przyjmuje jeden argument, string_, będący ciągiem znaków.
#
words = string_.split()
Dzieli ciąg znaków na listę słów, używając metody split(). Domyślnie split() dzieli ciąg na podstawie białych znaków, takich jak spacje, ale możemy również podać separator jako argument tej metody.
#
longest_word = ""
longest_word_index = -1
Inicjuje zmienne longest_word i longest_word_index jako puste ciągi znaków i -1 odpowiednio. Będziemy używać tych zmiennych do śledzenia najdłuższego słowa i jego indeksu w ciągu.
#
for idx, word in enumerate(words):
Rozpoczyna pętlę for, która przechodzi przez każde słowo w liście words, jednocześnie śledząc indeksy tych słów za pomocą funkcji enumerate().
#
if len(word) > len(longest_word):
Sprawdza, czy aktualne słowo (word) jest dłuższe niż najdłuższe słowo znalezione dotychczas (longest_word) poprzez porównanie ich długości za pomocą funkcji len().
#
longest_word = word
longest_word_index = idx
Jeśli aktualne słowo jest dłuższe, aktualizuje longest_word na to słowo i longest_word_index na jego indeks.
#
return longest_word, longest_word_index
Zwraca krotkę zawierającą najdłuższe słowo (longest_word) i jego indeks (longest_word_index).
#
string_ = "Hello, my best day ever-ever!"
print(get_longest_word_idx(string_))
Przypisuje ciąg znaków do zmiennej string_ i drukuje wynik wywołania funkcji get_longest_word_idx na tym ciągu, aby zobaczyć najdłuższe słowo i jego indeks.
