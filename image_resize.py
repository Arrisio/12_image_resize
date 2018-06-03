from PIL import Image
import os
import argparse


def calc_new_image_size(orig_size, width=None, height=None, scale=None):
    orig_width, orig_height = orig_size
    if width and height:
        return width, height
    elif scale:
        return int(orig_width * scale), int(orig_height * scale)
    elif width:
        return width, int((width * orig_height) // orig_width)
    elif height:
        return int((height * orig_width) // orig_height), height
    else:
        return orig_size


def set_new_img_name(orig_name, img_size, new_name=None ):
    if new_name:
        return new_name
    else:
        filename, extension = os.path.splitext(orig_name)
        return '{}_{}x{}{}'.format(
            filename, img_size[0], img_size[1], extension
        )


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i', '-img',
        action='store',
        dest='path_to_original',
        help='image that will ber resized',
        required=True
    )
    parser.add_argument(
        '-o',
        action='store',
        dest='path_to_result',
        help='filepath to save image'
    )

    parser_size_group = parser.add_argument_group(title='Define new size')
    parser_size_group.add_argument(
        '-width',
        action='store',
        type=int
    )
    parser_size_group.add_argument(
        '-height',
        action='store',
        type=int
    )

    parser_scale_group = parser.add_argument_group(title='Scale image')
    parser_scale_group.add_argument(
        '-scale',
        action='store',
        type=float
    )

    return parser.parse_args()


if __name__ == '__main__':
    params = parse_arguments()

    try:
        img = Image.open(params.path_to_original)
        new_size = calc_new_image_size(
            img.size,
            width=params.width,
            height=params.height,
            scale=params.scale
        )

        result_img = img.resize(new_size)

        path_to_result = set_new_img_name(
            params.path_to_original, new_size, params.path_to_result
        )

        result_img.save(path_to_result)
    except (ValueError, OSError) as image_error:
        exit(image_error)

    print('Image saved to {} with size {}'.format(path_to_result, new_size))
