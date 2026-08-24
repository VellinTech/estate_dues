
from datetime import datetime


MONTHLY_DUES = 5000


def record_dues(data, resident_id, month, amount):
    """Record monthly dues for a resident."""

    resident_id = resident_id.strip().upper()
    month = month.strip().capitalize()

    if resident_id not in data["residents"]:
        return False, "Resident ID does not exist."

    if not month:
        return False, "Month cannot be empty."

    if amount <= 0:
        return False, "Payment amount must be greater than zero."

    valid_months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if month not in valid_months:
        return False, "Please enter a valid month."

    for payment in data["payments"]:
        if (
            payment["resident_id"] == resident_id
            and payment["month"].lower() == month.lower()
        ):
            return False, f"Payment for {month} has already been recorded."

    payment = {
        "resident_id": resident_id,
        "month": month,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data["payments"].append(payment)

    return True, payment


def get_payment_history(data, resident_id):
    """Return all payments belonging to a resident."""

    resident_id = resident_id.strip().upper()

    if resident_id not in data["residents"]:
        return None

    history = []

    for payment in data["payments"]:
        if payment["resident_id"] == resident_id:
            history.append(payment)

    return history


def get_payment_for_month(data, resident_id, month):
    """Find a resident's payment for a particular month."""

    resident_id = resident_id.strip().upper()
    month = month.strip().lower()

    for payment in data["payments"]:
        if (
            payment["resident_id"] == resident_id
            and payment["month"].lower() == month
        ):
            return payment

    return None


def get_outstanding_residents(data, month):
    """Return residents who still owe for a month."""

    month = month.strip().capitalize()
    outstanding = []

    for resident_id, resident in data["residents"].items():

        payment = get_payment_for_month(
            data,
            resident_id,
            month
        )

        if payment is None:
            amount_owed = MONTHLY_DUES

        elif payment["amount"] < MONTHLY_DUES:
            amount_owed = MONTHLY_DUES - payment["amount"]

        else:
            continue

        outstanding.append({
            "resident_id": resident_id,
            "name": resident["name"],
            "amount_owed": amount_owed
        })

    return outstanding


def get_paid_up_residents(data, month):
    """Return residents who have fully paid their dues."""

    month = month.strip().capitalize()
    paid_up = []

    for resident_id, resident in data["residents"].items():

        payment = get_payment_for_month(
            data,
            resident_id,
            month
        )

        if payment is not None and payment["amount"] >= MONTHLY_DUES:
            paid_up.append({
                "resident_id": resident_id,
                "name": resident["name"]
            })

    return paid_up

