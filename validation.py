def is_transaction_valid(sheet, transaction_id):
    for ws in sheet.worksheets():
        if transaction_id in ws.col_values(3):
            return False
    return True
