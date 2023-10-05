import webbrowser
f = open('cd.html','w')

## BASIC INPUT
sku = input("SKU: ")
artist = input("Artist: ")
album = input("Nth (Album, Mini Album, EP, Single): ").title()
if "Ep" in album:
    album = album.replace("Ep","EP")
name = input("Title: ")
release_date = input("Release Date (YYMMDD):")



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
for x in range(len(package_list)):
    packageHTML = f"""
    <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">{package_list[x][0].upper()}</span>
    <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span>
    """
    # page
    if package_list[x][1] != "":
        packageHTML += f"""
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">{package_list[x][1]}p / """
    else:
        packageHTML += f"""
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">"""
   
    # random
    if package_list[x][3] != "":
        packageHTML += f"random {int(package_list[x][2])}ea out of {package_list[x][3]}"
    else:
        packageHTML += f"{int(package_list[x][2])}ea"
        
    # note
    if package_list[x][4] != "":
        packageHTML += f" / {package_list[x][4]}"

    
    packageHTML += """</span><span style="font-size: 12pt;"><br /><br /></span>"""

    package += packageHTML
    x += 1








def bigCommerce(artist, album, name, release_date, track, version, package):

    description = f"""
    <p dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 14pt; font-family: Arial,sans-serif; color: #ff0000; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">K-Pop</span><span style="font-size: 14pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> {artist.strip().upper()} {album.title()} [ {name} ] </span></p>
    <p dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■</span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;Release Date : 20{'.'.join(release_date[i:i+2] for i in range(0, len(release_date), 2))}</span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■</span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;Genre : K-Pop</span><br /><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■</span><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;Disc Format(s) : CD</span></p>
    <p dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span></p>
    <p dir="ltr" style="line-height: 1.8; margin-top: 0pt; margin-bottom: 0pt;">
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #000000; background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span>
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">■ Track List</span>
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #0000ff; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span>
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #800080; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">DISC1 (CD)</span>
        <span style="font-size: 12pt; font-family: Arial,sans-serif; color: #800080; background-color: transparent; font-weight: bold; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"><br /></span>
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
    f.write(description)
    return(description)



def walmart(sku, artist, album, name, release_date, versionHTML, package):
    description = f"""
    <h3 style="line-height: 150%">
    <font face="Arial" color="#ff0000"><b><font >K-Pop</font><font face="Arial">{artist.strip().upper()} {album.title()} [ {name} ]</b></font></h3>
    <br>
    <p style="line-height: 150%">
    <font face="Arial" size="3">
    <font color="#0000ff">■</font> Release Date : 20{'.'.join(release_date[i:i+2] for i in range(0, len(release_date), 2))}<br>
    <font color="#0000ff">■</font> Genre : K-Pop<br>
    <font color="#0000ff">■</font> Disc Format(s) : CD<br>
    <font color="#0000ff">■</font> KJCstar Product ID : {sku.upper()}</font>
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

    <p dir="ltr" style="line-height: 150%">
    <font size="3"  face="Arial">This album has {len(versionHTML.split()[::3])} versions : <br>{versionHTML}  </font></p>

    <p dir="ltr" style="line-height: 150%"><font face="Arial" size="3">
    On Package : <br>
    {package}
    </font>
    </p>

    """
    f.write(description)
    return(description)


bigCommerce(artist, album, name, release_date, track, version, package)

walmart(sku, artist, album, name, release_date, versionHTML, package)


f.close()
webbrowser.open('cd.html')