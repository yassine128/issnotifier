import requests
from pynotifier import Notification
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import time
from win10toast import ToastNotifier


def test():
    try:
        myrequest = requests.get('http://api.open-notify.org/iss-now.json')

        isslocation = myrequest.json()['iss_position']
        isslatitude = isslocation['latitude']
        isslongitude = isslocation['longitude']


        geolocator = Nominatim(user_agent="isslocalisation")
        location = geolocator.geocode(userlocation)

        latitude_User = location.latitude
        longitude_User = location.longitude

        userCoordinates = (float(location.latitude), float(location.longitude))
        issCoordinates = (float(isslatitude), float(isslongitude))

        #distance = great_circle(userCoordinates, issCoordinates).miles


        #GET THE COUNTRY OF THE USER 
        countryUser = geolocator.reverse(str(location.latitude)+', '+str(location.longitude))
        countryUser = str(countryUser)
        v1 = countryUser.split()
        countryUser = v1[len(v1)-1]

        #GET THE COUNTRY THE ISS ON TOP OF
        try:   
            countryIss = geolocator.reverse(str(float(isslatitude))+', '+str(float(isslongitude)))
            countryIss = str(countryIss)
            v1 = countryIss.split()
            countryIss = v1[len(v1)-1]
        except:
            countryIss = ''
            pass


        #NOTIFY IF ISS ON TOP OF THE SAME COUNTRY AS THE USER
        if countryIss == countryUser:
            v2 = 0
            if v2 != 1:
                toast = ToastNotifier()
                toast.show_toast("issnotifier","Iss above your country!",duration=5)
                v2 = 1
        elif countryIss != countryUser or countryIss == '':
            v2 = 0
    except AttributeError:
        pass

v3 = 0
while(True):
    if v3 == 0: 
        userlocation = str(input('Please enter your adress here ---> '))
        v3 = 1
    else:
        pass
    test()

