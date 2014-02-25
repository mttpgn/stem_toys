from stem.control import Controller as Cr

with Cr.from_port(port = 9051) as controller:
  controller.authenticate()
  while True:
    temp_read=int(controller.get_info("traffic/read"))
    temp_written=int(controller.get_info("traffic/written"))
    time.sleep(1)
    print "The past second, Tor has read %s more bytes and written %s \
      more." % (str(int(controller.get_info("traffic/read"))-temp_read), \
      str(int(controller.get_info("traffic/written"))-temp_written))


