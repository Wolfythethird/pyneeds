import os

def listToString(l: list) -> str:
    """Converts a list to a string."""
    str1 = ""
    for i in l:
        str1 += str(i)
    return str1

def digitalRoot(num: int) -> int:
    """Returns the digital root of a number."""
    num1 = 0
    num = list(str(num))
    while True:
        if len(num) != 1:
            for n in num:
                num1 += int(n)
                num = list(str(num1))
            num1 = 0
        else:
            break
    return int(str(num).strip("['").strip("']"))

def isKaprekar(num: int) -> bool:
    """Returns True if the number is a Kaprekar number, False otherwise."""
    num1 = num ** 2
    num1 = list(str(num1))
    if len(num1) == 1:
        return int(num1[0]) == num
    else:
        right = num1[-len(str(num)):]
        left = num1[:-len(str(num))]
        if left == []:
            left = "0"
        return int(listToString(left)) + int(listToString(right)) == num

def kaprekarNumbers(start: int, end: int) -> list:
    """Returns a list of Kaprekar numbers in the given range."""
    kaprekar = []
    for i in range(start, end + 1):
        if isKaprekar(i):
            kaprekar.append(i)
    return kaprekar

def truncateString(s: str, n: int) -> str:
    """Truncates a string to a given length."""
    if len(s) > n:
        return s[:n] + "..."
    else:
        return s

def isPalindrome(s: str) -> bool:
    """Returns True if the string is a palindrome, False otherwise."""
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def isPangram(s: str) -> bool:
    """Returns True if the string is a pangram, False otherwise."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.replace(" ", "").lower()
    for letter in alphabet:
        if letter not in s:
            return False
    return True

def isAnagram(s1: str, s2: str) -> bool:
    """Returns True if the two strings are anagrams, False otherwise."""
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

def isPrime(num: int) -> bool:
    """Returns True if the number is prime, False otherwise."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeFactors(num: int) -> list:
    """Returns a list of prime factors of a number."""
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return factors

def fibonacci(n: int) -> list:
    """Returns a list of the first n Fibonacci numbers."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

def factorial(n: int) -> int:
    """Returns the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def gcd(a: int, b: int) -> int:
    """Returns the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Returns the least common multiple of two numbers."""
    return (a * b) // gcd(a, b)

def isPerfect(num: int) -> bool:
    """Returns True if the number is perfect, False otherwise."""
    if num < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num

def isArmstrong(num: int) -> bool:
    """Returns True if the number is an Armstrong number, False otherwise."""
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

def isHappy(num: int) -> bool:
    """Returns True if the number is a happy number, False otherwise."""
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def isAutomorphic(num: int) -> bool:
    """Returns True if the number is an automorphic number, False otherwise."""
    num_squared = num ** 2
    return str(num_squared).endswith(str(num))

def isHarshad(num: int) -> bool:
    """Returns True if the number is a Harshad number, False otherwise."""
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

def isSmith(num: int) -> bool:
    """Returns True if the number is a Smith number, False otherwise."""
    if isPrime(num):
        return False
    digit_sum = sum(int(digit) for digit in str(num))
    prime_factor_sum = sum(sum(int(digit) for digit in str(factor)) for factor in primeFactors(num))
    return digit_sum == prime_factor_sum

def isStrong(num: int) -> bool:
    """Returns True if the number is a strong number, False otherwise."""
    digit_factorial_sum = sum(factorial(int(digit)) for digit in str(num))
    return digit_factorial_sum == num

def isNeon(num: int) -> bool:
    """Returns True if the number is a neon number, False otherwise."""
    num_squared = num ** 2
    digit_sum = sum(int(digit) for digit in str(num_squared))
    return digit_sum == num

def isAutomorphic(num: int) -> bool:
    """Returns True if the number is an automorphic number, False otherwise."""
    num_squared = num ** 2
    return str(num_squared).endswith(str(num))

def reverseString(s: str) -> str:
    """Returns the reverse of a string."""
    return s[::-1]

def removeVowels(s: str) -> str:
    """Returns the string with all vowels removed."""
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

def countVowels(s: str) -> int:
    """Returns the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def countConsonants(s: str) -> int:
    """Returns the number of consonants in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def slugify(s: str) -> str:
    """Converts a string to a slug."""
    return s.lower().replace(" ", "-")

