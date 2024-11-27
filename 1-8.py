#1-8
def cipher(text):

    transformed = [chr(219 - ord(char)) if 'a' <= char <= 'z' else char for char in text]
    return ''.join(transformed)

# メッセージの暗号化
message = "Autumn nights call for a book marathon! 📚 Starting my challenge with 101 books this season. #ReadingSpree"
encrypted_message = cipher(message)
decrypted_message = cipher(encrypted_message)

# 結果の出力
(encrypted_message, decrypted_message)
