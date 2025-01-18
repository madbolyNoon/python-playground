import re

"""
Guidelines for Regular Expressions in Python:

1. Always use raw strings (`r''`) when defining regular expressions to avoid misinterpretation of escape sequences.
   - Example: Use `r'\b\w{2}\b'` instead of `'\b\w{2}\b'` to correctly interpret `\b` as a word boundary.
   - Without the raw string, `\b` is treated as a backspace character (ASCII \x08) by Python, leading to unexpected behavior.

2. Key Special Characters in Regular Expressions:
   - `.`       Matches any character except a newline.
   - `^`       Matches the start of the string.
   - `$`       Matches the end of the string or just before the newline.
   - `*`       Matches 0 or more repetitions of the preceding character or group.
   - `+`       Matches 1 or more repetitions of the preceding character or group.
   - `?`       Matches 0 or 1 repetition of the preceding character or group.
   - `{m,n}`   Matches between m and n repetitions of the preceding character or group.
   - `\`       Escapes special characters or introduces a special sequence.
   - `[]`      Denotes a set of characters; `[^]` for a complementing set.
   - `|`       Matches either pattern A or pattern B (e.g., `A|B`).
   - `(...)`   Groups patterns for later reference or matching.
   - `(?:...)` Non-grouping version of parentheses.
   - `(?P<name>...)` Matches and names the group for later reference.
   - `(?=...)` Positive lookahead; ensures ... follows.
   - `(?!...)` Negative lookahead; ensures ... does not follow.
   - `(?<=...)` Positive lookbehind; ensures ... precedes (fixed length).
   - `(?<!...)` Negative lookbehind; ensures ... does not precede (fixed length).
   - `(?#...)` Inline comments ignored by the parser.
"""

# Input text
input_text = "This is a sample text"

# Example 1: Replace spaces with hyphens
pattern = re.compile(r"\s")  # Matches whitespace characters
print(pattern.sub("-", input_text))  # Output: "This-is-a-sample-text"

# Example 2: Replace occurrences of " is" with " was"
pattern = re.compile(r"\sis")  # Matches " is" with a leading space
print(pattern.sub(" was", input_text))  # Output: "This was a sample text"

# Example 3: Convert all lowercase letters to uppercase
pattern = re.compile(r"[a-z]")  # Matches lowercase letters
print(pattern.sub(lambda x: x.group(0).upper(), input_text))  # Output: "THIS IS A SAMPLE TEXT"

# Example 4: Match words ending with 't' and print their positions
pattern = re.compile(r"t$")  # Matches 't' at the end of the string
for match in pattern.finditer(input_text):
    print(f"Match: {match.group(0)}, Start: {match.start()}, End: {match.end()}")

# Example 5: Find all two-character words
pattern = re.compile(r"\b\w{2}\b")  # Matches two-character words surrounded by word boundaries
print(pattern.findall(input_text))  # Output: ['is']