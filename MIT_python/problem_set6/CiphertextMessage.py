class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
         
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max_real_words = 0
        best = 0
        save2 =''
        for shift in range(27):
            real_words = 0
            
            save = self.apply_shift(shift)
            words = save.split(string.punctuation + ' ')
            
            for word in words:
                if is_word(wordlist, word):
                    real_words += 1
            if real_words > max_real_words:
                max_real_words = real_words
                best =shift
                save2 = save
        
        return (best, self.message_text)
                    