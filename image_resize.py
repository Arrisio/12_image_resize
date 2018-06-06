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


def is_image_ratio_changed(img_size, img_new_size):
    return img_size[0] / img_new_size[0] != img_size[1] / img_new_size[1]


def set_result_path(orig_path, img_size, result_path=None):
    if result_path:
        result_dir, new_filename = os.path.split(result_path)

        if not new_filename:
            new_filename = os.path.split(orig_path)[1]
        elif not os.path.splitext(new_filename)[1]:
            new_filename = '{}{}'.format(
                new_filename, os.path.splitext(orig_path)[1]
            )
        return os.path.join(result_dir, new_filename)

    else:
        filename, extension = os.path.splitext(orig_path)
        return '{}_{}x{}{}'.format(
            filename, img_size[0], img_size[1], extension
        )


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i', '-img', action='store',
        dest='original_path',
        help='image that will ber resized',
        required=True
    )
    parser.add_argument(
        '-o',
        action='store',
        dest='result_path',
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


def validate_arguments(params):
    if not(params.height or params.width or params.scale):
        raise argparse.ArgumentError(
            'You should speсify scale or height and width params'
        )
    elif (params.height or params.width) and params.scale:
        raise argparse.ArgumentError(
            "Can't use -scale and -height/-with options in the together"
        )
    elif (
        (params.height and params.height <= 0) or
        (params.width and params.width <= 0) or
        (params.scale and params.scale <= 0)
    ):
        raise argparse.ArgumentTypeError("Params must be greater than zero")

    if not os.path.isfile(params.original_path):
        raise argparse.ArgumentTypeError('Invalid path to target image')

    if params.result_path and not (
            os.path.isdir(params.result_path) or
            os.path.isdir(os.path.split(params.result_path)[0])
    ):
        raise argparse.ArgumentTypeError('Invalid output path')


if __name__ == '__main__':
    params = parse_arguments()

    try:
        validate_arguments(params)
    except argparse.ArgumentTypeError as args_err:
        exit(args_err)

    img = Image.open(params.original_path)

    new_size = calc_new_image_size(
        img.size, width=params.width, height=params.height, scale=params.scale
    )

    result_img = img.resize(new_size)

    result_path = set_result_path(
        params.original_path, new_size, params.result_path
    )

    result_img.save(result_path)
    print('\nImage saved to {} with size {}'.format(result_path, new_size))

    if is_image_ratio_changed(img.size, new_size):
        print('\nWarning! Proportions of the original '
              'and resulting images are differen')
