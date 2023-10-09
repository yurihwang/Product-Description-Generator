import webbrowser
cd_bigcommerce = open('cd_bigcommerce.txt','w')
cd_ebay = open('cd_ebay.txt','w')
cd_walmart = open('cd_walmart.txt','w')
cd_amazon = open('cd_amazon.txt','w')

## BASIC INPUT
sku = input("SKU: ").strip().upper()
upc = input("UPC: ").strip()
artist = input("Artist: ").strip()
album = input("Nth (Album, Mini Album, EP, Single): ").strip().title()
if "Ep" in album:
    album = album.replace("Ep","EP")
if "Mini" in album and "Album" not in album:
    album += " Album"
name = input("Title: ").strip().title()
release_date = input("Release Date (YYMMDD):").strip()
record_label = input("Record Label (~ ent): ").strip().title()
if record_label[-3:] == "Ent":
    record_label.replace("Ent", "Entertainment")


## TRACKLIST - tracklist
print("\nTracklist **ENTER to end**")
tracklist =[]
song = "song"
while song != "":
    song = str(input("Song: "))
    if song == "":
        break
    tracklist.append(song)


trackHTML = ""
track = ""
for x in range(len(tracklist)):
    if x == 0:
        track += """
        <p dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;">
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span>
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■ Track List</span>
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span>
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #800080; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">DISC1 (CD)</span>
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #800080; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span>
        """

    trackHTML = f"""<span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">{"00"+ str(x+1)+ " "}{tracklist[x]}</span>
                <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span>"""
    track += trackHTML
    x += 1



## VERSIONS - versions
print("\nVersions **ENTER to end**")
versions =[]
version = "version"
while version != "":
    version = str(input("Version: "))
    if version == "":
        break
    versions.append(version)


versionHTML = ""
for x in range(len(versions)):
    versionHTML += versions[x].strip().upper() + " ver."
    x += 1
    if x < len(versions):
        versionHTML += " / "

version = ""  
if len(versions) > 1:
    version += f"""<h3 dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">This album has {len(versions)} versions :&nbsp;</span></h3>
                <h3 dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">{versionHTML}</span></h3>"""




### ON PACKAGE ###
gift = "gift"
page = 0
num = 1
total = 1
note = ""
package_list =[]
print("\nPackages **ENTER to end**")
while gift != "":
    single_package = []
    gift = str(input("Component: "))
    if gift == "":
        break
    page = input("(ENTER to skip) Pages: ")
    num = input("How many? ")
    total = input("(ENTER to skip) Randomly out of... ")
    note = input("(ENTER to skip) Any other note? ")
    print("\n")
    single_package= [gift,page,num,total, note]
    package_list.append(single_package)


package = ""
site_description = ""
for x in range(len(package_list)):
    packageHTML = f"""
    <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">- {package_list[x][0].upper()}</span>
    <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br>&nbsp;&nbsp;</span>
    """

    # page
    if package_list[x][1] != "":
        packageHTML += f"""
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">{package_list[x][1]}p / """
        site_description = f"{package_list[x][1]}p {package_list[x][0].title()} + "
    else:
        packageHTML += f"""
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">"""
        site_description += f"{package_list[x][0].title()}"

    # random
    if package_list[x][3] != "":
        packageHTML += f"random {package_list[x][2]}ea out of {package_list[x][3]}"
        site_description += f" ({package_list[x][2]}/{package_list[x][3]})"

    else:
        packageHTML += f"{package_list[x][2]}ea"
        site_description += f"({package_list[x][2]})"

    # note
    if package_list[x][4] != "":
        packageHTML += f" / {package_list[x][4]}"

    
    packageHTML += """</span><span style="font-size: 12pt;"><br /><br /></span>"""

    package += packageHTML
    x += 1








