import webbrowser
import string
wt_bc_walmart = open('wt_bc_walmart.txt','w')
wt_ebay = open('wt_ebay.txt','w')
wt_amazon = open('wt_amazon.txt','w')


# basic input
sku = input("SKU: ").strip().upper()
title = string.capwords(input ("Title: ").strip())
kor_title = input("Korean Title: ").strip()
edition = input("\n**Enter Exactly or ENTER to skip** (Vol. # - # special, limited, box set, etc.)\nEdition: ").title()
author = input("\nAuthor: ").strip().title()
artist = input("\n**ENTER to skip or Separate by comma** \nArtist: ").title()
publisher = input("\nPublisher: ").title()

length, width = input("Size (separated by space in mm): ").split()
length = round(float(length)*float(0.03937008), 1)
width = round(float(width)*float(0.03937008), 1)
size = f"{length} * {width} in"

plot = input("Plot: ")


vol_detail = []



packageHTML = ""
package_bigcommerce_ebay_walmart = ""
package_amazon = ""




if edition == "":
    num_of_vol = int(input("\nHow many volumes? "))
    print("Enter details for each volume")
    for x in range(num_of_vol):
        package = "package"
        package_list = []
        print(f"\n\nVolume {x+1}")
        release_date = input("Date: ")
        page = input("Page: ")
        isbn = input("ISBN: ")
        vol_detail.append([release_date, page, isbn])

        package_bigcommerce_ebay_walmart ="""<p><span style="color: #ff0000; background-color: #ffff00; font-family: arial, helvetica, sans-serif; font-size: 14pt;"><strong>"""
        while package != "":
            package = input("\n**ENTER to end**\nAnything Included? ('fpl' for First Press Limited) ")
            if "fpl" in package: 
                package = package.replace("fpl", "First Press Limited")
            num = input("**ENTER if 1** How many? ")

            package_list.append([package, num])
        


        for i, [package,num] in enumerate(package_list):
            if len(package) != 0:
                if i == 0:
                    package_bigcommerce_ebay_walmart += f"&nbsp;Vol. {x+1} : "
                if num != "":
                    package_bigcommerce_ebay_walmart += f"{package.title()} ({num})"
                    package_amazon += f"{package.title()} ({num})"
                else: 
                    package_bigcommerce_ebay_walmart += f"{package.title()} (1)"
                    package_amazon += f"{package.title()} (1)"

                if i < len(package_list)-2: 
                    package_bigcommerce_ebay_walmart += " + "
        package_bigcommerce_ebay_walmart += "</strong></span></p>"

    if package_list != [['','']]:
        packageHTML += package_bigcommerce_ebay_walmart




vol = []
if edition != "":
    for word in edition:
        if word.isdigit() == True:
            vol.append(word)
    
    if len(vol) == 2:
        for x in range(int(vol[0]),int(vol[1])+1):
            package = "package"
            package_list = []
            print(f"\n\nVolume {x}")
            release_date = input("Date: ")
            page = input("Page: ")
            isbn = input("ISBN: ")
            vol_detail.append([release_date, page, isbn])
    else:
        package = "package"
        package_list = []
        print(f"\n\nVolume {int(vol[0])}")
        release_date = input("Date: ")
        page = input("Page: ")
        isbn = input("ISBN: ")
        vol_detail.append([release_date, page, isbn]) 

    package_bigcommerce_ebay_walmart = """<p style="box-sizing: border-box; color: #ffffff; font-family: Karla, Arial, Helvetica, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; line-height: 200%; margin: 0in; padding: 0px; background: white;"><strong><span style="font-family: Arial; font-weight: bold; font-size: 14pt; background-color: #000000; background-position: 0 0;">&nbsp;On Package </span></strong> <strong style="box-sizing: border-box; font-weight: bold; line-height: inherit;"> <span style="box-sizing: border-box; font-size: 14pt; line-height: 28px; font-family: Arial; background-color: #000000;"> :&nbsp;</span></strong></p>"""
    while package != "":
        package = input("\n**ENTER to end**\nOn Package: ('fpl' for First Press Limited) ")
        if "fpl" in package: 
            package = package.replace("fpl", "First Press Limited")
        num = input("**ENTER if 1** How many? ")

        if package != "":
            package_bigcommerce_ebay_walmart += """<p style="box-sizing: border-box; font-family: Arial; font-size: 14pt; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; text-indent: -0.25in; line-height: 150%; padding: 0px; background-image: white; background-repeat: repeat; background-attachment: scroll; margin: 0in 0in 0in 0.5in;">✔ """
            package_bigcommerce_ebay_walmart += package.title()
            package_amazon += f"- {package.title()}"
            if num != "":
                package_bigcommerce_ebay_walmart += f" ({num})</p>"
                package_amazon += f" ({num})</br>"
    packageHTML = package_bigcommerce_ebay_walmart




