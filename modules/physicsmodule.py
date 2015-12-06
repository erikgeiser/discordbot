"""
    Collection of physics related modules
"""

from astropy.coordinates import ICRS, Galactic, Angle
from astropy import units as u

class Mastro:
    def __init__(self,dclient):
        self.dclient = dclient

    def check(self,message):
        msg = message.content

        if msg.startswith("!eq2gal "):
            coords = msg.replace("!eq2gal ","").split("/")
            if len(coords)!=2:
                self.dclient.send_message(message.channel,"Invalid Coordinates")
            else:
                gal = self.eq2gal(coords[0],coords[1])
                if gal==0:
                    self.dclient.send_message(message.channel,"Invalid Coordinates")
                else:
                    self.dclient.send_message(message.channel,"*%s in Galactic Coordinates:*\nl=%s,   b=%s" % ("/".join(coords),str(gal.l.deg),str(gal.b.deg)))


    def eq2gal(self,ra,dec):
        try:
            ra = Angle(ra)
            dec = Angle(dec)
            c = ICRS(ra=ra, dec=dec)
            return c.transform_to(Galactic)
        except Exception as e:
            print(e)
            return 0
