import cgi


from google.appengine.api import users
from google.appengine.ext import webapp


from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="de-de">
<head>
  <title>Sensoria Demo IPWE 1 Server</title>
  <meta http-equiv="expires" content="0; URL=/">
  <meta http-equiv="refresh" content="180; URL=/">
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body style="color: #FF6000; background-color: #000015; direction: ltr;" 
alink="#FF6000" link="#FF6000" vlink="#FF6000">
<table align="center" border="0" width="600">
  <tbody>
    <tr height="70">
      <td><br>
&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td align="center" valign="middle" width="170">&nbsp;&nbsp;</td>
      <td align="center" valign="middle" width="300">
      <h1>Sensoria Demo IPWE 1 Server</h1>
      </td>
      <td align="center" valign="middle" width="170"><small><small>
&nbsp;</small></small></td>
      <td>&nbsp;</td>
    </tr>
    <tr height="80">
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>
<form name="Schalten" action="ipwe.cgi" method="get">
<input value="ipwe" name="pg" type="hidden"><span style="font-family: Times New Roman;"><br>
  </span>
  <table style="width: 700px; text-align: left; margin-left: auto; margin-right: auto;" border="1" 
cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="text-align: center;">Sensortyp</td>
        <td style="text-align: center;">Adresse</td>
        <td style="text-align: center;">Beschreibung</td>
        <td style="text-align: center;">Temperatur</td>
        <td style="text-align: center;">Luftfeuchtigkeit</td>
        <td style="text-align: center;">Windgeschwindigkeit</td>
        <td style="text-align: center;">Regenmenge</td>
      </tr>
      <tr>
<td style="text-align: center;">T/F<br></td>
<td style="text-align: center;">0<br></td>
<td style="text-align: center;">Kueche<br></td>
<td style="text-align: center;">17.2 C<br></td>
<td style="text-align: center;">60 <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
      </tr>
      <tr>
<td style="text-align: center;">T/F<br></td>
<td style="text-align: center;">1<br></td>
<td style="text-align: center;">Yellow Room<br></td>
<td style="text-align: center;">16.4 C<br></td>
<td style="text-align: center;">60 <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
      </tr>
      <tr>
<td style="text-align: center;">T/F<br></td>
<td style="text-align: center;">2<br></td>
<td style="text-align: center;">Bad<br></td>
<td style="text-align: center;">18.1 C<br></td>
<td style="text-align: center;">60 <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
      </tr>
      <tr>
<td style="text-align: center;">T/F<br></td>
<td style="text-align: center;">3<br></td>
<td style="text-align: center;">Red Room<br></td>
<td style="text-align: center;">18.7 C<br></td>
<td style="text-align: center;">60 <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
      </tr>
      <tr>
<td style="text-align: center;">T/F<br></td>
<td style="text-align: center;">4<br></td>
<td style="text-align: center;">Carport<br></td>
<td style="text-align: center;"> 6.6 C<br></td>
<td style="text-align: center;">74 <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
      </tr>
      <tr>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;">  <br></td>
<td style="text-align: center;">  <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
      </tr>
      <tr>
<td style="text-align: center;">T/F<br></td>
<td style="text-align: center;">6<br></td>
<td style="text-align: center;">Flur<br></td>
<td style="text-align: center;">16.7 C<br></td>
<td style="text-align: center;">59 <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
      </tr>
      <tr>
<td style="text-align: center;">T/F<br></td>
<td style="text-align: center;">7<br></td>
<td style="text-align: center;">Blue Room<br></td>
<td style="text-align: center;">15.7 C<br></td>
<td style="text-align: center;">64 <br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;"> <br></td>
      </tr>
      <tr>
<td style="text-align: center;">Kombi<br></td>
<td style="text-align: center;"> <br></td>
<td style="text-align: center;">Aussensensor<br></td>
<td style="text-align: center;"> 5.3 C<br></td>
<td style="text-align: center;">80 <br></td>
<td style="text-align: center;">  0.2 km/h<br></td>
<td style="text-align: center;">      2.7 mm<br></td>
      </tr>
    </tbody>
  </table>
&nbsp;<br>
</form>
<table align="center" border="1" width="700">
  <tbody>
    <tr align="center" valign="middle">
      <td width="33%"><a href="/">n/a</a></td>
      <td width="34%"><a href="/">n/a</a></td>
      <td width="33%"><a href="/">n/a</a></td>
    </tr>
  </tbody>
</table>
<table align="center" border="0" width="700">
  <tbody>
    <tr height="50">
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr align="center" valign="middle">
      <td width="33%">CD</td>
      <td width="34%"></td>
      <td width="33%"></td>
    </tr>
  </tbody>
</table>
.
</body>
</html>

""")


application = webapp.WSGIApplication(
                                     [('/', MainPage)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()