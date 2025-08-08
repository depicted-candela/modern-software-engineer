class DataBuffer:
    def __init__(self, data: str):
        self.data: str = data
        self.is_closed: bool = True
        print("Buffer created")
    def open(self):
        self.is_closed = False
        print("Buffer opened")
    def process(self):
        if ("corrupt" in self.data): raise RuntimeError("Data is corrupt")
        print("Data processed")
    def close(self):
        self.is_closed = True
        print("Buffer closed")

def process_data_buffer():
    datas = ["corrupt data", "clean data"]
    for data in datas:
        buffer = DataBuffer(data)
        buffer.open()
        try:
            buffer.process()
        except RuntimeError as re:
            print(f"Runtime Error: {re}")
        finally:
            buffer.close()

if __name__ == "__main__":
    process_data_buffer()