def bigcommerce_and_walmart(packageHTML, title, kor_title, edition, vol_detail, vol, size, author, artist, publisher, plot):
    description = f"""
        {packageHTML}
        <br><br><br>
        <p dir="ltr" style="line-height: 150%;"><strong><span style="color: #ff0000; font-family: Arial; font-size: 14pt;">Webtoon</span><span style="font-family: Arial; font-size: large;"><span style="font-size: 14pt;"> [ {title} ] {edition}</span></span></strong></p>
        <br>
        <p style="line-height: 150%;" align="justify">
        <span style="font-size: 12pt; font-family: Arial;">
        """
    if len(vol_detail) > 1 and vol_detail[0][0] != vol_detail[1][0]: 
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
        date = vol_detail[0][0]
        tot_page = 0
        for [release_date, page, isbn] in vol_detail:
            tot_page += int(page)
        description += f"""
        <font color="#0000FF">■</font> Release Date : 20{'.'.join(date[i:i+2] for i in range(0, len(date), 2))}<br>
        <font color="#0000FF">■</font> Page &amp; Size : {tot_page}p | {size}<br>
        <br>
        """   
    description += f"""
        <span style="color: #0000ff;">■</span> Author : {author}<br>
        <span style="color: #0000ff;">■</span> Artist : {artist}<br>
        <span style="color: #0000ff;">■</span> Publisher : {publisher}
        </span></p>
        <br><br>

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
        <span style="font-family: Arial; font-size: 12pt; color: #0000ff;"><strong>■ Table of Contents</strong></span></p>

        """
    
    if edition == "":
        for detail in vol_detail:
            v = int(vol_detail.index(detail)) + 1
            release_date, page, isbn = detail

            description += f"""
                <p style="line-height: 150%;" align="justify">
                <span style="font-family: Arial; font-size: 12pt;">
                <strong> Vol. {v} </strong><br>
                ISBN: {isbn} | {page}p
                </span></p>
            """
    else:
        for index, [release_date, page, isbn] in enumerate(vol_detail):
            description += f"""
                <p style="line-height: 150%;" align="justify">
                <span style="font-family: Arial; font-size: 12pt;">
                <strong> Vol. {vol[index]} </strong><br>
                ISBN: {isbn} | {page}p
                </span></p>
            """


    wt_bc_walmart.write(description)
   



