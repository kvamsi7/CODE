def dnaComplement(s):
    map_ = {'A':'T',
            'C':"G",
            'T':'A',
            'G':'C'}
    s = s.upper();
    s = s[::-1]
    return ''.join([map_.get(let) for let in s])

if __name__ == "__main__":
    s = input()
    print(dnaComplement(s))