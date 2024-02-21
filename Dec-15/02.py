try:
    with open("02.html", encoding="utf8") as fd:
        html_content = fd.read()
except FileNotFoundError:
    print("Файл не найден!")
    exit()

def extract_text_between_tags(tag_start, tag_end, html):
    start_index, end_index = html.find(tag_start), html.find(tag_end, html.find(tag_start))
    return html[start_index + len(tag_start):end_index].strip() if start_index != -1 and end_index != -1 else ""

title = extract_text_between_tags("<title>", "</title>", html_content)

headings = []
for i in range(1, 6):
    heading = extract_text_between_tags(f"<h{i}>", f"</h{i}>", html_content)
    headings.append(heading)

print(title)

for heading in headings:
    print(heading)

try:
    with open("output02.txt", "w", encoding="utf8") as output_file:
        output_file.write(f"{title}\n")
        for heading in headings:
            output_file.write(f"{heading}\n")
except PermissionError:
    print("Здесь нельзя создавать файл")
