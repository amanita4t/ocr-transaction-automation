from sheets import get_sheet, save_transaction
from auth import user_access
from ocr_processor import run_ocr
from extractor import extract_transaction_data
from validation import is_transaction_valid

IMAGE_PATH = "Image path"


def main():
    sheet = get_sheet()
    user = user_access(sheet)

    text = run_ocr(IMAGE_PATH)
    data = extract_transaction_data(text)

    if is_transaction_valid(sheet, data["Transaction ID"]):
        save_transaction(sheet, user, data)
        print("Transaction saved successfully.")
    else:
        print("Duplicate transaction detected.")


if __name__ == "__main__":
    main()
