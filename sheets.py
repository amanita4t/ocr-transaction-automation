import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = "json_file"
SCOPES = ["scopes"]
SHEET_URL = "master sheet url"


def get_sheet():
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(SHEET_URL)

    if "user credentials" not in [ws.title for ws in sheet.worksheets()]:
        ws = sheet.add_worksheet("user credentials", 100, 26)
        ws.insert_row(["Email Address", "Password", "User Name"], 1)

    return sheet


def is_transaction_id_unique(sheet, transaction_id):
    for ws in sheet.worksheets():
        if transaction_id in ws.col_values(3):
            return False
    return True


def save_transaction(sheet, user, data):
    ws = sheet.worksheet(user)

    if ws.get_all_values() == []:
        ws.insert_row(["Sender", "Receiver", "Transaction ID", "Amount", "Date"], 1)

    ws.append_row([
        data["Sender"],
        data["Receiver"],
        data["Transaction ID"],
        data["Amount"],
        data["Date"]
    ])
