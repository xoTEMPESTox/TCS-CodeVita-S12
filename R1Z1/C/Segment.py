seg_map = {
    '0': [" _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"],
    '4': ["   ", "|_|", "  |"],
    '5': [" _ ", "|_ ", " _|"],
    '6': [" _ ", "|_ ", "|_|"],
    '7': [" _ ", "  |", "  |"],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _|"],
    '+': ["   ", "|_ ", "|  "],
    '-': ["   ", " _ ", "  "],
    '*': ["   ", "|_|", "| |"],
    '/': [" _ ", " _ ", " _ "],
    '=': ["   ", " _ ", " _ "]
}

def count_dif(a, b):
    dif_cnt = 0
    for i in range(3):
        for j in range(3):
            if a[i][j] != b[i][j]:
                dif_cnt += 1
    return dif_cnt

def get_chr_frm_grid(grid):
    for chr, corr_grid in seg_map.items():
        if count_dif(grid, corr_grid) == 0:
            return chr
    return None

def find_falty_seg(N, lines):
    eqn_chr = []
    for i in range(N):
        char_grid = [lines[0][i*3:(i+1)*3], lines[1][i*3:(i+1)*3], lines[2][i*3:(i+1)*3]]
        eqn_chr.append(char_grid)
    
    fulty_pos = -1
    for i in range(N):
        original_char = get_chr_frm_grid(eqn_chr[i])
        if original_char is None:
            fulty_pos = i + 1
            break
    
    return fulty_pos

N = int(input())
lines = [input() for _ in range(3)]

print(find_falty_seg(N, lines))
