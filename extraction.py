import json
import os

# clean up invalid characters
def sanitize_filename(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '^', '@']
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename

# create 'authors' directory if we dont have one
os.makedirs('authors', exist_ok=True)

# load json data from trick files of any map, replace this
with open('filename.json', 'r', encoding='utf-8') as file:
    tricks = json.load(file)

# organize tricks by author
organized_tricks = {}
for trick in tricks:
    author = trick['author']
    if author not in organized_tricks:
        organized_tricks[author] = []
    # grab only the stuff we want 2 see
    simplified_trick = {
        'Trick Name': trick.get('name', 'N/A'),
        'Tier': trick.get('tier', 'N/A'),
        'Points': trick.get('points', 'N/A')
    }
    organized_tricks[author].append(simplified_trick)

# save each authors tricks in its own file
for author, tricks in organized_tricks.items():
    sanitized_author = sanitize_filename(author)  # more cleanup to create valid filename
    filename = os.path.join('authors', f"{sanitized_author}.json")  # prolly could have used author id to avoid dis but idk enuf abt it
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(tricks, file, ensure_ascii=False, indent=4)  # write the data 2 the file

print("cash money success. saved to authors directory.")
