import time
from os import uname

if uname()[4].startswith("arm"):
    import scrollphathd
    from scrollphathd.fonts import font3x5
else:
    print('MOCKING SCROLLPHATHD')
    import scrollphathd_mock as scrollphathd

def scroll_message(message):
    print(message)
    scrollphathd.rotate(degrees=180)
    scrollphathd.set_brightness(0.2)
    scrollphathd.clear()
    length = scrollphathd.write_string(message, x=1)
    scrollphathd.show()
    time.sleep(0.5)

    length -= scrollphathd.width

    while length > 0:
        scrollphathd.scroll(1)
        scrollphathd.show()
        length -= 1
        time.sleep(0.02)

    time.sleep(0.5)
