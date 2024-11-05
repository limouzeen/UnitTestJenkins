# my_function.py
def is_palindrome(word):
    word = word.lower().replace(" ", "")  # แปลงเป็นตัวพิมพ์เล็กและลบช่องว่าง
    return word == word[::-1]
