
from estate_flow import registry

from estate_flow.database import load_data, save_data
from estate_flow.dues import (
    MONTHLY_DUES,
    record_dues,
    get_payment_history,
    get_outstanding_residents,
    get_paid_up_residents
)
from estate_flow.activity import log_activity


def show_menu():
    """Display the main menu."""

    print("\n" + "=" * 45)
    print("        ESTATE RESIDENTS' PORTAL")
    print("=" * 45)
    print("1. Register resident")
    print("2. View resident directory")
    print("3. Record monthly dues")
    print("4. View resident statement")
    print("5. Check outstanding dues")
    print("6. Check paid-up residents")
    print("7. Exit")
    print("=" * 45)


def register_resident_menu(data):
    """Handle resident registration."""

    print("\n--- Register Resident ---")

    name = input("Enter resident name: ")
    phone = input("Enter phone number: ")

    success, result = registry.register_resident(
        data,
        name,
        phone
    )

    if success:
        save_data(data)

        log_activity(
            f"RESIDENT REGISTERED | ID={result} | Name={name.strip()}"
        )

        print(f"\nResident registered successfully.")
        print(f"Resident ID: {result}")

    else:
        print(f"\nError: {result}")


def show_residents(data):
    """Display all registered residents."""

    residents = registry.get_all_residents(data)

    print("\n--- Resident Directory ---")

    if not residents:
        print("No residents have been registered yet.")
        return

    for resident_id, resident in residents.items():
        print(
            f"{resident_id} | "
            f"{resident['name']} | "
            f"{resident['phone']}"
        )


def record_payment_menu(data):
    """Handle dues payment."""

    print("\n--- Record Monthly Dues ---")

    resident_id = input("Enter resident ID: ")
    month = input("Enter month: ")

    amount_input = input("Enter amount paid: ")

    try:
        amount = float(amount_input)
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    success, result = record_dues(
        data,
        resident_id,
        month,
        amount
    )

    if not success:
        print(f"\nError: {result}")
        return

    save_data(data)

    log_activity(
        f"DUES PAYMENT | "
        f"ID={result['resident_id']} | "
        f"Month={result['month']} | "
        f"Amount=₦{result['amount']:,.2f}"
    )

    print("\nPayment recorded successfully.")
    print(f"Resident: {result['resident_id']}")
    print(f"Month: {result['month']}")
    print(f"Amount: ₦{result['amount']:,.2f}")
    print(f"Date: {result['date']}")


def show_statement(data):
    """Display a resident's payment history."""

    print("\n--- Resident Statement ---")

    resident_id = input("Enter resident ID: ").strip().upper()

    resident = registry.find_resident(data, resident_id)

    if resident is None:
        print("Resident ID does not exist.")
        return

    history = get_payment_history(data, resident_id)

    print(f"\nResident: {resident['name']}")
    print(f"ID: {resident_id}")
    print(f"Phone: {resident['phone']}")

    print("\nPayment History")
    print("-" * 55)

    if not history:
        print("No payments recorded.")
        return

    for payment in history:
        print(
            f"{payment['month']:<12} "
            f"₦{payment['amount']:>10,.2f}   "
            f"{payment['date']}"
        )


def show_outstanding(data):
    """Display residents who owe dues."""

    print("\n--- Outstanding Dues ---")

    month = input("Enter month: ")

    outstanding = get_outstanding_residents(
        data,
        month
    )

    if not outstanding:
        print("No residents have outstanding dues for this month.")
        return

    print(f"\nOutstanding dues for {month.capitalize()}")
    print("-" * 45)

    for person in outstanding:
        print(
            f"{person['resident_id']} | "
            f"{person['name']} | "
            f"Owes ₦{person['amount_owed']:,.2f}"
        )


def show_paid_up(data):
    """Display residents who are up to date."""

    print("\n--- Paid-Up Residents ---")

    month = input("Enter month: ")

    paid_up = get_paid_up_residents(
        data,
        month
    )

    if not paid_up:
        print("No residents are fully paid up for this month.")
        return

    print(f"\nPaid-up residents for {month.capitalize()}")
    print("-" * 45)

    for person in paid_up:
        print(
            f"{person['resident_id']} | "
            f"{person['name']}"
        )


def main():
    """Run the Estate Union Dues Tracker."""

    data = load_data()

    print("\nWelcome to the Estate Residents' Portal.")
    print(f"Monthly dues: ₦{MONTHLY_DUES:,.2f}")

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_resident_menu(data)

        elif choice == "2":
            show_residents(data)

        elif choice == "3":
            record_payment_menu(data)

        elif choice == "4":
            show_statement(data)

        elif choice == "5":
            show_outstanding(data)

        elif choice == "6":
            show_paid_up(data)

        elif choice == "7":
            print("\nThank you for using the Estate Residents' Portal.")
            break

        else:
            print("\nInvalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