def ebay(packageHTML, title, kor_title, sku, vol_detail, vol, size, author, artist, publisher, plot):
    description = f"""
        {packageHTML}
        <h3 dir="ltr" style="line-height: 150%">
        <br>
        <b><font size="4" color="#ff0000">Korean Webtoon</font><font size="4"> [ {title} ] {edition} ({sku})</font>
        </b></h3>

        <p align="justify" style="line-height: 150%">
        <font color="#008000" size="2" face="Arial">Photographs and actual product colors may vary slightly</font></p>

        <p align="justify" style="line-height: 150%">
        <font color="#008000" face="Arial">
        📦 Safely packed with Tracking Number<br>
        ✔ 100% Original Brand New Product<br>
        ★This book is written in Korean
        </font></p>
        
        <br><br>

        <p align="justify" style="line-height: 150%">
        <font face="Arial">
        <font color="#0000FF">■</font> Type : Manhwa / Webtoon<br>
        <br>

        """
    
    
    if len(vol_detail) > 1 and vol_detail[0][0] != vol_detail[1][0]: 
        first_date = vol_detail[0][0]
        first_date = f"20{'.'.join(first_date[i:i+2] for i in range(0, len(first_date), 2))}"
        last_date = vol_detail[-1][0]
        last_date = f"20{'.'.join(last_date[i:i+2] for i in range(0, len(last_date), 2))}"

        description += f"""
        <font color="#0000FF">■</font> Release Date : {first_date} ~ {last_date}<br>
        <font color="#0000FF">■</font> Page &amp; Size : <i>see Table of Contents</i> | {size}<br>
        <br>
        """
    else:
        date = vol_detail[0][0]
        tot_page = 0
        for [release_date, page, isbn] in vol_detail:
            tot_page += int(page)
        description += f"""
        <font color="#0000FF">■</font> Release Date : 20{'.'.join(date[i:i+2] for i in range(0, len(date), 2))}<br>
        <font color="#0000FF">■</font> Page &amp; Size : {tot_page}p | {size}<br>
        <br>
        """    


    description += f"""
        <font color="#0000FF">■</font> Author : {author}<br>
        <font color="#0000FF">■</font> Artist : {artist}<br>
        <font color="#0000FF">■</font> Publisher : {publisher}<br>
        <font color="#0000FF">■</font> Country of Origin : South Korea <br>
        <br>
        <font color="#0000FF">■</font> KJCstar ID : {sku} 
        </font></p>

        <br><br>

        <p align="justify" style="line-height: 150%">
        <font face="Arial">
        <font color="#0000FF"><b>■ Details</b></font><br>
        <br>
        Korean Title : {kor_title}<br>
        English Title : {title}
        </font></p>

        <p align="justify" style="line-height: 150%">
        <font color="#FF0000" face="Arial"><b>This book is written in Korean.</b></font></p>
        <br><br>

        <p align="justify" style="line-height: 150%">
        <font face="Arial">
        <font color="#0000FF"><b>■ Synopsis / Plot</b></font>
        </font></p>

        <p style="background-repeat:repeat; background-attachment:scroll; line-height:150%">
        <font face="Arial">
        {plot}
        </font></p>
        <br><br><br>


        <p align="justify" style="line-height: 150%">
        <font color="#0000FF" face="Arial"><b>■ Table of Contents</b></font></p>

        """
    
    if edition == "":
        for detail in vol_detail:
            v = int(vol_detail.index(detail)) + 1
            release_date, page, isbn = detail

            description += f"""
                <p style="line-height: 150%;" align="justify">
                <span style="font-family: Arial; font-size: 12pt;">
                <strong> Vol. {v} </strong><br>
                ISBN: {isbn} | {page}p
                </span></p>
            """
    else:
        for index, [release_date, page, isbn] in enumerate(vol_detail):
            description += f"""
                <p style="line-height: 150%;" align="justify">
                <span style="font-family: Arial; font-size: 12pt;">
                <strong> Vol. {vol[index]} </strong><br>
                ISBN: {isbn} | {page}p
                </span></p>
            """




    description += f"""
        <br><br><br><br><br><br>

        <table border="0" cellpadding="10px" style="border-collapse: collapse" bordercolor="#ffffff" width="800px" height="836">
        <tbody><tr>
            <td height="20" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF" bgcolor="#6767FF">
            <p style="line-height: 150%">
            <b><font face="Arial">
            <font color="#FFFFFF">PRODUCT GUARANTEE</font></font></b></p></td>
        </tr>
        <tr>
            <td height="19" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF">
            <p style="line-height: 150%">
            <font face="Arial"><b>We guarantee all our items are 100% original. If you are not satisfied with our items, Please contact us!
            </b> </font></p></td>
        </tr>
        <tr>
            <td height="20" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF" bgcolor="#6767FF">
            <p style="line-height: 150%">
            <b><font face="Arial">
            <font color="#FFFFFF">SHIPPING</font></font></b></p></td>
        </tr>
        <tr>
            <td height="133" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF">
            <p style="line-height: 150%">
            <b><font face="Arial"><font color="#FF0000">All orders from the U.S. will be shipped from our US office via USPS with tracking number (exceptions may occur, we will notify you prior shipping or specify in item description).</font><br>
            
            <font color="#0000FF">Sorry, we currently do not offer International Shipping due to increase of shipping cost (except Canada). Buyers who wish to purchase our merchandise outside of the U.S. may choose to use desired shipping forwarder company. If you choose to use a shipping forwarder company, we are not responsible for any damage or loss after the package is safely delivered to the forwarding company. Also, we are not responsible for Buyer's Customs charges.</font><br>
            
            <font color="#000000">
            We ship within 1 to 5 business days  except holiday. Transit times may vary particularly during peak periods.</font></font></b></p></td>
        </tr>
        <tr>
            <td height="20" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF" bgcolor="#6767FF">
            <p style="line-height: 150%">
            <b><font face="Arial">
            <font color="#FFFFFF">ESTIMATED DELIVERY TIME</font></font></b></p></td>
        </tr>
        <tr>
            <td height="55" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF">
            <p style="line-height: 150%">
            <b><font face="Arial">US Standard : 4 - 14 business days via USPS First Class/Media/Parcel<br>
            US Expedited : 2 - 4 business days via USPS Priority<br>
            Canada : 15 - 25 business days</font></b></p></td>
        </tr>
        <tr>
            <td height="20" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF" bgcolor="#6767FF">
            <p style="line-height: 150%">
            <b><font face="Arial">
            <font color="#FFFFFF">SHIPPING &amp; HANDLING CHARGE</font></font></b></p></td>
        </tr>
        <tr>
            <td height="19" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF">
            <p style="line-height: 150%">
            <b><font face="Arial">No handling charge. <font color="#FF0000">
            Tracking number will be provided on all orders.</font></font></b></p></td></tr>
        <tr>
            <td height="20" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF" bgcolor="#6767FF">
            <p style="line-height: 150%">
            <b><font face="Arial">
            <font color="#FFFFFF">COMBINED SHIPPING</font></font></b></p></td>
        </tr>
        <tr>
            <td height="38" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF">
            <p style="line-height: 150%">
            <b><font face="Arial">We always do combine shipping.<br>
            The highest shipping costs and each additional costs will be calculated as a total shipping fee.</font></b></p></td>
        </tr>
        <tr>
            <td height="20" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF" bgcolor="#6767FF">
            <p style="line-height: 150%">
            <b><font face="Arial">
            <font color="#FFFFFF">CUSTOMS</font></font></b></p></td>
        </tr>
        <tr>
            <td height="38" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF">
            <p style="line-height: 150%">
            <b><font face="Arial">We do not hold any liability on any issues relating to CUSTOMS including but not limited to delays and taxation. Please check with your country's Customs Office to determine the additional cost and policy.</font></b></p></td>
        </tr>
        <tr>
            <td height="20" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF" bgcolor="#6767FF">
            <p style="line-height: 150%">
            <b><font color="#FFFFFF" face="Arial">RETURN POLICY</font></b></p></td>
        </tr>  
        <tr>
            <td height="114" bordercolorlight="#FFFFFF" bordercolordark="#FFFFFF">
            <p style="line-height: 150%">
            <b><font face="Arial">We accept return request for buyer's any reason, but the item must be sealed, unused, and in original condition. Return request must be made within 14 days of item delivery. If the returning item has been opened or used, the return request will not be accepted.<br>
            Refund will be issued after arrival and inspection of the returning item. Shipping is NOT REFUNDABLE.<br>
            If you received wrong item, please let us know to resolve problem. We will exchange to correct item upon receiving wrong item in unopened, in original condition (We will pay return shipping).</font></b></p></td>
        </tr>
        </tbody></table>

    """

    wt_ebay.write(description)



