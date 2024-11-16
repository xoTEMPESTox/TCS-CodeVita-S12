def can_fit_line(max_len, words):
    total_len = 0
    for index, wrd in enumerate(words):
        total_len += len(wrd) 
        if index > 0:  
            total_len += 1
    return total_len <= max_len

def place_words(words, max_line, max_len, index, line_cfg, words_plcd):

    if index == len(words):
        return words_plcd

    best_cnt = words_plcd


    for l in range(len(line_cfg)):

        if can_fit_line(max_len, line_cfg[l] + [words[index]]):
            line_cfg[l].append(words[index])  
            best_cnt = max(best_cnt, place_words(words, max_line, max_len, index + 1, line_cfg, words_plcd + 1))
            line_cfg[l].pop()  


    if len(line_cfg) < max_line:
        line_cfg.append([words[index]])  
        best_cnt = max(best_cnt, place_words(words, max_line, max_len, index + 1, line_cfg, words_plcd + 1))
        line_cfg.pop()  

    return best_cnt


n = int(input()) 
words = [input() for _ in range(n)]  

max_line, max_len = map(int, input().split())  


words = [w for w in words if len(w) <= max_len]


words.sort(key=len, reverse=True)


max_words = place_words(words, max_line, max_len, 0, [], 0)


print(max_words)
