# -*- coding: utf-8 -*-

import os
import base64
import subprocess
import time
import click
import pydisp


@click.command(context_settings={'help_option_names':['-h','--help']})
@click.argument('images', nargs=-1, type=click.Path(exists=True), required=True)
@click.option('--title', '-t', type=str, help='Window title')
@click.option('--win', type=str, help='Window ID. By default, a generated unique id. %p will use path as id. %f will use filename.')
@click.option('--width', '-w', type=int, help='Initial indow width.' )
@click.option('--pause', '-p', default=0.2, help='Pause between images in seconds')
@click.option('--port', default=pydisp.PORT, help='Display server port.')
@click.option('--hostname', default=pydisp.HOSTNAME, help='Display server hostname.')
def main(images, title, win, width, pause, port, hostname):
    # TODO tiling option

    if port is not None:
        pydisp.PORT = port

    if hostname is not None:
        pydisp.HOSTNAME = hostname

    for img_fname in images:
        click.echo('loading {}'.format(img_fname))
        base, ext = os.path.splitext(img_fname)
        ext = ext.lower().replace('.', '').replace('jpg', 'jpeg')
        if not pydisp.is_valid_image_mime_type(ext):
            raise click.BadParameter('unrecognized image format: {}'.format(ext))
        with open(img_fname, 'rb') as f:
            encoded = pydisp.b64_encode(f.read(), ext)
        if title == '':
            title = img_fname
        if win=='%f':
            win = img_fname
        elif win=='%p':
            win = os.path.basename(img_fname)
        pydisp.pane('image',
                    win=win,
                    title=title,
                    content={'src': encoded,
                             'width': width,
                            })
        if (len(img_fname) > 1) and (pause > 0.0):
            time.sleep(pause)


if __name__ == '__main__':
    main()
