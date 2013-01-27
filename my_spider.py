#!/home/qishui/env/42qu/bin/python
"""
抓取新浪微话题所有标题和简介,通过url抓取从http://huati.weibo.com/10001
到 http://huati.weibo.com/27500 的页面,有话题的就截取题目和简介,没有话
题的就跳过.
"""
import requests
import sys
from extract import extract, extract_all

TITLE_START = '<a href="javascript:;" node-type="topic-title">'
TITLE_END = '</a>'
TEXT_START = '<div class="text">'
TEXT_END = '</div>'
URL = "http://huati.weibo.com/"
SPLIT = "=" * 10


def run():
    """抓取页面处理内容"""
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    file_name = sys.argv[3]
    count = 0
    global outfile
    outfile = open(file_name, "w")

    for url_num in range(start, end + 1):
        url = URL + str(url_num)
        html = requests.get(url)
        content = html.content
        title_list = extract_all(TITLE_START, TITLE_END, content)
        if len(title_list) > 0:
            count += 1
            title = title_list[0]
            text_space = extract_all(TEXT_START, TEXT_END, content)[0]
            text = "".join(text_space.split())
            print ("get ok %s all:%d \n") % (url, count)
            write_file(url_num, title, text)
        else:
            print 'nothig here at %s\n' % url

    outfile.close()


def write_file(url_num, title, text):
    """写入文件"""
    outfile.write((SPLIT + "%d \n%s \n%s\n") % (url_num, title, text))

if __name__ == '__main__':
    run()
