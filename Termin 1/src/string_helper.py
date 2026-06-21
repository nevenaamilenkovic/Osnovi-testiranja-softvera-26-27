def obrni_string(s):
    return s[::-1]

def izbroj_samoglasnike(s):
    samoglasnici='aeiouAEIOU'
    return sum(1 for c in s if c in samoglasnici)
def je_palindrom(s):
    s=s.lower().replace(' ','')
    return s == s[::-1]