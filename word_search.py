#! /usr/bin/env python3

import re

if __name__ == "__main__":
    herit_pattern_str = r'\w*herit\w*'
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE)
    print('Opening origin.txt')
    with open('origin.txt', 'r') as in_stream:
        print('Opening output_origin.txt')
        with open('output_origin.txt', 'w') as out_stream:
            for line_index, line in enumerate(in_stream):
                 line = line.strip()
                 word_list = line.split()
                 word_list.sort()
                 for word in word_list:
                     if herit_pattern.search(word):
                         out_stream.write(f'Line: {line_index}\t{word}\n')
print("Done!")
print('dummy.txt is closed?', in_stream.closed)
print('output_origin.txt is closed?', out_stream.closed)

