from pprint import pprint
import requests
import os
import csv
from pytube import YouTube
import xml.dom.minidom
from lxml import etree



source = YouTube('https://youtu.be/2ejMpDd3PL0')

en_caption = source.captions.get_by_language_code('en')
# en_caption_convert_to_srt =(en_caption.generate_srt_captions())
en_caption_convert_to_xml = (en_caption.xml_captions)
print(en_caption_convert_to_xml)
# pretty_xml_as_string = etree.tostring(en_caption_convert_to_xml, encoding='UTF-8', xml_declaration=True, pretty_print=True)

# pretty_xml_as_string = xml.dom.minidom.parse(en_caption_convert_to_xml).toprettyxml()
#
# text_file = open("test.xml", "w")
# text_file.write(pretty_xml_as_string)
# text_file.close()
