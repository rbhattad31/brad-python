import os
from win32com import client
from os import path
import re
import pandas as pd
from PyPDF2 import PdfFileReader, PdfFileWriter


def extract_paasword(excel_path, sheet, last_digit, column_name):
    df = pd.read_excel(excel_path, sheet_name=sheet, dtype=object)
    password = []
    for index, row in df.iterrows():
        account_number = str(row[column_name])
        digits = account_number[-4:]
        if digits.casefold().__eq__(str(last_digit).casefold()):
            password.insert(0, account_number[:6])
        else:
            pass
    return password


def decrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as input_file, \
            open(output_path, 'wb') as output_file:
        reader = PdfFileReader(input_file)
        reader.decrypt(password)

        writer = PdfFileWriter()
        page_obj = reader.getPage(0)
        pdf_content = page_obj.extractText()
        payment_ref = re.search("(?<=Payment Doc No :)(.(0-9)*)+", pdf_content)
        total_amount = re.search("(?<=INR)(.(0-9)*)+", pdf_content)

        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))

        writer.write(output_file)
        return payment_ref[0], total_amount[0].strip()


def UTR_Process(in_body, output_dir, in_sender_address, accounts_path, accounts_sheet, accounts_col):

    try:
        # Connect to outlook
        outlook = client.Dispatch("Outlook.Application").GetNamespace("MAPI")

        # Connect to folder
        inbox = outlook.GetDefaultFolder(6)

        # Get messages
        messages = inbox.Items

        # Iterate each message
        for message in messages:
            if in_body in message.Body and message.Unread and message.SenderEmailAddress == in_sender_address:
                attachments = message.Attachments
                body = message.Body

                # Create separate folder for each message
                target_folder = path.join(output_dir, "temp")
                if path.exists(target_folder):
                    pass
                else:
                    os.mkdir(target_folder)

                # Extract 4-digit Number
                four_digit = re.search("(?<=XXXXX)(.(0-9)*)+", body)
                four_digit = four_digit[0]
                four_digit = four_digit.replace("X", "").replace(".", "").strip()

                # Extract Password
                password_list = extract_paasword(accounts_path, accounts_sheet, four_digit, accounts_col)

                # Save attachments
                for attachment in attachments:
                    attachment_name = str(attachment).replace("-", "")
                    attachment_Path = path.join(target_folder, attachment_name)
                    attachment.SaveAsFile(attachment_Path)
    except Exception as error:
        print(error)


Body_Content = "Regards"
outputFolder_path = path.join(os.getcwd(), "Output")
SenderAddress = "vinothrit74@gmail.com"
BankAccounts_Path = r"C:\Users\Hi\PycharmProjects\HDFC UTR PROCESS\Input\Vendor bank accounts.XLSX"
BankAccounts_Sheet = "Vendor Bank accounts"
BankAccounts_Col = "Bank Acc. No."
UTR_Process(Body_Content, outputFolder_path, SenderAddress, BankAccounts_Path, BankAccounts_Sheet, BankAccounts_Col)
#print(extract_paasword(BankAccounts_Path, BankAccounts_Sheet, "8912", BankAccounts_Col))
