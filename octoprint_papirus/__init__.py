# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from PIL import Image, ImageDraw, ImageFont
from papirus import Papirus
from datetime import datetime

class PapirusPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.ProgressPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")
        self.papirus = Papirus()
        self.font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 14)
        self.papirus.clear()
        self.last_update = datetime.now()
    
    def on_print_progress(self, storage, path, progress):
        pass

    def on_slicing_progress(self, slicer, source_location, source_path, dest_location, dest_path, progress):
        if progress == 0 or progress == 100 or (datetime.now() - self.last_update).total_seconds() > 3:
            width, height = self.papirus.size
            self.last_update = datetime.now()
            image = Image.new('1', (width, height), 1)
            
            draw = ImageDraw.Draw(image)
            
            #Draw progress
            start_x = width / 10
            end_x = width - start_x
            start_y = height / 2
            end_y = start_y + 20
            draw.rectangle((start_x, start_y, end_x, end_y), 1, 0)
            fillWidth = (end_x - start_x) * progress / 100
            try:
                self._logger.info("On slicing progress : ({}, {}, {}, {}, {})".format(start_x, end_x, start_y, end_y, fillWidth))
            except:
                self._logger.info("Error writing log")
            draw.rectangle((start_x, start_y, start_x + fillWidth, end_y), 0, 0)
            
            # Draw text
            draw.text((0, 0), dest_path, font=self.font, fill=0)

            del draw

            self.papirus.display(image)
            self.papirus.update()

__plugin_name__ = "Papirus"
__plugin_implementation__ = PapirusPlugin()
