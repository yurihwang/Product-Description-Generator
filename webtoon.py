import webbrowser
wt_bigcommerce = open('wt_bigcommerce.txt','w')
wt_ebay = open('wt_ebay.txt','w')
wt_walmart = open('wt_walmart.txt','w')
wt_amazon = open('wt_amazon.txt','w')


# basic input
sku = input("SKU: ").strip().upper()
title = input ("Title: ").strip().title()
kor_title = input("Korean Title: ").strip()
edition = input("**ENTER to skip** Edition: (Vol. # special, limited, box set, etc.)").title()
author = input("Author: ").strip().title()
artist = input("**ENTER to skip or Separate by space** \nArtist: ").strip().title().replace(" ", ", ")
publisher = input("Publisher: ")

length, width = input("Size (separated by space in mm): ").split()
length = length*0.03937008
width = width*0.03937008
size = length + "*" + width +"in"

plot = input("Plot: ")

num_of_vol = input("How many volumes? ")
print("Enter details for each volume")
vol_detail = []

package = ""
package_list = []
package_bigcommerce = """<p><span style="color: #ff0000; background-color: #ffff00; font-family: arial, helvetica, sans-serif; font-size: 14pt;"><strong>&nbsp;"""
package_ebay = ""
package_walmart = ""

for x in range(num_of_vol):
    print(f"Volume {x}")
    release_date = input("Date: ")
    page = input("Page: ")
    upc = input("UPC: ")
    vol_detail.append([release_date, page, upc])

    if edition == "":
        
        while package != "":
            print("**ENTER to end** put 'fpl' in front if First Press Limited")
            package = input("Included: ")
            if "Fpl" in package: 
                package = package.replace("Fpl", "First Press Limited")
            num = input("**ENTER if 1** How many? ")

            package_list.append([package, num])

        package_bigcommerce += f"Vol. {x} : "
        last = package_list[-1]
        for package, num in package_list:
            if num != "":
                package_bigcommerce += f"{package} ({num})"
            else: 
                package_bigcommerce += f"{package}"
            
            if [package, num] != last:
                package_bigcommerce += " + "
            else:
                package_bigcommerce += "</strong></span></p>"



if edition != "":
    package_bigcommerce = """<p style="box-sizing: border-box; color: #ffffff; font-family: Karla, Arial, Helvetica, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; line-height: 200%; margin: 0in; padding: 0px; background: white;"><strong><span style="font-family: Arial; font-weight: bold; font-size: 14pt; background-color: #000000; background-position: 0 0;">&nbsp;On Package </span></strong> <strong style="box-sizing: border-box; font-weight: bold; line-height: inherit;"> <span style="box-sizing: border-box; font-size: 14pt; line-height: 28px; font-family: Arial; background-color: #000000;"> :&nbsp;</span></strong></p>"""
    while package != "":
        print("**ENTER to end** put 'fpl' in front if First Press Limited")
        package = input("Included: ").title()
        if "Fpl" in package: 
            package = package.replace("Fpl", "First Press Limited")
        num = input("**ENTER if 1** How many? ")
        
        package_bigcommerce += """<p style="box-sizing: border-box; font-family: Arial; font-size: 14pt; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; text-indent: -0.25in; line-height: 150%; padding: 0px; background-image: white; background-repeat: repeat; background-attachment: scroll; margin: 0in 0in 0in 0.5in;">✔ """
        package_bigcommerce += package
        if num != "":
            package_bigcommerce += f" ({num})</p>"





def bigCommerce(package_bigcommerce, vol_detail, size, ):
    description = f"""
        {package_bigcommerce}
        <br><br><br>
        <p dir="ltr" style="line-height: 150%;"><strong><span style="color: #ff0000; font-family: Arial; font-size: 14pt;">Webtoon</span><span style="font-family: Arial; font-size: large;"><span style="font-size: 14pt;"> [ {title} ] {edition}</span></span></strong></p>
        <br>
        <p style="line-height: 150%;" align="justify">
        <span style="font-size: 12pt; font-family: Arial;">
        """
    if len(vol_detail) > 1: 
        first_date = vol_detail[0][0]
        first_date = f"20{'.'.join(first_date[i:i+2] for i in range(0, len(first_date), 2))}"
        last_date = vol_detail[-1][0]
        last_date = f"20{'.'.join(last_date[i:i+2] for i in range(0, len(last_date), 2))}"

        description += f"""
        <span style="color: #0000ff;">■</span> Release Date : {first_date} ~ {last_date}<br>
        <span style="color: #0000ff;">■</span> Page &amp; Size : <i>see Table of Contents</i> | {size}<br>
        <br />
        """
    else:
        description += f"""
        <span style="color: #0000ff;">■</span> Release Date : {vol_detail[0][0]}<br>
        <span style="color: #0000ff;">■</span> Page &amp; Size : {vol_detail[0][1]} | {size}<br>
        <br />
        """
    description += f"""
        <span style="color: #0000ff;">■</span> Author : {author}<br>
        <span style="color: #0000ff;">■</span> Artist : {artist}<br>
        <span style="color: #0000ff;">■</span> Publisher : {publisher}
        </span></p>

        <p style="line-height: 150%;" align="justify">
        <span style="font-family: Arial; font-size: 12pt;">
        <span style="color: #0000ff;"><strong>■ Details</strong></span><br><br>
        Korean Title : {kor_title}<br>
        English Title : {title}
        </span></p>
        <p style="line-height: 150%;" align="justify"><span style="color: #ff0000; font-family: Arial; font-size: 12pt;"><strong>This book is written in Korean.</strong></span></p>
        <br><br>

        <p style="line-height: 150%;" align="justify"><span style="font-family: Arial; font-size: 12pt;"> 
        <span style="color: #0000ff;"><strong>■ Synopsis / Plot</strong></span><br><br>
        {plot}
        </span></p>
        <br><br><br><br>

        <p style="line-height: 150%;" align="justify">
        <span style="font-family: Arial; font-size: 12pt;">
        <span style="color: #0000ff;”><strong>■ Table of Contents</strong></span></span></p>

        """
    
    for detail in vol_detail:
        vol = vol_detail.index(detail)
        release_date, page, upc = detail

        description += f"""
            <p style="line-height: 150%;" align="justify">
            <span style="font-family: Arial; font-size: 12pt;">
            <strong> Vol. {vol} </strong><br>
            ISBN: {upc} | {page}p
            </span></p>
        """

    wt_bigcommerce.write(description)
   










wt_bigcommerce.close()
wt_ebay.close()
wt_walmart.close()
wt_amazon.close()
webbrowser.open('wt_bigcommerce.txt')
webbrowser.open('wt_ebay.txt')
webbrowser.open('wt_walmart.txt')
webbrowser.open('wt_amazon.txt')