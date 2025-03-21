#!/usr/bin/env python3

import os

# Define the shebang line
shebang = "#!/usr/bin/env python3\n"

# Specify the root directory containing your Python files
root_directory = "./"  # Current directory (you can change this to the path of your directory)

# Walk through the directory tree recursively
for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith(".py") and filename != "__init__.py":  # Exclude __init__.py
            filepath = os.path.join(dirpath, filename)

            # Read the existing content of the file
            with open(filepath, "r") as file:
                content = file.read()

            # Write the shebang line followed by the original content
            with open(filepath, "w") as file:
                file.write(shebang + content)

            print(f"Added shebang to {filepath}")
