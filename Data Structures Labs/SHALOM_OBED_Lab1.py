def isValidPassword(new_password, previous_passwords):
    try:
        recent_passwords = previous_passwords[-3:]
        def are_anagrams_v3(s1, s2):
            if len(s1) != len(s2):
                return False
            count1 = [0] * 26
            count2 = [0] * 26
            for c in s1:
                idx = ord(c) - ord('a')
                if idx < 0 or idx > 25:
                    continue
                count1[idx] += 1
            for c in s2:
                idx = ord(c) - ord('a')
                if idx < 0 or idx > 25:
                    continue
                count2[idx] += 1
            for i in range(26):
                if count1[i] != count2[i]:
                    return False
            return True

        for word in recent_passwords:
            if are_anagrams_v3(new_password, word):
                return False
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

prev = ['abc','def', 'ghi', 'jkl', 'mno']
print(isValidPassword('xyz', prev)) # Should print True
print(isValidPassword('bac', prev)) # Should print True
print(isValidPassword('ihg', prev)) # Should print False