class Notebook:
    def __init__(self, brand, size, page_count, paper_type):
        self.brand = brand
        self.size = size
        self.page_count = page_count
        self.paper_type = paper_type
        self.current_page = 1

    def write_on_page(self, content):
        print(f"Wriet on page {self.current_page}: {content}")
        self.current_page += 1

    def flip_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print(f"Flipped to page {self.current_page}")
        else:
            print("You' ve reached the last page")

    def get_page_count(self):
        return self.page_count

notebook1 = Notebook("BestNotebooks", "A4", 96, "Lined")
notebook2 = Notebook("KakoitoBrand", "A5", 48, "Dotted")

notebook1.write_on_page("Notes")
notebook2.flip_page()
notebook1.write_on_page("Ideas for the project...")

print(f"Total pages in notebook: {notebook1.get_page_count()}")