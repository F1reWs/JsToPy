class console:
    @staticmethod
    def log(*args):
        text = " ".join(str(arg) for arg in args)
        print(text)

    @staticmethod
    def error(*args):
        text = " ".join(str(arg) for arg in args)
        print("[ERROR] " + text)

    @staticmethod
    def warn(*args):
        text = " ".join(str(arg) for arg in args)
        print("[WARNING] " + text)

    @staticmethod
    def info(*args):
        text = " ".join(str(arg) for arg in args)
        print("[INFO] " + text)

    @staticmethod
    def debug(*args):
        text = " ".join(str(arg) for arg in args)
        print("[DEBUG] " + text)

    @staticmethod
    def clear():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def table(data):
        headers = data[0].keys()
        rows = [list(d.values()) for d in data]
        col_widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
        header_row = '|'.join(headers[i].ljust(col_widths[i]) for i in range(len(headers)))
        sep_row = '-' * len(header_row)
        print(header_row)
        print(sep_row)
        for row in rows:
            print('|'.join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

    @staticmethod
    def time():
        import time
        return time.time()

    @staticmethod
    def timeEnd(start_time):
        import time
        elapsed_time = time.time() - start_time
        print("Time elapsed:", elapsed_time, "seconds")