import numpy as np

def fix_gt():
    with open('corridor_gt_raw.csv', 'r') as f:
        lines = f.readlines()
    with open('gt_final.tum', 'w') as f:
        for line in lines:
            if line.startswith('#'): continue
            p = line.replace(',', ' ').split()
            if len(p) < 8: continue
            # 将纳秒转为秒，保留 9 位小数
            ts = float(p[0]) / 1e9
            f.write(f"{ts:.9f} {p[1]} {p[2]} {p[3]} {p[5]} {p[6]} {p[7]} {p[4]}\n")

def fix_res():
    with open('f_dataset-corridor1_512_stereoi.txt', 'r') as f:
        lines = f.readlines()
    with open('res_final.tum', 'w') as f:
        for line in lines:
            p = line.split()
            if len(p) < 8: continue
            # 将纳秒转为秒，保留 9 位小数
            ts = float(p[0]) / 1e9
            f.write(f"{ts:.9f} {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]} {p[7]}\n")

if __name__ == "__main__":
    fix_gt()
    fix_res()
    print("转换完成：时间戳已转为秒（TUM标准格式）")