def bigCommerce(sku, upc, artist, album, name, release_date, track, versionHTML, version, package):

    listing_title = f"{artist.upper()} {album.title()} [{name}])"
    cd_bigcommerce.write("Product Name: ", listing_title, "\nSKU: ", sku, "\n\nProduct UPC: ", upc, "\n\nVersions: ", versionHTML)
    cd_bigcommerce.write("\n\nAvailability: Approximately 7 ~ 9 business days")

    description = f"""
    <p dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 14pt; font-family: Arial,sans-serif; color: #ff0000; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">K-Pop</span><span style="font-size: 14pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> {artist.strip().upper()} {album.title()} [ {name} ] </span></p>
    <p dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■</span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;Release Date : 20{'.'.join(release_date[i:i+2] for i in range(0, len(release_date), 2))}</span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■</span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;Genre : K-Pop</span><br /><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■</span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;Disc Format(s) : CD</span></p>
    <p dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span></p>

    {track}
    <p>&nbsp;</p>

    <h3 dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■ Contents</span></h3>
    {version}

    <p>&nbsp;</p>
    <h3 dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 10pt;"><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">On Package :</span></h3>

    <h3 dir="ltr" style="line-height: 1.2; margin-top: 0pt; margin-bottom: 0pt;">
    {package}</h3>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    """
    ## for image
    # <p><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><img src="http://image.kyobobook.co.kr/newimages/apps/b2c/prom/2023/09/26/2564238-2.jpg" alt="" /></span></p>
    
    cd_bigcommerce.write("\n=====BIG COMMERCE=====\n\n\n")
    cd_bigcommerce.write(description)
    return(description)



