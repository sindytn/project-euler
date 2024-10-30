"""
Find the number of words which sum to triangle numbers when their chars are converted to
ints. Given word bank here: https://projecteuler.net/resources/documents/0042_words.txt

Approach:
Brute force. Precompute the triangle numbers which can be no more than 
26 * <max_word_length> since 'Z' maps to 26. Then we iterate through the word bank and 
check the sums.
"""
import argparse
import csv

def coded_triangle_numbers(words):
    # Precompute triangle numbers
    triangle_numbers = []
    max_word_len = len(max(words, key=len))
    for n in range(1, max_word_len * 26):
        triangle_num = n * (n + 1) // 2
        triangle_numbers.append(triangle_num)
        if triangle_num >= max_word_len * 26:
            break

    # Count triangle words
    char_to_num = {chr(num): num - ord('A') + 1 for num in range(ord('A'), ord('Z') + 1)}
    triangle_words = []
    num_triangle_words = 0
    for word in words:
        if sum([char_to_num[char] for char in word]) in triangle_numbers:
            num_triangle_words += 1
            triangle_words.append(word)
    # print(triangle_words)
    return num_triangle_words 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='file with words separated by commas')
    parser.add_argument('filename', type=str, help='The path to the file to process.')

    args = parser.parse_args()
    with open(args.filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',', quotechar='"')
        words = next(csv_reader)
        print(f"Result = {coded_triangle_numbers(words)}")