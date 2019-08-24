from geopy.geocoders import Nominatim
import csv
import requests
import json
import statistics


def process(address, rented, house, price):
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(address)
    
   
    addressList = location.address.split(', ')
    d = {}
 
    with open('Neighbourhood_Crime_Rates_Boundary_File_.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                d[row[1]] = float(row[26])
                """ print(f'\t{row[1]} is {row[26]}.') """
                line_count += 1
    
    d['Etobicoke North'] = round(statistics.mean([d['Mount Olive-Silverstone-Jamestown'], d['West Humber-Clairville'], d['Thistletown-Beaumond Heights'], d['Rexdale-Kipling'], d['Elms-Old Rexdale'], d['Kingsview Village-The Westway']]), 2)
    d['Etobicoke Centre'] = round(statistics.mean([d['Willowridge-Martingrove-Richview'], d['Humber Heights-Westmount'], d['Edenbridge-Humber Valley'], d['Princess-Rosethorn'], d['Eringate-Centennial-West Deane'], d['Markland Wood'], d['Etobicoke West Mall'], d['Islington-City Centre West']]), 2)
    d['Etobicoke-Lakeshore'] = round(statistics.mean([d['Islington-City Centre West'], d['Kingsway South'], d['Stonegate-Queensway'], d['Mimico'], d['New Toronto'], d['Long Branch'], d['Alderwood']]), 2)
    d['Parkdale-High Park'] = round(statistics.mean([d['High Park-Swansea'], d['Runnymede-Bloor West Village'], d['High Park North'], d['Roncesvalles'], d['South Parkdale'], d['Junction Area']]), 2)
    d['York South-Weston'] = round(statistics.mean([d['Junction Area'], d['Rockcliffe-Smythe'], d['Mount Dennis'], d['Beechborough-Greenbrook'], d['Keelesdale-Eglinton West'], d['Brookhaven-Amesbury'], d['Weston'], d['Maple Leaf'], d['Rustic'], d['Pelmo Park-Humberlea']]), 2)
    d['York Centre'] = round(statistics.mean([d['Downsview-Roding-CFB'], d['York University Heights'], d['Glenfield-Jane Heights'], d['Bathurst Manor'], d['Westminster-Branson'], d['Clanton Park'], d['Lansing-Westgate']]), 2)
    d['Humber River-Black Creek'] = round(statistics.mean([d['York University Heights'], d['Glenfield-Jane Heights'], d['Downsview-Roding-CFB'], d['Pelmo Park-Humberlea'], d['Humbermede'], d['Humber Summit'], d['Black Creek']]), 2)
    d['Eglinton-Lawrence'] = round(statistics.mean([d['Yorkdale-Glen Park'], d['Englemount-Lawrence'], d['Bedford Park-Nortown'], d['Lawrence Park North'], d['Lawrence Park South'], d['Forest Hill North'], d['Briar Hill-Belgravia'], d['Yonge-Eglinton']]), 2)
    d['Davenport'] = round(statistics.mean([d['Little Portugal'], d['Dufferin Grove'], d['Dovercourt-Wallace Emerson-Junction'], d['Corso Italia-Davenport'], d['Weston-Pellam Park'], d['Caledonia-Fairbank']]), 2)
    d['Spadina-Fort York'] = round(statistics.mean([d['Niagara'], d['Waterfront Communities-The Island'], d['Kensington-Chinatown'], d['Bay Street Corridor'], d['Trinity-Bellwoods']]), 2)
    d['Scarborough-Rouge Park'] = round(statistics.mean([d['West Hill'], d['Centennial Scarborough'], d['Rouge'], d['Highland Creek'], d['Malvern']]), 2)
    d['University-Rosedale'] = round(statistics.mean([d['Bay Street Corridor'], d['Kensington-Chinatown'], d['University'], d['Palmerston-Little Italy'], d['Annex'], d['Rosedale-Moore Park']]), 2)
    d['Toronto-St Paul’s'] = round(statistics.mean([d['Wychwood'], d['Casa Loma'], d['Humewood-Cedarvale'], d['Oakwood Village'], d['Forest Hill South'], d['Yonge-St.Clair'], d['Yonge-Eglinton'], d['Mount Pleasant West']]), 2)
    d['Toronto Centre'] = round(statistics.mean([d['Church-Yonge Corridor'], d['Moss Park'], d['Regent Park'], d['Cabbagetown-South St.James Town'], d['North St.James Town']]), 2)
    d['Scarborough-Guildwood'] = round(statistics.mean([d['Guildwood'], d['Scarborough Village'], d['Woburn'], d['West Hill'], d['Morningside']]), 2)
    d['Toronto-Danforth'] = round(statistics.mean([d['Old East York'], d['Danforth East York'], d['Danforth'], d['Greenwood-Coxwell'], d['South Riverdale'], d['North Riverdale'], d['Blake-Jones'], d['Playter Estates-Danforth'], d['Broadview North']]), 2)
    d['Don Valley West'] = round(statistics.mean([d['Banbury-Don Mills'], d['St.Andrew-Windfields'], d['Bridle Path-Sunnybrook-York Mills'], d['Lawrence Park North'], d['Lawrence Park South'], d['Mount Pleasant East'], d['Leaside-Bennington'], d['Thorncliffe Park']]), 2)
    d['Don Valley East'] = round(statistics.mean([d['St.Andrew-Windfields'], d['Parkwoods-Donalda'], d['Victoria Village'], d['Banbury-Don Mills'], d['Flemingdon Park']]), 2)
    d['Don Valley North'] = round(statistics.mean([d['Bayview Village'], d['Bayview Woods-Steeles'], d['Hillcrest Village'], d['Pleasant View'], d['Don Valley Village'], d['Henry Farm']]), 2)
    d['Willowdale'] = round(statistics.mean([d['Willowdale East'], d['Willowdale West'], d['Lansing-Westgate'], d['Newtonbrook West'], d['Newtonbrook East']]), 2)
    d['Beaches-East York'] = round(statistics.mean([d['The Beaches'], d['East End-Danforth'], d['O\'Connor-Parkview'], d['Taylor-Massey'], d['Woodbine-Lumsden'], d['South Riverdale'], d['Woodbine Corridor'], d['Danforth'], d['Danforth East York'], d['Old East York']]), 2)
    d['Scarborough Southwest'] = round(statistics.mean([d['Scarborough Village'], d['Cliffcrest'], d['Kennedy Park'], d['Birchcliffe-Cliffside'], d['Oakridge'], d['Clairlea-Birchmount']]), 2)
    d['Scarborough Center'] = round(statistics.mean([d['Dorset Park'], d['Bendale'], d['Eglinton East'], d['Ionview'], d['Wexford/Maryvale']]), 2)
    d['Scarborough-Agincourt'] = round(statistics.mean([d['Steeles'], d['L\'Amoreaux'], d['Tam O\'Shanter-Sullivan']]), 2)
    d['Scarborough North'] = round(statistics.mean([d['Malvern'], d['Agincourt South-Malvern West'], d['Rouge'], d['Milliken'], d['Agincourt North']]), 2)

    for add in addressList:
        add = add.replace('—', '-')
        if add in d:
            breakins = d[add]

    risk = breakins/76
    if rented:
        risk *= 1.37
    if house:
        risk *= 1.42

    risk = round(risk, 2)
    print(risk)
    housemin = {}
    housemin['100K'] = 70
    housemin['300K'] = 118
    housemin['700K'] = 139
    housemin['1.5M'] = 192
    housemin['MAX'] = 301
    housemax = 450
    apartmentmin = {}
    apartmentmin['100K'] = 23
    apartmentmin['300K'] = 29
    apartmentmin['700K'] = 34
    apartmentmin['1.5M'] = 48
    apartmentmin['MAX'] = 73
    apartmentmax = 120
    premium = 0
    if house:
        if price < 100000:
            premium = housemin['100K'] + (housemin['300K'] - housemin['100K']) * risk/5
        elif price < 300000:
            premium = housemin['300K'] + (housemin['700K'] - housemin['300K']) * risk/5
        elif price < 700000:
            premium = housemin['700K'] + (housemin['1.5M'] - housemin['700K']) * risk/5
        elif price < 1500000:
            premium = housemin['1.5M'] + (housemin['MAX'] - housemin['1.5M']) * risk/5
        else:
            premium = housemin['MAX'] + (housemax - housemin['MAX']) * risk/5
        if rented:
            premium = premium * 1/3
    else:
        if price < 100000:
            premium = apartmentmin['100K'] + (apartmentmin['300K'] - apartmentmin['100K']) * risk/5
        elif price < 300000:
            premium = apartmentmin['300K'] + (apartmentmin['700K'] - apartmentmin['300K']) * risk/5
        elif price < 700000:
            premium = apartmentmin['700K'] + (apartmentmin['1.5M'] - apartmentmin['700K']) * risk/5
        elif price < 1500000:
            premium = apartmentmin['1.5M'] + (apartmentmin['MAX'] - apartmentmin['1.5M']) * risk/5
        else:
            premium = apartmentmin['MAX'] + (apartmentmax - apartmentmin['MAX']) * risk/5


    premium = round(premium, 2)
    return risk, premium