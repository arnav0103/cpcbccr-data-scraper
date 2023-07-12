[33mcommit dba37dffff16fbadc9580c8b27555dec5f6f1a3d[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m)[m
Author: Ruchika Gupta <ruchika.gupta_1@nxp.com>
Date:   Wed Jul 12 22:14:20 2023 +0530

    Misc station sites
    
    - Maharashtra - few sites and Mumbai
    - Andhra Pradesh
    - Tamil Nadu - chennai
    etc
    
    Signed-off-by: Ruchika Gupta <ruchika.gupta_1@nxp.com>

[33mcommit 1a91dbff89b02a464ffcb4f4df2baeda11a1c2d1[m
Author: Ruchika Gupta <ruchika.gupta_1@nxp.com>
Date:   Wed Jul 12 22:13:01 2023 +0530

    Sites xls files added for different states
    
    - delhi, haryana, uttar pradesh, rajasthan and karnataka
    
    Signed-off-by: Ruchika Gupta <ruchika.gupta_1@nxp.com>

[33mcommit 12aa8f37502fbb24c29f0d745d75e69a0f397a8a[m
Author: Ruchika Gupta <ruchika.gupta_1@nxp.com>
Date:   Wed Jul 12 22:10:39 2023 +0530

    setup_pull.py modified to fetch yearly summayry data
    
    --> Change from to date based on years you want to use
    --> Different xls available for UP,rajasthan. Use them as required.
    
    Signed-off-by: Ruchika Gupta <ruchika.gupta_1@nxp.com>

[33mcommit d63589f6a4b2f060478dcfdeb3172ed81f5a5b5c[m
Author: Ruchika Gupta <ruchika.gupta_1@nxp.com>
Date:   Wed Jul 12 22:08:25 2023 +0530

    Create a copy of pull.py
    
    - Copy created as pull_wo_try.py
    - Major changes

[33mcommit 5307b3842a2ff3bf18521339e8796e702aaac6fa[m
Author: Ruchika Gupta <ruchika.gupta_1@nxp.com>
Date:   Wed Jul 12 22:05:05 2023 +0530

    Changes in get_availability to fetch the data in July 2023
    
    - the CPCB website has a Captcha provision now, so cookie needs to be
    added in header to prevent error "unauthorized access"
    { Note the cookie needs to be changed if error timeout start coming from
    website }
    - Direct .json doesn't work on the response. So decode data to base64
    and then add in json.dumps
    
    Signed-off-by: Ruchika Gupta <ruchika.gupta_1@nxp.com>

[33mcommit b0d7fff8bd963c7c4084056adce0d629f993699c[m
Author: Ruchika Gupta <ruchika.gupta_1@nxp.com>
Date:   Wed Jul 12 22:17:03 2023 +0530

    Revert "Delhi date fetched for Year assesment"
    
    This reverts commit 0a82cdaa080f780b6df91882e39f29e4c7a702f8.

[33mcommit 0a82cdaa080f780b6df91882e39f29e4c7a702f8[m[33m ([m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: arnav0103 <66205884+arnav0103@users.noreply.github.com>
Date:   Wed Jul 12 07:39:59 2023 +0530

    Delhi date fetched for Year assesment
    
    - Data fetched on 11-July-2023
    - Changes to add cookie as site expects captcha now
    - Misc debug changes to be cleaned
    - Output received needs to be decoded.

[33mcommit 79771c6119d21974ce38d675cacfd9c31ea5e475[m
Author: Gurjot Sidhu <stuff@thatgurjot.com>
Date:   Wed Jun 15 03:51:46 2022 +0530

    fix link

[33mcommit 3d91b98df426d61bab89b36a08b919c11729d27b[m
Author: Gurjot Sidhu <stuff@thatgurjot.com>
Date:   Wed Jun 15 03:49:31 2022 +0530

    initialise

[33mcommit c483d16d0e016fb5c65e74418436453117a299e3[m
Author: Gurjot Sidhu <stuff@thatgurjot.com>
Date:   Wed Jun 15 03:47:23 2022 +0530

    Initial commit
