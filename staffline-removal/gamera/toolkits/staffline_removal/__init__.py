"""
Toolkit setup

This file is run on importing anything within this directory.
Its purpose is only to help with the Gamera GUI shell,
and may be omitted if you are not concerned with that.
"""

from gamera import toolkit
from gamera.gui import has_gui
from gamera.toolkits.staffline_removal.toolkit_icon import toolkit_icon
from gamera.toolkits.staffline_removal.plugins.staff_removal import StaffRemovalGenerator


import wx
