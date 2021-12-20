import os
import time

from PIL import Image


def generate(layer_directories, output_directory, collection_name):
    '''
    Takes the file paths from the Entry Widgets and layers each vector on top of each other.
    :return:
    '''

    # Get files from layers
    base_layer_file_paths = [str(file.path).replace('\\', '/') for file in os.scandir(layer_directories[0].get())]
    first_layer_file_paths = [str(file.path).replace('\\', '/') for file in os.scandir(layer_directories[1].get())]
    second_layer_file_paths = [str(file.path).replace('\\', '/') for file in os.scandir(layer_directories[2].get())]
    third_layer_file_paths = [str(file.path).replace('\\', '/') for file in os.scandir(layer_directories[3].get())]
    fourth_layer_file_paths = [str(file.path).replace('\\', '/') for file in os.scandir(layer_directories[4].get())]
    fifth_layer_file_paths = [str(file.path).replace('\\', '/') for file in os.scandir(layer_directories[5].get())]
    sixth_layer_file_paths = [str(file.path).replace('\\', '/') for file in os.scandir(layer_directories[6].get())]
    output_directory = str(output_directory.get()).replace('\\', '/')
    collection_name = str(collection_name.get())

    # Loop through layers and stack them on each other
    counter = 0
    for base_layer in base_layer_file_paths:
        base_layer_img = Image.open(base_layer)
        for first_layer in first_layer_file_paths:
            first_layer_img = Image.open(first_layer)
            for second_layer in second_layer_file_paths:
                second_layer_img = Image.open(second_layer)
                for third_layer in third_layer_file_paths:
                    third_layer_img = Image.open(third_layer)
                    for fourth_layer in fourth_layer_file_paths:
                        fourth_layer_img = Image.open(fourth_layer)
                        for fifth_layer in fifth_layer_file_paths:
                            fifth_layer_img = Image.open(fifth_layer)
                            for sixth_layer in sixth_layer_file_paths:
                                sixth_layer_img = Image.open(sixth_layer)

                            # Stack layers
                            base_layer_img.paste(first_layer_img, (0, 0), first_layer_img)
                            print('First layer pasted')
                            base_layer_img.paste(second_layer_img, (0, 0), second_layer_img)
                            print('Second layer pasted')
                            base_layer_img.paste(third_layer_img, (0, 0), third_layer_img)
                            print('Third layer pasted')
                            base_layer_img.paste(fourth_layer_img, (0, 0), fourth_layer_img)
                            print('Fourth layer pasted')
                            base_layer_img.paste(fifth_layer_img, (0, 0), fifth_layer_img)
                            print('Fifth layer pasted')
                            base_layer_img.paste(sixth_layer_img, (0, 0), sixth_layer_img)

                            # Convert & save
                            base_layer_img = base_layer_img.convert('RGB')
                            base_layer_img.save(f'{output_directory}/{collection_name}_{counter}.jpg')
                            print(f'Saved to: {output_directory}/{collection_name}_{counter}.jpg')
                            counter += 1
