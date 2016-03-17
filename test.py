class AreAnagrams:


    @staticmethod
    def are_anagrams(a, b):
        s1 = ''.join(sorted(a))
        s2 = ''.join(sorted(b))
        if s1 == s2:
            return True
        else:
            return False



#To see the output, uncomment the line belows:
print(AreAnagrams.are_anagrams('momdad', 'dadmom'))