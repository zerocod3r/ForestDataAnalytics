# Python Code for parsing json data in files stored in ~\DataSets\ folder.
# To manually parse a file, add it to ~\DataSets\ folder and edit line - 25.
# For our purpose we are only picking up few keys from raw json data for 
# better visualization. 



from bs4 import BeautifulSoup
import requests,json,os
from geopy.geocoders import Nominatim
import time


def locationGetter(latutm,longutm):
    url = 'http://epsg.io/trans?s_srs=3067&t_srs=4326&x=' + str(latutm) + '&y=' + str(longutm)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = json.loads(soup.text)
    #print(str(data['y']) + str(data['x']))
    latitude = str(data['y'])
    longitude = str(data['x'])
    tmp = latitude + ','+ longitude
    geolocator = Nominatim()
    location = geolocator.reverse(tmp)
    #print(location.address)
    return location,latitude,longitude



rawjsonfile = open("DataSets/S.json")   # Add dataset file name here
data = json.load(rawjsonfile)

dm = data['ForestPropertyData']['Stands']['Stand']
finaldata = []
area = []
op = open("parsedData/jsondata" + os.path.basename(rawjsonfile.name),"a")   # Data stored in parsedData folder
op.write('[\n')
for fdat in dm:
    try:
        # Fetching Baisc Stand Attributes 
        st = fdat['StandBasicData']['SoilType']['__text']
        stnum = fdat['StandBasicData']['StandNumber']['__text']
        fertcls = fdat['StandBasicData']['FertilityClass']['__text']
        cutres = fdat['StandBasicData']['CuttingRestriction']['__text']
        areatemp = fdat['StandBasicData']['Area']['__text']
        standdate = fdat['StandBasicData']['StandBasicDataDate']['__text']

        # Converting GML coordinates to Latitude & longitude
        latutm = fdat['StandBasicData']['PolygonGeometry']['pointProperty']['Point']['coordinates']['__text'].split(',')[0]
        longutm = fdat['StandBasicData']['PolygonGeometry']['pointProperty']['Point']['coordinates']['__text'].split(',')[1]
        location,latitude,longitude = locationGetter(latutm,longutm)

        dateList = standdate.split('-')
        date_at = dateList[0] + '-' + dateList[1] + '-' + dateList[2] + 'T00:00:00Z'

        # Fetching treestandsummary attributes
        treeData = fdat['TreeStandData']['TreeStandDataDate'][1]
        meanAge = treeData['TreeStandSummary']['MeanAge']['__text']
        stemCount = treeData['TreeStandSummary']['StemCount']['__text']
        meanDiameter = treeData['TreeStandSummary']['MeanDiameter']['__text']
        meanHeight = treeData['TreeStandSummary']['MeanHeight']['__text']
        vol = treeData['TreeStandSummary']['Volume']['__text']
        sawLogVol = treeData['TreeStandSummary']['SawLogVolume']['__text']
        pulpWoodVol = treeData['TreeStandSummary']['PulpWoodVolume']['__text']
        leafBiomas = treeData['TreeStandSummary']['LeafBiomass']['__text']
        volGrowth = treeData['TreeStandSummary']['VolumeGrowth']['__text']
    except KeyError:
        break
    dataDict = '{"soilType":"' + str(st) + '","standNumber":"' + str(stnum) + '","fertilityClass":"' + str(fertcls) + '","cuttingRestriction":"' + str(cutres) + '","area":"' + str(areatemp) +'","standBasicDataDate":"' + date_at + '","meanAge":"' + str(meanAge) + '","stemCount":"'+ str(stemCount) +'","meanDiameter":"'+str(meanDiameter)+'","meanHeight":"'+str(meanHeight)+'","volume":"'+str(vol)+'","sawLogVolume":"'+str(sawLogVol)+'","pulpWoodVolume":"'+str(pulpWoodVol)+'","leafBiomass":"'+str(leafBiomas)+'","volumeGrowth":"'+str(volGrowth) +'","latitude":"'+str(latitude)+'","longitude":"'+str(longitude)+'","location":"'+str(location)+'"},'

    op.write(dataDict + "\n")
    time.sleep(20)

op.write(']')
op.close()

