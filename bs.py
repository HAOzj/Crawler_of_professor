"""
@date: Sep 14th, 2019

@author: woshihaozhaojun@sina.com
"""
import re
import requests
import conf_loader
from bs4 import BeautifulSoup


def get_url_list(url, prefix, href_pattern):
    """获取所有教授信息的urls

    Args:
        url(str) :- 有教授清单的网页
        prefix(str) :- 教授信息网页的前缀
        href_pattern(str) :- 教授信息网页的pattern
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    prof_block = soup.find_all(href=re.compile(href_pattern))
    urls = []
    for li in prof_block:
        url = prefix + li.get("href")
        urls.append(url)
    return urls


def get_detail_of_prof(url, classes, classes_li, classes_next):
    """根据教授信息的url来获取教授的信息,存入字典

    Args:
        url(str) :- 网页地址
        classes(iterables) :- 只需要提取正文的类
        classes_li(iterables) :- 需要提取列举型内容的类
        classes_next(dict) :- 根据类名来提取下一个p的内容
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    info = dict()
    for class_ in classes:
        detail = soup.find(class_=class_)
        if detail:
            info[class_] = detail.get_text()
        else:
            info[class_] = ""
    for k, v in classes_next.items():
        detail = soup.find("p", k)
        if detail:
            detail = detail.find_next_sibling("p")
            info[v] = detail.get_text()
        else:
            info[v] = ""
    for class_ in classes_li:
        detail = soup.find(class_=class_)
        if detail:
            info[class_] = [li.get_text() for li in detail.find_all("li")]
        else:
            info[class_] = ""
    return info


def main():
    urls = get_url_list(
        url=conf_loader.url,
        prefix=conf_loader.prefix,
        href_pattern=conf_loader.href_pattern
    )

    profs = []
    for url in urls:
        prof = get_detail_of_prof(
            url=url,
            classes=conf_loader.classes,
            classes_li=conf_loader.classes_li,
            classes_next=conf_loader.classes_next
        )
        profs.append(prof)
    return profs


if __name__ == "__main__":
    main()
