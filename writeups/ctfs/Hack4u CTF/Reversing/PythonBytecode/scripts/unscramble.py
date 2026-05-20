#!/usr/bin/python3

def unscramble(vals):
    out = []
    for i, v in enumerate(vals):
        out.append(chr(v ^ (i + 19)))
    return ''.join(out)


if __name__ == '__main__':
    
    expected = [99, 109, 97, 126, 39, 118, 70, 120, 98, 104, 46, 125, 47, 68, 18, 125, 81, 23, 83]

    key = unscramble(expected)
    print(key)
