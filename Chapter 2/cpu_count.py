"""
cpu_countを使ってみたかった。
"""

from multiprocessing import cpu_count

if __name__ == "__main__":
    num_count = cpu_count()
    print(num_count)