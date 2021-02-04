# ABBODA
ABB ODA Data export tool

## How to make a ODBC connection for 800xA IM Server

# setp1:
a) configurateion wizard > system administrator > system extension load
b) Load >> ABB inform IT ODA 5.1-033

# step2:
a) start > abb industiral IT 800xA > information Mgmt > ABB open access to 800xA > managment console

b) ABB 800xA connect >> ABBODA >> manager(localhost) >> connected to ABB_ODA_AGENT
                     >> services >> sql engine parameters >> service sqldiskcachmaxsize(defalt:2000) >> 10000000
