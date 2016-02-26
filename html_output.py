# coding:utf8
__author__ = 'AlexPC'

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []


    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')

        fout.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')
        fout.write('<html xmlns="http://www.w3.org/1999/xhtml">\n')

        fout.write('<head>\n<meta charset="UTF-8">\n</head>\n')

        fout.write('<body>\n')
        fout.write('<table>\n')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            #.encode('utf-8')
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>\n')

        fout.write('</html>\n')
        fout.write('</body>\n')
        fout.write('</table>\n')

        fout.close()
