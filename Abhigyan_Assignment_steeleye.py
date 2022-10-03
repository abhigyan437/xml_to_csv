import pandas as pd
import unittest
import logging

def file_reading():
    """In this Function we are just reading the XML File which we have extracted from the Zipped Folder"""
    file_name = 'DLTINS_20210117_01of01.xml'
    try:
        with open(file_name,'r', encoding="utf-8") as file:
            file_text = file.read()
        return file_text
    except:
        logging.error('The Concerned File is not Found')

def xml_to_csv(file_text):
    """This function will convert the XML Content to CSV File, with comma Delimited & uisng Pandas Module
    will create the CSV File"""
    list_id = []
    list_name = []
    list_fn = []
    list_ind = []
    list_ccy = []
    list_issr = []
    main_tag_split = file_text.split('<FinInstrmGnlAttrbts>')
    count = 1
    try:
        while count < len(main_tag_split):
            main_text = main_tag_split[count]
            split1 = (main_text.split('<Id>'))[1]
            split10 = (split1.split('</Id>'))[0]
            list_id.append(split10)
            split1 = (main_text.split('<FullNm>'))[1]
            split10 = (split1.split('</FullNm>'))[0]
            list_name.append(split10)
            split1 = (main_text.split('<ClssfctnTp>'))[1]
            split10 = (split1.split('</ClssfctnTp>'))[0]
            list_fn.append(split10)
            split1 = (main_text.split('<CmmdtyDerivInd>'))[1]
            split10 = (split1.split('</CmmdtyDerivInd>'))[0]
            list_ind.append(split10)
            split1 = (main_text.split('<NtnlCcy>'))[1]
            split10 = (split1.split('</NtnlCcy>'))[0]
            list_ccy.append(split10)
            split1 = (main_text.split('<Issr>'))[1]
            split10 = (split1.split('</Issr>'))[0]
            list_issr.append(split10)
            count += 1
    except:
        logging.critical('XML FIle is not read Properly')
    try:
        data = pd.DataFrame()
        data['FinInstrmGnlAttrbts.Id'] = list_id
        data['FinInstrmGnlAttrbts.FullNm'] = list_name
        data['FinInstrmGnlAttrbts.ClssfctnTp'] = list_fn
        data['FinInstrmGnlAttrbts.CmmdtyDerivInd'] = list_ind
        data['FinInstrmGnlAttrbts.NtnlCcy'] = list_ccy
        data['Issr'] = list_issr
        data.to_csv('output1.csv')
    except:
        logging.error("CSV File can't be created")


file_text = file_reading()
xml_to_csv(file_text)