def ebay(sku, upc, artist, album, name, release_date, record_label, track, version, package):
    
    listing_title = f"{artist.upper()} {album.title()} [{name}] ({sku})"
    artist = artist.title()
    cd_ebay.write("Listing Title: ", listing_title, "\n\nArtist: ", artist, "\nRelease Title: ", name, "\nUPC: ", upc)
    cd_ebay.write("\n\nGenre: Pop\nRecord Label: ", record_label, "\nStyle: K-Pop")


    description = f"""

    <p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;">
    <span style="font-size: 14pt; font-family: Arial, sans-serif; color: rgb(255, 0, 0); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">K-Pop</span><span style="font-size: 14pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"> {artist.upper()} {album.title()} [ {name} ] ({sku})</span></p>

    <p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 10pt; font-family: Arial, sans-serif; color: rgb(0, 128, 128); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">Please consider that product information, release date or special content could be change without notice depending on publisher.&nbsp;</span></p>  
    <p>
    <font face="Arial" size="3" color="#008080"><b>
    💽 Safely packed with Tracking Number<br>
    ✔ 100% Original Brand New Product<br> 
    🎯 Your order will be reflected and counted towards CIRCLE and HANTEO chart!<br></b></font>
    </p>

    <span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">
    <span style="color: rgb(0, 0, 255)">■</span> Artist : {artist.strip().capitalize()}<br>
    <span style="color: rgb(0, 0, 255)">■</span> Release Date : 20{'.'.join(release_date[i:i+2] for i in range(0, len(release_date), 2))}<br>
    <span style="color: rgb(0, 0, 255)">■</span> Genre : K-Pop<br>
    <span style="color: rgb(0, 0, 255)">■</span> Disc Format(s) : CD<br>
    <br>
    <span style="color: rgb(0, 0, 255)">■</span> Language : Korean<br>
    <span style="color: rgb(0, 0, 255)">■</span> Country of origin : Korea<br>
    <span style="color: rgb(0, 0, 255)">■</span> Label : {record_label}<br>
    <br>
    <span style="color: rgb(0, 0, 255)">■</span> KJCstar Product ID : {sku.upper()}
    </span>
    </p>

    <br><br><br>
    {track}
    <p>&nbsp;</p>

    <br><br>

    <p dir="ltr" style="line-height: 150%">
    <font color="#0000ff" size="3" face="Arial"><b>■ Contents</b></font></p>

    {version}

    <p dir="ltr" style="line-height: 150%"><font face="Arial" size="3" color="#000000">
    On Package : <br><br>
    {package}
    </font>
    </p>


    <br><br><br><br><br><br>

    <div dir="ltr" style="margin-left:0pt;" align="left"><table style="border:none;border-collapse:collapse;"><colgroup><col width="624"></colgroup><tbody><tr style="height:43pt"><td style="vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: rgb(52, 254, 0); font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">Your order will be reflected and counted towards CIRCLE and HANTEO chart.</span></p></td></tr><tr style="height:43pt"><td style="vertical-align:top;background-color:#6767ff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 255, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">PRODUCT GUARANTEE</span></p></td></tr><tr style="height:61pt"><td style="vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">We guarantee all our items are 100% original. If you are not satisfied with our items, Please contact us!</span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"><br></span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"> </span><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 0, 0); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">NOT A BOOTLEG CD!</span></p></td></tr><tr style="height:43pt"><td style="vertical-align:top;background-color:#6767ff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 255, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">SHIPPING</span></p></td></tr><tr style="height:170.5pt"><td style="vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 0, 0); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">All orders from the U.S. will be shipped from our US office via USPS with tracking number (exceptions may occur, we will notify you prior shipping or specify in item description).</span><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 0, 0); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"><br></span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"> </span><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(0, 0, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">Sorry, we currently do not offer International Shipping due to increase of shipping cost (except Canada). Buyers who wish to purchase our merchandise outside of the U.S. may choose to use desired shipping forwarder company. If you choose to use a shipping forwarder company, we are not responsible for any damage or loss after the package is safely delivered to the forwarding company. Also, we are not responsible for Buyer's Customs charges.</span><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(0, 0, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"><br></span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"> We ship within 1 to 5 business days except holiday. Transit times may vary particularly during peak periods.</span></p></td></tr><tr style="height:43pt"><td style="vertical-align:top;background-color:#6767ff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 255, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">ESTIMATED DELIVERY TIME</span></p></td></tr><tr style="height:79pt"><td style="vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">US Standard : 4 - 14 business days via USPS First Class/Media/Parcel</span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"><br></span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">US Expedited : 2 - 4 business days via USPS Priority</span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"><br></span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">Canada : 15 - 25 business days</span></p></td></tr><tr style="height:43pt"><td style="vertical-align:top;background-color:#6767ff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 255, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">SHIPPING &amp; HANDLING CHARGE</span></p></td></tr><tr style="height:43pt"><td style="vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">No handling charge. </span><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 0, 0); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">Tracking number will be provided on all orders.</span></p></td></tr><tr style="height:43pt"><td style="vertical-align:top;background-color:#6767ff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 255, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">COMBINED SHIPPING</span></p></td></tr><tr style="height:61pt"><td style="vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">We always do combine shipping.</span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"><br></span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">The highest shipping costs and each additional costs will be calculated as a total shipping fee.</span></p></td></tr><tr style="height:43pt"><td style="vertical-align:top;background-color:#6767ff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 255, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">CUSTOMS</span></p></td></tr><tr style="height:61pt"><td style="vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">We do not hold any liability on any issues relating to CUSTOMS including but not limited to delays and taxation. Please check with your country's Customs Office to determine the additional cost and policy.</span></p></td></tr><tr style="height:43pt"><td style="vertical-align:top;background-color:#6767ff;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; color: rgb(255, 255, 255); background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">RETURN POLICY</span></p></td></tr><tr style="height:133pt"><td style="vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.7999999999999998;margin-top:0pt;margin-bottom:0pt;"><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">We accept return request for buyer's any reason, but the item must be sealed, unused, and in original condition. Return request must be made within 14 days of item delivery. If the returning item has been opened or used, the return request will not be accepted.</span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"><br></span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"> Refund will be issued after arrival and inspection of the returning item. Shipping is NOT REFUNDABLE.</span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"><br></span><span style="font-size: 12pt; font-family: Arial, sans-serif; background-color: transparent; font-weight: 700; font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;"> If you received wrong item, please let us know to resolve problem. We will exchange to correct item upon receiving wrong item in unopened, in original condition (We will pay return shipping).</span></p></td></tr></tbody></table></div></span>


    """

    cd_ebay.write("\n=====EBAY=====\n\n\n")
    cd_ebay.write(description)
    return(description)



