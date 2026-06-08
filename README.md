# Warning ⚠

The githubPagesToRepo function does not work currently.

---

# 🚀 pyneeds

A high-utility, all-in-one developer workspace toolkit for Python. `pyneeds` bundles a massive, native suite of math properties, regex validators, string utilities, and terminal managers alongside seamless access to industry-standard external engines for 3D gaming, terminal user interfaces, audio playback, and schema validation.

---

## 🛠️ Features

- **🧮 Advanced Number Theory**: Identify Kaprekar, Armstrong, Smith, Happy, Harshad, Neon, Strong, Perfect, and Automorphic numbers natively.
- **🛡️ Complete Robust Validators**: Out-of-the-box regex checking patterns for Emails, URLs, IPs, Credit Cards, ISBNs, Hex/RGB Color spaces, Datetime signatures, and Base systems.
- **🎮 3D Game Prototyping**: Ready-made pipeline integration using the [Ursina Engine](https://pypi.org).
- **🖥️ Desktop-Grade Terminal UIs**: Build advanced text-driven user layouts directly within the console shell with [Textual](https://pypi.org).
- **🎨 Visuals, Strings & Audio**: Generate massive ASCII fonts with `art`, color text streams via `colorama`, handle string algorithms safely, and fire off async sound bytes using `playsound3`.

---

## 💾 Installation
### Does not work:
Install the entire package workspace along with its external dependencies via a single execution string:

```bash
pip install pyneeds
```

### Does work:
#### Dependencies:
* Python
* colorama
* art
* playsound3
* pydantic
* textual
* ursina
### Install:
```bash
git clone https://github.com/Wolfythethird/pyneeds.git
cd pyneeds/dist
pip install pyneeds-0.1.0-py3-none-any.whl
```

---

## 🎯 Native Utility Reference Guide

Because `pyneeds` maps your files with automated wildcard (`*`) routing, every function listed below can be loaded globally into your operational scripts.

### 🔢 Math, Prime & Sequences

| Function | Description | Example Input | Expected Output |
| :--- | :--- | :--- | :--- |
| `digitalRoot(num)` | Computes the single-digit iterative digital sum sequence. | `555` | `6` |
| `isPrime(num)` | Optimized check to confirm if a number is prime. | `11` | `True` |
| `primeFactors(num)`| Extracts prime factor integers as an ordered collection. | `12` | `[2, 2, 3]` |
| `fibonacci(n)` | Generates first $n$ elements in the Fibonacci sequence. | `5` | `[0, 1, 1, 2, 3]` |
| `factorial(n)` | Recursively calculates the factorial of a target value. | `4` | `24` |
| `gcd(a, b)` | Returns the greatest common divisor between integers. | `12, 18` | `6` |
| `lcm(a, b)` | Returns the least common multiple between integers. | `12, 18` | `36` |

### 🎛️ Special Number Systems
Verify complex number behaviors using dedicated boolean checkers:
```python
from pyneeds import isKaprekar, kaprekarNumbers, isHappy, isSmith, isArmstrong

# Find specialized math constants inside range margins
constants = kaprekarNumbers(1, 100) # Output: [1, 9, 45, 55, 99]

print(isHappy(19))       # Output: True
print(isSmith(493))      # Output: True
print(isArmstrong(153))  # Output: True
```

### 🧵 String Engineering & Text Analysis

| Function | Description | Example Input | Expected Output |
| :--- | :--- | :--- | :--- |
| `listToString(l)` | flattens item array sets into one raw text string. | `['a', 1, 'b']` | `"a1b"` |
| `truncateString(s, n)`| Shortens long lines safely appending trailing ellipsis. | `"Hello World", 5` | `"Hello..."` |
| `isPalindrome(s)` | Returns true if characters read identically backwards. | `"Race car"` | `True` |
| `isPangram(s)` | Detects if target phrase uses every letter in alphabet. | `"The quick brown fox..."` | `True` |
| `isAnagram(s1, s2)` | Verifies character structure matching across texts. | `"listen", "silent"` | `True` |
| `removeVowels(s)` | Strips out vowel markers from string characters. | `"Python"` | `"Pythn"` |
| `slugify(s)` | Cleans up string labels into uniform web URL slugs. | `"My Game Title"` | `"my-game-title"` |

### 🛡️ Regex Validation Arrays
Run rigid verification passes on incoming text buffers with single-function wrappers:
```python
from pyneeds import (
    isValidEmail, isValidIPAddress, isValidCreditCard, 
    isValidISBN, isValidHexColor, isValidDate, isValidTime
)

print(isValidEmail("dev@pyneeds.org"))        # True
print(isValidIPAddress("192.168.1.1"))         # True
print(isValidCreditCard("4000123456789010"))   # True (Passes Luhn Algorithm)
print(isValidISBN("978-3-16-148410-0"))        # True
print(isValidHexColor("#ff5733"))              # True
print(isValidDate("2026-05-18"))               # True
print(isValidTime("14:30:00"))                 # True
```

### 🌐 GitHub & Systems Helpers
Cleanly toggle workspace environments and URL transformations:
```python
from pyneeds import repoToGithubPages, isValidGitHubRepo, clear

# Map repos to active hosting domains
pages_url = repoToGithubPages("https://github.com")
# Returns: "https://github.io"

# Clear all console buffer history across Windows/Unix platforms safely
clear()
```

---

## 🚀 Pre-bundled External Ecosystems

`pyneeds` installs and manages full sub-packages natively. Import top tier assets alongside your native functions:

### 1. Game Windows & Rendering via Ursina
```python
from pyneeds import Ursina, Entity, color

app = Ursina()
cube = Entity(model='cube', color=color.azure, scale=2)
app.run()
```

### 2. Audio Triggers & Terminal Themes
```python
from pyneeds import text2art, Fore, playsound

print(text2art("PYNEEDS READY"))
print(Fore.GREEN + "[SYSTEM SUCCESS] Audio assets mounting.")
playsound("level_up.mp3", block=False)
```

### 3. Schema Models via Pydantic
```python
from pyneeds import BaseModel, Field

class Profile(BaseModel):
    user_id: int
    alias: str = Field(min_length=3, max_length=20)

valid_user = Profile(user_id=101, alias="NinjaCoder")
```

---

## 📝 License

Distributed under the CC BY-SA License. See `LICENSE` for more details.
