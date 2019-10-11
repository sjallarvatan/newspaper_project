#!/usr/bin/python

from google.cloud import vision
import io
import sys 
import os
import pandas as pd 

#takes an image argument and sends to google's image to text api. Will accept a list of images and print the file name and text content in a file.

text_image = sys.argv[1]
print(text_image)

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            #print('\nBlock confidence: {}\n'.format(block.confidence))
            print(' @@ ', end="", flush=True, file=texts)

            for paragraph in block.paragraphs:
                #print('Paragraph confidence: {}'.format(
                #    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    
                    print ('{}'.format(
                        word_text), end=" ", flush=True, file=texts),

                    #print('Word text: {} (confidence: {})'.format(
                    #    word_text, word.confidence))
    print("\n",end="", flush=True, file=texts)

                    #for symbol in word.symbols:
                    #    print('\tSymbol: {} (confidence: {})'.format(
                    #        symbol.text, symbol.confidence))

#replaces file extention 
image_name = os.path.basename(text_image)

texts = open("image_error_text_list.txt", "a+")

print(image_name + "|||", file=texts, flush=True,end="")

detect_text(text_image)

texts.close()


