from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" class="special">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special super-special">This list item is special.</li>
        <li class="special">This list item is also special.</li>
        <li>This list item is not special.</li>
    </ol>
    <div data-example="yes">bye</div>
</body>
</html>
''' 

soup = BeautifulSoup(html, "html.parser")
# soup.find("h3").attrs['data']
attr = soup.find("h3")["data-example"] # yes
i_d = soup.find("div")["id"] # first
print(i_d)
# for el in soup.select(".special"):
    # print(el.get_text()) # if element doesn't have innerText, returns empty
    # print(el.name)
    # print(el.attrs)
    # print(el.attrs['class'])