def amazon(title, kor_title, size, sku, plot, edition, vol_detail, vol, package_amazon):

    def regular_HTML(v, p, c):
        description = f"""
        Korean Webtoon [{title}] Vol. {v}<br>
        <br>
        ■ Korean Title : {kor_title}<br>
        """
        if c.isdigit() == True:
            select = ""
            for x in range(c):
                select += f"{x} / "
            description += f"■ Select : {select}Set <br>"
        
        description += f"""
            ■ Page & Size : {p}p | {size} <br>
            ■ KJCstar Product ID : {sku}<br>
            <br>
            ★This book is written in Korean<br>
            ✔ 100% Original Brand New Product<br>
            📦 Safely packed with Tracking Number<br>
            <br>
            <b>Vol. {v}</b> Episode  ~ <br>
            <br>
            ■ Synopsis / Plot<br>
            {plot}
            <br><br>
        """

        return(description)
    

    def special_HTML(vol,tot_page, package_amazon):
        description = f"""
            Korean Webtoon [{title}] {edition}<br>
            <br>
            ■ Korean Title : {kor_title}<br>
            ■ Page & Size : {tot_page}p | {size} <br>
            ■ KJCstar Product ID : {sku}<br>
            <br>
            ★This book is written in Korean<br>
            ✔ 100% Original Brand New Product<br>
            📦 Safely packed with Tracking Number<br>
            <br>
        """

        for v in vol:
            description += f"""
            <b>Vol. {v}</b> Episode  ~ <br>
            """

        description += f"""
            <br>
            ■ On Package<br>
            {package_amazon}
            <br><br>
        """

       


        return(description)




    if edition == "":
        isCompleted = input("\nCompleted Series? (Total # of volumes for yes, ENTER for no) ")
        for detail in vol_detail:
            v = int(vol_detail.index(detail)) + 1
            release_date, p, isbn = detail
            wt_amazon.write(regular_HTML(v, p, c))

    else:
        tot_page = 0
        for [release_date, page, isbn] in vol_detail:
            tot_page += int(page)
        wt_amazon.write(special_HTML(vol, tot_page, package_amazon))





    
  


bigcommerce_and_walmart(package_bigcommerce_ebay_walmart, title, kor_title, edition, vol_detail, vol, size, author, artist, publisher, plot)
ebay(packageHTML, title, kor_title, sku, vol_detail, vol, size, author, artist, publisher, plot)
amazon(title, kor_title, size, sku, plot, edition, vol_detail, vol, package_amazon)


wt_bc_walmart.close()
wt_ebay.close()
wt_amazon.close()
webbrowser.open('wt_bc_walmart.txt')
webbrowser.open('wt_ebay.txt')
webbrowser.open('wt_amazon.txt')