import hashlib


def main():
    input_file = "in.txt"
    output_file = "out.txt"

    completed_hash = set()
    output_file = open(output_file, "w")

    for line in open(input_file, "r"):
        hash_value = hashlib.md5(line.strip().encode('utf-8')).hexdigest()

        if hash_value not in completed_hash:
            output_file.write(line)
            completed_hash.add(hash_value)

    output_file.close()


if __name__ == "__main__":
    main()
