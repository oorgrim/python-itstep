import threading

def process_file(input_file):
    output_file = "mod_" + input_file
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            modified_line = line.replace("python", "c#")
            outfile.write(modified_line)

def main():
    input_files = ["file01.txt", "file02.txt", "file03.txt"]

    threads = []
    for input_file in input_files:
        thread = threading.Thread(target=process_file, args=(input_file,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()