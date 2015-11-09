def piglatintranslate(s):
    s = s.split(); ns = ""
    for w in s:
        i = 0; sf = "yay";p = ""; a = False
        if not w.isalpha(): ns += w + " "; a = True
        if not w[len(w) - 1].isalpha(): p = w[len(w) - 1]; w = w[:len(w) - 1]
        for c in w:
            if c in "aeiouAEIOU":
                if w[0].isupper(): ns += w[i].upper() + w[i + 1:] + w[:i].lower() + sf + p + " "; a = True; break
                else: ns += w[i:] + w[:i] + sf + p + " "; a = True; break
            else: sf = "ay"
            i += 1
        if not a: ns += w + sf + p + " "
    return ns
