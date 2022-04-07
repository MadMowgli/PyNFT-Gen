import os
import time
import tkinter
from os import listdir
from os.path import isfile, join

from PIL import Image

# ----------------------------------------------------------------------------------------- constants
debug = False


# ----------------------------------------------------------------------------------------- functions
def generate(layer_directories, output_directory, collection_name):
    """
    Takes the file paths from the Entry Widgets and layers each vector on top of each other.
    :param layer_directories: 
    :param output_directory: 
    :param collection_name: 
    :return: 
    """

    # Grab strings from tkinter variables
    collection_name = collection_name.get()
    layers = None
    if debug:
        layers = layers = [BASE_LAYER, LAYER_1, LAYER_2, LAYER_3, LAYER_4]
        output_directory = OUTPUT_DIR + '/' + collection_name
    else:
        layers = [x.get() for x in layer_directories if x.get() != '']
        layers.pop()  # Clear output directory from layers
        output_directory = output_directory.get() + '/' + collection_name

    # Create output dir for collection
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    # debug
    print('Layers: \t\t\t' + str(layers))
    print('Output dir: \t\t\'' + output_directory + '\'')
    print('Collection name: \t\'' + collection_name + '\'')

    # Check if base layer, output dir and collection name are set
    input_is_valid = validate_inputs(layers[0], output_directory, collection_name)

    # If input is valid, go ahead
    if input_is_valid:

        # Get path for each image saved in the directories
        layer_paths = grab_image_paths(layers)
        base_layer_paths = layer_paths[0] if len(layer_paths) >= 1 else None
        first_layer_paths = layer_paths[1] if len(layer_paths) >= 2 else None
        second_layer_paths = layer_paths[2] if len(layer_paths) >= 3 else None
        third_layer_paths = layer_paths[3] if len(layer_paths) >= 4 else None
        fourth_layer_paths = layer_paths[4] if len(layer_paths) >= 5 else None
        fifth_layer_paths = layer_paths[5] if len(layer_paths) >= 6 else None

        last_merge = None
        first_merge = merge(base_layer_paths,
                            first_layer_paths) if base_layer_paths is not None and first_layer_paths is not None else None
        last_merge = first_merge
        print('First merge done.')

        second_merge = merge(first_merge, second_layer_paths) if first_merge is not None and second_layer_paths is not None else None
        if second_merge is not None:
            for img in first_merge:
                img.close()
            first_merge.clear()
            first_merge = None
            last_merge = second_merge
            print('Second merge done.')

        third_merge = merge(second_merge, third_layer_paths) if second_merge is not None and third_layer_paths is not None else None
        if third_merge is not None:
            for img in second_merge:
                img.close()
            second_merge.clear()
            second_merge = None
            last_merge = third_merge
            print('Third merge done.')

        fourth_merge = merge(third_merge, fourth_layer_paths) if third_merge is not None and fourth_layer_paths is not None else None
        if fourth_merge is not None:
            for img in third_merge:
                img.close()
            third_merge.clear()
            third_merge = None
            last_merge = fourth_merge
            print('Fourth merge done.')

        fifth_merge = merge(fourth_merge, fifth_layer_paths) if fourth_merge is not None and fifth_layer_paths is not None else None
        if fifth_merge is not None:
            for img in fourth_merge:
                img.close()
            fourth_merge.clear()
            fourth_merge = None
            last_merge = fifth_merge
            print('Fifth merge done.')

        print('Saving last merge...')
        save(last_merge, output_directory)
        last_merge.clear()
        last_merge = None


def validate_inputs(base_layer_path, output_dir_path, collection_name):
    if base_layer_path == '':
        tkinter.messagebox.showerror(title='Invalid Input', message='Base layer path must not be empty.')
        return False
    if output_dir_path == '':
        tkinter.messagebox.showerror(title='Invalid Input', message='Output directory path must not be empty.')
        return False
    if collection_name == '':
        tkinter.messagebox.showerror(title='Invalid Input', message='Collection name must not be empty.')
        return False
    return True


def grab_image_paths(layers):
    paths = []
    for layer in layers:
        try:
            image_paths = [layer + '/' + str(f) for f in listdir(layer) if isfile(join(layer, f))]
            paths.append(image_paths)
        except BaseException as e:
            print('Exception: ' + str(type(e)))
    return paths


def merge(layer_1, layer_2):
    merged = []
    for path in layer_1:
        image_one = None
        try:
            image_one = Image.open(path)
        except:
            image_one = path

        for path_2 in layer_2:
            image_one_copy = image_one.copy()
            image_two = Image.open(path_2)
            image_one_copy.paste(image_two, (0, 0), image_two)
            merged.append(image_one_copy)
            image_two.close()
    return merged


def save(merged_images, output_directory):
    counter = 0
    for img in merged_images:
        img = img.convert('RGB')
        img.save(f'{output_directory}/{counter}.jpg')
        counter += 1
