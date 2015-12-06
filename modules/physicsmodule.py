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
                gal = eq2gal(coords[0],coords[1])
                if gal==0:
                    self.dclient.send_message(message.channel,"Invalid Coordinates")
                else:
                    self.dclient.send_message(message.channel,"%s in Galactic Coordinates\nl=%.2f, d=%.2f"%("/".join(coords),gal.l.deg,gal.d.deg))


    def eq2gal(self,ra,dec):
        try:
            ra = Angle(coords[0])
            dec = Angle(coords[1])
            c = ICRS(ra=ra, dec=dec)
            return c.galactic
        except:
            return 0
