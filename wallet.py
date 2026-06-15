import logging
import re

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def deposit(balance, amount):
    if amount <= 0:
        raise ValueError(f"InvalidAmountError: Attempted to process {amount} VND.")
    
    balance += amount
    logging.info(f"Deposit successful: +{amount} VND. Current Balance: {balance}")
    return balance

def transfer(balance, phone, amount):
    if amount <= 0:
        raise ValueError(f"InvalidAmountError: Attempted to process {amount} VND.")
    
    if amount > balance:
        raise ValueError(f"InsufficientBalanceError: Attempted to transfer {amount} VND with balance {balance} VND.")
    
    if amount >= 10000000:
        logging.warning(f"High value transaction detected: {amount} VND to {phone}")
    
    balance -= amount
    logging.info(f"Transfer successful: -{amount} VND to {phone}. Current Balance: {balance}")
    return balance

def show_balance(balance):
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {balance:,} VND")
    logging.info(f"Balance checked. Current Balance: {balance}")

def input_amount(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error("ValueError: Invalid numeric input.")

def input_phone():
    while True:
        phone = input("Nhập số điện thoại người nhận: ")
        if re.fullmatch(r"\d{10}", phone):
            return phone
        print("Số điện thoại phải gồm 10 chữ số.")

def display_menu():
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("=====================================")

def main():
    balance = 0

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                print("\n--- NẠP TIỀN VÀO VÍ ---")
                try:
                    amount = input_amount("Nhập số tiền cần nạp: ")
                    balance = deposit(balance, amount)
                    print(f"\nNạp tiền thành công: +{amount:,} VND")
                    print(f"Số dư hiện tại: {balance:,} VND")
                except ValueError as err:
                    print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                    logging.error(err)

            case "2":
                print("\n--- CHUYỂN TIỀN ---")
                try:
                    phone = input_phone()
                    amount = input_amount("Nhập số tiền cần chuyển: ")
                    balance = transfer(balance, phone, amount)
                    print(f"\nChuyển tiền thành công tới số điện thoại {phone}")
                    print(f"Số tiền đã chuyển: {amount:,} VND")
                    print(f"Số dư còn lại: {balance:,} VND")
                except ValueError as err:
                    error_message = str(err)
                    if "InsufficientBalanceError" in error_message:
                        print("\nGiao dịch thất bại: Số dư của bạn không đủ.")
                        print(f"Số dư hiện tại: {balance:,} VND")
                    else:
                        print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                    logging.error(err)

            case "3":
                show_balance(balance)

            case "4":
                logging.info("System shutdown")
                print("\nCảm ơn bạn đã sử dụng dịch vụ.")
                break

            case _:
                print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()