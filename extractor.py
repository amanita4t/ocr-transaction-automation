def separate(words, start, end):
    start_index = words.index(start) + 1
    end_index = words.index(end)
    return words[start_index:end_index]


def extract_transaction_data(text):
    words = text.split(" ")
    words = [sub for word in words for sub in word.replace("-", " ").replace(".", " ").split()]

    date = separate(words, "on", "transaction")[:1]
    sender = separate(words, "from", "for")
    receiver = separate(words, "for", "transaction")[:3]
    transaction_id = separate(words, "transaction", "Total")[0]
    amount = separate(words, "Amount", "commission")[1:3]

    return {
        "Sender": " ".join(sender),
        "Receiver": " ".join(receiver),
        "Transaction ID": transaction_id,
        "Amount": " ".join(amount),
        "Date": " ".join(date)
    }
