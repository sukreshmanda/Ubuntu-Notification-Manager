'''
    create custom notification manager from python3.
'''

import gi

gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init("Dumb Minds")

notification = Notify.Notification.new(
	"Firefox",
	"<b>Open <i>Firefox</i> with notification manager</b>",
	"/home/student/Pictures/HatchfulExport-All/logo.png",
)

notification.set_urgency(2)
def callback():
	pass
	
notification.add_action(
	"action_click",
	"Reply to Message",
	callback,
	None
)
notification.show()
