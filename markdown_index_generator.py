#!/usr/bin/python3

# Modules
import os
import sys
import errno
import pathlib
import slugify


# Global variables
DEFAULT_SPACE_LENGHT = "  "


# Print help about this script
def print_help() -> None:
    """
    Prints the help message to the standard output.
    """
    help_str = """
    This script prints the index of a file written in Markdown.
    Each title in the index embed a working section link to redirect
    to the proper section in the file.

    You need to specify a valid file path as an argument to use this script.
    """
    print(help_str)


def generate_index(filepath: str) -> None:
    """
    Build the index of a Markdown file and prints it to the standard output.

    Arguments:
      :param:filepath: the path of the Markdown file to create index from.

    Returns:
      None
    """
    with open(file=filepath, mode="r") as readme_file:
        # An identifier here is any "```" string
        identifiers_count = 0

        for line in readme_file.readlines():
            splitted_line = line.split()
            if line != "\n":
                if line.startswith("```"):
                    identifiers_count += 1

                # We must not consider any hashtag between two identifiers
                elif line.startswith("#") and identifiers_count % 2 == 0:
                    title = ' '.join(splitted_line[1:])
                    hashtags_count = len(splitted_line[0])
                    space_indent = "" if hashtags_count == 0 else DEFAULT_SPACE_LENGHT * (hashtags_count - 1)
                    print(f"{space_indent}- [{title}](#{slugify.slugify(text=title)})", end="\n")


# Main function
def main() -> None:
    """
    The main function of this script. It must only be run once right after the script execution.

    Arguments:
      None

    Returns:
      None
    """

    # Check if a file is given in argument and if it's a file
    if len(sys.argv) != 2:
        print("Error! You must specify a valid file path as an argument to use this script!")
    else:
        input_file_path = sys.argv[1]

        # If help command
        if input_file_path == "--help" or input_file_path == "-h":
            print_help()

        # Else if a valid file path
        elif pathlib.Path(input_file_path).is_file():
            generate_index(filepath=input_file_path)

        else:
            print(FileNotFoundError(errno.ENOENT, f"{os.strerror(errno.ENOENT)} to read from", input_file_path))
    return None
   

if __name__ == "__main__":
    main()
