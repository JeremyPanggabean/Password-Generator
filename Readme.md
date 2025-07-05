# PyPassword Generator

A simple Python password generator that creates secure, randomized passwords with customizable character types and lengths.

## Features

- **Customizable Length**: Choose how many letters, symbols, and numbers you want in your password
- **Random Generation**: Uses Python's `random` module to ensure unpredictable password creation
- **Character Variety**: Includes lowercase letters, uppercase letters, numbers, and special symbols
- **Shuffled Output**: Characters are randomly shuffled to avoid predictable patterns

## Character Sets

- **Letters**: `a-z`, `A-Z` (52 characters total)
- **Numbers**: `0-9` (10 characters total)
- **Symbols**: `!`, `#`, `$`, `%`, `&`, `(`, `)`, `*`, `+` (9 characters total)

## How It Works

1. The program prompts you to specify how many characters of each type you want
2. It generates the requested number of random characters from each category
3. All characters are combined into a list and shuffled randomly
4. The final password is created by joining all characters into a string

## How to Run

### Method 1: Clone and Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JeremyPanggabean/Password-Generator.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Password-Generator
   ```

3. **Run the script:**
   ```bash
   python password_generator.py
   ```
   or
   ```bash
   python3 password_generator.py
   ```

### Method 2: Download and Run

1. **Download the script:**
   - Go to [GitHub Repository](https://github.com/JeremyPanggabean/Password-Generator.git)
   - Click "Code" → "Download ZIP"
   - Extract the ZIP file

2. **Navigate to the extracted folder:**
   ```bash
   cd Password-Generator
   ```

3. **Run the script:**
   ```bash
   python password_generator.py
   ```

### Method 3: Run in IDE/Online Platforms

- **VS Code**: Open the project folder and run the script in the integrated terminal
- **PyCharm**: Open the project and run the script directly
- **Google Colab**: Upload the `.py` file and run it in a code cell
- **Jupyter Notebook**: Create a new notebook and copy the code into cells

### Prerequisites

- Python 3.x installed on your system
- No additional packages required (uses only built-in modules)

### Example Output

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
5
How many symbols would you like?
5
How many numbers would you like?
5
['a', 'j', 'r', 'f', 'M', '%', '#', '#', '!', '&', '7', '3', '8', '3', '2']
['3', '%', '2', '#', 'f', '&', '7', '3', 'r', '!', 'M', '#', 'a', '8', 'j']
Your Password is: 3%2#f&73r!M#a8j
```

## Code Structure

The script includes two approaches:

1. **Sequential Password** (commented out): Generates passwords with letters first, then symbols, then numbers
2. **Random Password** (active): Shuffles all characters randomly for better security

## Requirements

- Python 3.x
- No external dependencies (uses only built-in modules)

## Security Notes

- Passwords are generated using Python's `random` module, which is suitable for most applications
- For cryptographic purposes, consider using `secrets` module instead of `random`
- The generated passwords include a good mix of character types for enhanced security

## Installation

1. Clone or download the script
2. Ensure you have Python 3.x installed
3. Run the script directly: `python password_generator.py`

## Customization

You can easily modify the character sets by editing the `letters`, `numbers`, and `symbols` lists in the code to include or exclude specific characters based on your requirements.

## License

This project is open source and available under the MIT License.
