# coding=utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<meta charset = \"utf-8\" > <title > 百度百科 </title >")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            # fout.write("<tr>")
            if data is None:
                continue
            fout.write("<h3>%s</h3>" % data['title'].encode('utf-8'))
            # print data['url']
            fout.write("<a href=\"")
            fout.write(data['url'])
            fout.write("\">点击连接</a>")
            fout.write("<p>%s</p></br> </hr></br>" % data['summary'].encode('utf-8'))
            # fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