def isValidEmail(email: str) -> bool:
    """Returns True if the email is valid, False otherwise."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def isValidURL(url: str) -> bool:
    """Returns True if the URL is valid, False otherwise."""
    import re
    pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(pattern, url) is not None

def isValidPhoneNumber(phone: str) -> bool:
    """Returns True if the phone number is valid, False otherwise."""
    import re
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None

def isValidIPAddress(ip: str) -> bool:
    """Returns True if the IP address is valid, False otherwise."""
    import re
    pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def isValidCreditCard(card: str) -> bool:
    """Returns True if the credit card number is valid, False otherwise."""
    import re
    pattern = r'^\d{13,19}$'
    if re.match(pattern, card):
        total = 0
        reverse_digits = card[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0
    return False

def isValidISBN(isbn: str) -> bool:
    """Returns True if the ISBN number is valid, False otherwise."""
    import re
    isbn = isbn.replace('-', '').replace(' ', '')
    if len(isbn) == 10:
        if not re.match(r'^\d{9}[\dX]$', isbn):
            return False
        total = sum((i + 1) * (10 if x == 'X' else int(x)) for i, x in enumerate(isbn))
        return total % 11 == 0
    elif len(isbn) == 13:
        if not re.match(r'^\d{13}$', isbn):
            return False
        total = sum((int(x) * (1 if i % 2 == 0 else 3)) for i, x in enumerate(isbn))
        return total % 10 == 0
    return False

def isValidPassword(password: str) -> bool:
    """Returns True if the password is valid, False otherwise."""
    import re
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password) is not None

def isValidUsername(username: str) -> bool:
    """Returns True if the username is valid, False otherwise."""
    import re
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return re.match(pattern, username) is not None

def isValidHexColor(color: str) -> bool:
    """Returns True if the hex color code is valid, False otherwise."""
    import re
    pattern = r'^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$'
    return re.match(pattern, color) is not None

def isValidRGBColor(color: str) -> bool:
    """Returns True if the RGB color code is valid, False otherwise."""
    import re
    pattern = r'^rgb\(\s*(\d{1,3}\s*,\s*){2}\d{1,3}\s*\)$'
    if re.match(pattern, color):
        numbers = [int(n) for n in re.findall(r'\d+', color)]
        return all(0 <= n <= 255 for n in numbers)
    return False

def isValidHexadecimal(num: str) -> bool:
    """Returns True if the hexadecimal number is valid, False otherwise."""
    import re
    pattern = r'^[0-9a-fA-F]+$'
    return re.match(pattern, num) is not None

def isValidBinary(num: str) -> bool:
    """Returns True if the binary number is valid, False otherwise."""
    import re
    pattern = r'^[01]+$'
    return re.match(pattern, num) is not None

def isValidOctal(num: str) -> bool:
    """Returns True if the octal number is valid, False otherwise."""
    import re
    pattern = r'^[0-7]+$'
    return re.match(pattern, num) is not None

def isValidDecimal(num: str) -> bool:
    """Returns True if the decimal number is valid, False otherwise."""
    import re
    pattern = r'^\d+$'
    return re.match(pattern, num) is not None

def isValidFloat(num: str) -> bool:
    """Returns True if the float number is valid, False otherwise."""
    import re
    pattern = r'^[+-]?\d+(\.\d+)?$'
    return re.match(pattern, num) is not None

def isValidScientific(num: str) -> bool:
    """Returns True if the scientific notation number is valid, False otherwise."""
    import re
    pattern = r'^[+-]?\d+(\.\d+)?[eE][+-]?\d+$'
    return re.match(pattern, num) is not None

def isValidDate(date: str) -> bool:
    """Returns True if the date is valid, False otherwise."""
    import re
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date):
        year, month, day = map(int, date.split('-'))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    return False

def isValidTime(time: str) -> bool:
    """Returns True if the time is valid, False otherwise."""
    import re
    pattern = r'^\d{2}:\d{2}:\d{2}$'
    if re.match(pattern, time):
        hours, minutes, seconds = map(int, time.split(':'))
        if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
            return True
    return False

def githubPagesToRepo(pagesurl: str) ->  None:
    """Converts a GitHub Pages URL to a repository URL."""
    pass

def repoToGithubPages(repourl: str) ->  None:
    """Converts a GitHub repository URL to a GitHub Pages URL."""
    if repourl.startswith("https://github.com/"):
        return repourl.replace("https://github.com/", "https://").replace("/", ".github.io/")
    return None

def isValidGitHubRepo(url: str) -> bool:
    """Returns True if the URL is a valid GitHub repository URL, False otherwise."""
    import re
    pattern = r'^https://github\.com/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+$'
    return re.match(pattern, url) is not None

def isValidGitHubPages(url: str) -> bool:
    """Returns True if the URL is a valid GitHub Pages URL, False otherwise."""
    import re
    pattern = r'^https://[a-zA-Z0-9_-]+\.github\.io/[a-zA-Z0-9_-]+$'
    return re.match(pattern, url) is not None

def clear() -> None:
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')