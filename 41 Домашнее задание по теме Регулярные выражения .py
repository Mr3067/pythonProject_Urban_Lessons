"""
https://habr.com/ru/articles/349860/
https://habr.com/ru/companies/skillfactory/articles/677402/


"""
import re


def extract_image_links(html_text):
    match = re.findall(r'<img src=\'(.*?)\'>',
                       html_text)
    return match if match != [''] else []


sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"

image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")
