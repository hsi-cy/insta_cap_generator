import random
import pandas as pd


def linebreak(content):
    """create linebreak in IG"""
    return [line.rstrip().lstrip() + "\n" for line in content]


def produce_hashtags(choice_of_tags):
    """
    1. Read the pre-processed tags.csv file
    2. Create a set of hashtags depending on the input value
    3. Return a set of hashtags
    """
    tags_file = pd.read_csv("tags.csv")
    col_names = tags_file.columns.tolist()
    if choice_of_tags.lower() == "birds":
        all_tags = []
        for i in range(4):
            all_tags += tags_file[col_names[i]].dropna().tolist()
        hashtags = [("#" + i + " ") for i in random.choices(all_tags, k=25)]
        return hashtags
    else:
        all_tags = []
        for i in ["Taiwan tags", "Wildlife tags", "Other tags"]:
            all_tags += tags_file[i].dropna().tolist()
        hashtags = [("#" + i + " ") for i in random.choices(all_tags, k=25)]
        return hashtags


def main():
    """
    The main function. Takes 4 inputs the species name, date, content,
    bird or animal hashtag
    """
    species = input("Please Enter Species\n").strip()
    eng_caption = linebreak(input("Please Enter Eng Caption\n").split("\\n"))
    ch_caption = linebreak(input("Please Enter Ch Caption\n").split("\\n"))
    date = input("Please Enter Date\n").strip()
    sonytags = "#sonya6500 ,#sel70350g ,#captureonepro"
    footer = [
        ".\n",
        "Nature is all around us!\n",
        "So Open Your Mind, Be Curious, and Care More\n",
        "#hcy_wildlife_photography",
    ]
    choice_of_tags = input("Birds or Non-birds?\n")
    hashtags = produce_hashtags(choice_of_tags)

    with open("post.txt", "w", encoding="utf-8") as file:
        file.write("#" + species + "\n")
        file.writelines(eng_caption)
        file.write(".\n")
        file.writelines(ch_caption)
        file.write(".\n")
        file.write("Date: " + date + "\n")
        file.write(".\n")
        file.write(sonytags)
        file.write(".\n")
        file.writelines(footer)
        file.write(".\n")
        file.writelines(hashtags)


if __name__ == "__main__":
    main()