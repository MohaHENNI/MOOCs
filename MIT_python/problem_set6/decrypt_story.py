def decrypt_story():
    cipher = CiphertextMessage (get_story_string())
    tup = cipher.decrypt_message()
    return tup