def walmart(sku, upc, artist, album, name, release_date, record_label, versionHTML, version, package, site_description):
    
    listing_title = f"{artist.upper()} {album.title()} [{name}]"
    if len((versionHTML).split()) >= 5:
        cd_walmart.write("\nSite Description: K-Pop ", listing_title, " **random ver.** Incl. ", site_description)
        listing_title += f" random ver. ({sku})"
    else:
        listing_title += f" ({sku})"
        cd_walmart.write("\nSite Description: K-Pop ", listing_title, " Incl. ", site_description)


    cd_walmart.write("GTIN: 0", upc, "\nItem Name: ", listing_title, "\n\nSKU: ", sku, "\n\nGenre: K-Pop\n\nRecord Label: ", record_label)
    
    description = f"""
    <h3 style="line-height: 150%">
    <font face="Arial" size="4" color="#ff0000"><b><font >K-Pop </font><font face="Arial" size="4" color="#000000">{artist.strip().upper()} {album.title()} [ {name} ]</b></font></h3>
    <p style="line-height: 150%">
    <font face="Arial" size="3">
    <font color="#0000ff">■</font> <font color="#000000">Release Date : 20{'.'.join(release_date[i:i+2] for i in range(0, len(release_date), 2))}</font><br>
    <font color="#0000ff">■</font> <font color="#000000">Genre : K-Pop</font><br>
    <font color="#0000ff">■</font> <font color="#000000">Disc Format(s) : CD</font><br>
    <font color="#0000ff">■</font> <font color="#000000">KJCstar Product ID : {sku}</font>
    </font>
    </p>

    <p>
    <font face="Arial" size="3" color="#008080"><b>
    💽 Safely packed with Tracking Number<br>
    ✔ 100% Original Brand New Product<br> 
    🎯 Your order will be reflected and counted towards CIRCLE and HANTEO chart!<br></b></font>
    </p>

    <br>

    <p dir="ltr" style="line-height: 150%">
    <font color="#0000ff" size="3" face="Arial"><b>■ Contents</b></font></p>

    {version}

    <p dir="ltr" style="line-height: 150%"><font face="Arial" size="3" color="#000000">
    On Package : <br><br>
    {package}
    </font>
    </p>

    

    """
    cd_walmart.write("\n=====WALMART=====\n\n\n")
    cd_walmart.write(description)
    return(description)


def amazon(artist, album, name, sku, upc, versionHTML, site_description, record_label, release_date, trackHTML):
    listing_title = f"{artist.upper()} {album.title()} [{name}]"
    if len((versionHTML).split()) >= 5:
        for x in versionHTML.split()[::3]:
            listing_title += f" {x} ver. - Incl. {site_description}"
            cd_amazon.write(listing_title)
        
    else:
        listing_title += f" - Incl. {site_description}"
        cd_amazon.write(listing_title)

    track = trackHTML.replace("""<span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">""", "")
    track = track.replace("</span>","")

    description =f"""
    K-Pop {listing_title}<br>
    <br>
    ■ Genre : K-Pop<br>
    ■ Disc Format(s) : CD <br>
    ■ Record Label : {record_label} <br>
    ■ KJCstar ID : {sku}<br>
    <br>
    📆 Release Date : {release_date}<br>
    💽 Safely packed with Tracking Number<br>
    ✔ 100% Original Brand New Product<br>
    🎯 Your order will be reflected and counted towards CIRCLE and HANTEO chart!<br>
    <br>
    ■ Track List <br>
    {track}<br>
    <br><br>

    """
    cd_amazon.write("Listing Title: ",listing_title, "\nUPC: ", upc, "" )
    cd_amazon.write("Langauage: Korean\nMaufacturer: ", record_label, "\nPublication Date: ", release_date.replace(".","-"), "\nGenre: K-Pop\nCountry of Origin: South Korea\nDesigner Name: ", artist)
    cd_amazon.write("\n\nSKU: ", sku)
    cd_amazon.write(description)





bigCommerce(sku, upc, artist, album, name, release_date, track, versionHTML, version, package)
ebay(sku, upc, artist, album, name, release_date, record_label, track, version, package)
walmart(sku, upc, artist, album, name, release_date, record_label, versionHTML, version, package, site_description)
amazon(artist, album, name, sku, upc, versionHTML, site_description, record_label, release_date, trackHTML)





cd_bigcommerce.close()
cd_ebay.close()
cd_walmart.close()
cd_amazon.close()
webbrowser.open('cd_bigcommerce.txt')
webbrowser.open('cd_ebay.txt')
webbrowser.open('cd_walmart.txt')
webbrowser.open('cd_amazon.txt')