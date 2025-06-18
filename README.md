# Date & Utility Functions in Python

## 📦 Overview of Functions

### 1. `get_days_from_today(date: str) -> int`

Calculates the number of days between today and a given date.

- **Input:** A string in `"YYYY-MM-DD"` format.
- **Output:** Integer number of days (can be negative if the date is in the future).

### 2. `get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list`

Generates a sorted list of unique random numbers within a specified range.

- **Input:**
  - `min_num` – minimum value (≥1)
  - `max_num` – maximum value (≤1000)
  - `quantity` – number of unique values to generate
- **Output:** Sorted list of integers or an empty list if validation fails.

### 3. `normalize_phone(phone_number: str) -> str`

Normalizes a phone number to Ukrainian format `+380XXXXXXXXX`.

- **Input:** Raw phone number string (may include spaces, parentheses, etc.)
- **Output:** Cleaned phone number or `None` if invalid.

### 4. `get_upcoming_birthdays(users: list[dict]) -> list[dict]`

Finds users who have birthdays in the next 7 days (including today). If a birthday falls on a weekend, the greeting is moved to the following Monday.

- **Input:** List of user dictionaries:  
  Example:
  ```python
  [
      {"name": "Alice", "birthday": "1990.06.21"},
      {"name": "Bob", "birthday": "1985.06.25"}
  ]
  ```
