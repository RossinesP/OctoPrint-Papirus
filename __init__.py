# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from PIL import Image, ImageDraw, ImageFont
from papirus import Papirus

class PapirusPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.ProgressPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")
        self.papirus = Papirus()
        self.font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 20)
    
    def on_print_progress(storage, path, progress):
        image = Image.new('1', papirus.size, 1)
        
        draw = ImageDraw.Draw(image)
        
        #Draw progress
        screen_size_x, screen_size_y = papirus.size
        start_x = screen_size_x / 10
        end_x = screen_size_x - start_x
        start_y = screen_size_x / 2
        end_y = start_y + 20
        draw.rectangle((start_x, start_y, end_x, end_y), 1, 0)
        fillWidth = im.width * progress / 100
        draw.rectangle((start_x, start_y, fillWidth, end_y), 0, 0)
        
        # Draw text
        draw.text((0, 0), path, font=font, fill=BLACK)

        del draw

        papirus.display(image)
        papirus.update()
        pass

    def on_slicing_progress(storage, path, progress):
        pass

__plugin_name__ = "Papirus"
__plugin_implementation__ = PapirusPlugin()
