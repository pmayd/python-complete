# Bite 105. Slice and dice

Take the block of text provided and `strip` off the whitespace at both ends. Split the text by newline (`\n`).

Loop through the lines, for each line:

- strip off any leading spaces,
- check if the first character is lowercase,
- if so, split the line into words and get the last word,
- strip the trailing dot (.) and exclamation mark (!) from this last word,
- and finally add it to the `results` list.

Return the `results` list.
