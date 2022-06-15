import hashlib


def md5(value: str) -> str:
    return hashlib.md5(value.encode("utf-8")).hexdigest()


# 生成 md5 字典
def generate_md5_dict(dict_file: str, prefix_size: int, dict_size: int):
    with open(dict_file, "w") as df:
        for i in range(1, dict_size):
            md5_prefix = md5(str(i))[0:prefix_size]
            df.write(md5_prefix + "," + str(i) + "\n")
            if i % 10000 == 0:
                df.flush()


if __name__ == "__main__":
    generate_md5_dict("./data/md5_dict.txt", 6, 100000)
