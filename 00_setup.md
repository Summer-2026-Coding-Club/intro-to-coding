# Setup: Installing Python and Running Code

There are two kinds of Python files you'll see in this repo, and it's helpful if you know how to use both of them!

## 1. Install Python

1. Go to [python.org/downloads](https://www.python.org/downloads/) and install the latest version for your OS.
2. Check it worked — open a terminal (Mac: Terminal app, Windows: Command Prompt or PowerShell) and run:
   ```
   python3 --version
   ```
   (On Windows this might just be `python --version`.) You should see something like `Python 3.12.0`.

## 2. Running a `.py` script

A `.py` file is a plain text file full of Python code. You run the whole file at once from the terminal.

Try it with [`hello_world.py`](hello_world.py) in this folder:

```
cd intro-to-coding
python3 hello_world.py
```

You should see it print something out.

**When to use a `.py` file:** real programs, scripts you want to run repeatedly, anything bigger than quick experimentation.

## 3. Running a Jupyter notebook (`.ipynb`)

A notebook is a mix of text and code, split into **cells**. You run cells one at a time and immediately see the output below each one (this is great for learning, since you can experiment piece by piece).

Easiest way to get started, no install required: upload `walkthrough.ipynb` to [Google Colab](https://colab.research.google.com/) (File --> Upload notebook).

To run it locally instead:
```
pip install notebook
jupyter notebook
```
This opens a browser tab: navigate to `walkthrough.ipynb` and open it.

**Using a notebook:**
- Click a cell, press `Shift + Enter` to run it and move to the next one.
- Code cells run Python. Markdown cells (like this explanation) are just text.
- Cells share state. A variable defined in one cell is available in later cells, as long as you've run them in order.
- Use the menu to "Restart kernel and run all" to start fresh from the top.

**When to use a notebook:** learning, exploring data, anything where you want to see output after every small step.

## Next step

Once you can run `hello_world.py` and open `walkthrough.ipynb`, head to the walkthrough and start from the top.
