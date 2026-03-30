"""
NEW SYNTAX REFERENCE — JS vs PYTHON (Exceptions)

JavaScript (try/catch/finally):
--------------------------------
try {
  // risky code
} catch (err) {
  // handle error
} finally {
  // always runs
}

throw new Error("message");


Python (try/except/else/finally):
---------------------------------
try:
    # risky code
except SomeError as e:
    # handle error
else:
    # runs ONLY if no exception was raised in try
finally:
    # always runs, whether there was an exception or not

raise ValueError("message")         # raising a built-in exception
raise CustomError("message")        # raising a custom exception class

# Accessing exception object:
try:
    ...
except Exception as e:
    # use e to inspect error details

# Assertions:
assert condition, "message if condition is False"

"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import numbers, products, users

os.system("cls")


# 1. Basic try/except around integer division (handle ZeroDivisionError)
#
#   def safe_divide(a, b):
#       try:
#           ...attempt integer division a // b...
#       except ZeroDivisionError as e:
#           ...return a clear message that division by zero is not allowed...
#       return result_or_message
#
#   call:   safe_divide(10, 0)
#   output: "Cannot divide by zero"
def safe_divide(a, b):
    try:
        result = a // b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    return result


print(safe_divide(10, 0))


# 2. Basic try/except converting string to int (handle ValueError)
#
#   def parse_int(value):
#       try:
#           ...attempt to convert value to an integer...
#       except ValueError as e:
#           ...return a message that the string is not a valid integer...
#       return parsed_or_message
#
#   call:   parse_int("abc")
#   output: "Invalid integer: abc"
def parse_int(value):
    try:
        result = int(value)
    except ValueError:
        return f"Invalid integer: {value}"
    return result


print(parse_int("abc"))


# 3. Basic try/except for list indexing (handle IndexError)
#
#   def get_number_at(index):
#       try:
#           ...attempt to get numbers[index] from the imported numbers list...
#       except IndexError as e:
#           ...return a message that the index is out of range...
#       return value_or_message
#
#   call:   get_number_at(999)
#   output: "Index 999 is out of range"
def get_number_at(index):
    try:
        return numbers[index]
    except IndexError:
        return "Index out of range"


print(get_number_at(999))


# 4. Basic try/except for dict key access (handle KeyError)
#
#   def get_user_name(user_dict):
#       try:
#           ...attempt to access the 'name' key from user_dict...
#       except KeyError as e:
#           ...return a message that the key is missing...
#       return name_or_message
#
#   call:   get_user_name({})
#   output: "Missing key: name"
def get_user_name(user_dict):
    try:
        return user_dict["name"]
    except KeyError:
        return "Missing key"


print(get_user_name({}))


# 5. Basic try/except for unsupported addition (handle TypeError)
#
#   def add_values(a, b):
#       try:
#           ...attempt to add a and b together...
#       except TypeError as e:
#           ...return a message that these types cannot be added...
#       return sum_or_message
#
#   call:   add_values("10", 5)
#   output: "Cannot add str and int"
def add_values(a, b):
    try:
        return a + b
    except TypeError:
        return f"Cannot add {(type(a))} and {type(b)}"


print(add_values("10", 5))


# 6. try/except with generic Exception catch-all
#
#   def risky_operation(x):
#       try:
#           ...perform some arithmetic that might raise different exceptions...
#       except Exception as e:
#           ...return a generic error message including the exception text...
#       return result_or_error
#
#   call:   risky_operation(0)
#   output: "Error occurred: division by zero"
def risky_operation(x):
    try:
        return 5 // x
    except Exception as e:
        return f"Error occured: {e}"


print(risky_operation(0))


# 7. try/except that returns None on failure
#
#   def safe_int(value):
#       try:
#           ...attempt to convert value to int...
#       except ValueError as e:
#           ...return None instead of raising...
#       return parsed_or_none
#
#   call:   safe_int("not a number")
#   output: None
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None


print(safe_int("not a number"))


# 8. try/except logging-like behavior (just returning a formatted message)
#
#   def describe_division(a, b):
#       try:
#           ...attempt division a / b...
#       except ZeroDivisionError as e:
#           ...return a string like "Failed division: division by zero"...
#       return successful_or_failed_message
#
#   call:   describe_division(5, 0)
#   output: "Failed division: division by zero"
def describe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return f"Failed division: {e}"


print(describe_division(5, 0))


# 9. try/except reading a possibly-missing key from first user
#
#   def first_user_city():
#       try:
#           ...take users[0] and access 'city' key...
#       except (IndexError, KeyError) as e:
#           ...return a message that city is unavailable...
#       return city_or_message
#
#   call:   first_user_city()
#   output: "City not available"
def first_user_city():
    try:
        return users[0]["city"]
    except (IndexError, KeyError):
        return "City not available"


print(first_user_city())


# 10. try/except converting first product price to float
#
#   def get_first_product_price():
#       try:
#           ...access products[0]['price'] and convert to float...
#       except (IndexError, KeyError, ValueError) as e:
#           ...return a message that price is invalid...
#       return price_or_message
#
#   call:   get_first_product_price()
#   output: either a float value or "Invalid product price"
def get_first_product_price():
    try:
        return float(products[0]["price"])
    except (IndexError, KeyError, ValueError):
        return "Invalid product price"


print(get_first_product_price())

# 11. try/except/else for clean separation of success path
#
#   def divide_with_else(a, b):
#       try:
#           ...attempt division a / b...
#       except ZeroDivisionError as e:
#           ...return "Cannot divide by zero"...
#       else:
#           ...return "Result is X" using the computed result...
#
#   call:   divide_with_else(10, 2)
#   output: "Result is 5.0"


# 12. try/except/else to parse int and confirm success
#
#   def parse_int_with_message(value):
#       try:
#           ...attempt int(value)...
#       except ValueError as e:
#           ...return "Failed to parse integer"...
#       else:
#           ...return "Parsed integer: X"...
#
#   call:   parse_int_with_message("42")
#   output: "Parsed integer: 42"


# 13. try/finally where finally always returns a fixed string (no except)
#
#   def always_cleanup(a, b):
#       try:
#           ...attempt risky division a / b but ignore result...
#       finally:
#           ...return a fixed string like "cleanup done" regardless of errors...
#
#   call:   always_cleanup(10, 0)
#   output: "cleanup done"


# 14. try/except/finally where finally adds text to error message
#
#   def divide_with_finally(a, b):
#       try:
#           ...attempt a / b...
#       except ZeroDivisionError as e:
#           ...set message to "Error: division by zero"...
#       else:
#           ...set message to "Success: result is X"...
#       finally:
#           ...append " | finished" to message and return it...
#
#   call:   divide_with_finally(6, 0)
#   output: "Error: division by zero | finished"


# 15. try/except returning default when list index invalid
#
#   def get_number_or_default(index, default):
#       try:
#           ...attempt to access numbers[index]...
#       except IndexError as e:
#           ...return the default value instead...
#       return value_or_default
#
#   call:   get_number_or_default(500, -1)
#   output: -1


# 16. try/except for nested dict access in a user
#
#   def get_user_email(user_dict):
#       try:
#           ...attempt to access user_dict['contact']['email']...
#       except (KeyError, TypeError) as e:
#           ...return "Email not found"...
#       return email_or_message
#
#   call:   get_user_email({'name': 'Alice'})
#   output: "Email not found"


# 17. try multiple operations raising different errors
#
#   def multi_risky(a, b, value):
#       try:
#           ...first divide a by b, then parse value as int...
#       except ZeroDivisionError as e:
#           ...return "Bad math"...
#       except ValueError as e:
#           ...return "Bad number"...
#       return "All good"
#
#   call:   multi_risky(10, 0, "123")
#   output: "Bad math"


# 18. order of except blocks matters (ValueError before Exception)
#
#   def parse_and_describe(value):
#       try:
#           ...attempt int(value)...
#       except ValueError as e:
#           ...return "Specific value error"...
#       except Exception as e:
#           ...return "Generic error"...
#       return "OK"
#
#   call:   parse_and_describe("not-int")
#   output: "Specific value error"


# 19. catching TypeError from adding incompatible types
#
#   def concat_or_fail(a, b):
#       try:
#           ...attempt a + b...
#       except TypeError as e:
#           ...return "Type mismatch"...
#       return result_or_message
#
#   call:   concat_or_fail(1, "2")
#   output: "Type mismatch"


# 20. try/except around accessing first order's total
#
#   def get_first_order_total():
#       try:
#           ...access orders[0]['total']...
#       except (IndexError, KeyError) as e:
#           ...return 0...
#       return total_or_zero
#
#   call:   get_first_order_total()
#   output: either a numeric total or 0


# 21. Using exception object message in return string
#
#   def parse_with_error_detail(value):
#       try:
#           ...attempt int(value)...
#       except ValueError as e:
#           ...return a string that includes str(e)...
#       return parsed_int
#
#   call:   parse_with_error_detail("xyz")
#   output: 'Error: invalid literal for int() with base 10: \'xyz\''


# 22. Access exception type name dynamically
#
#   def risky_add(a, b):
#       try:
#           ...attempt a + b...
#       except Exception as e:
#           ...return a string like "Caught TypeError" using type(e).__name__...
#       return result_or_message
#
#   call:   risky_add([], {})
#   output: "Caught TypeError"


# 23. Catch IndexError and show requested index in message
#
#   def fetch_number(index):
#       try:
#           ...access numbers[index]...
#       except IndexError as e:
#           ...return f"No item at index {index}"...
#       return value_or_message
#
#   call:   fetch_number(1000)
#   output: "No item at index 1000"


# 24. Catch KeyError and show missing key in message
#
#   def fetch_user_field(user_dict, field):
#       try:
#           ...access user_dict[field]...
#       except KeyError as e:
#           ...return f"Missing field: {field}"...
#       return value_or_message
#
#   call:   fetch_user_field({'name': 'Bob'}, 'age')
#   output: "Missing field: age"


# 25. try/except/else/finally full pattern demonstration
#
#   def full_flow(a, b):
#       try:
#           ...attempt division a / b...
#       except ZeroDivisionError as e:
#           ...set message to "error"...
#       else:
#           ...set message to "success"...
#       finally:
#           ...return message plus " (finalized)"...
#
#   call:   full_flow(5, 0)
#   output: "error (finalized)"


# 26. Using raise inside except to re-raise same exception
#
#   def rethrow_division(a, b):
#       try:
#           ...attempt a / b...
#       except ZeroDivisionError as e:
#           ...log-like behavior by creating a message string, then re-raise...
#       return "never reached on error"
#
#   call:   rethrow_division(1, 0)
#   output: ZeroDivisionError is propagated to caller


# 27. Converting one exception type into another using raise
#
#   def wrap_value_error(value):
#       try:
#           ...attempt int(value)...
#       except ValueError as e:
#           ...raise TypeError with message like "Expected numeric string"...
#       return parsed_int
#
#   call:   wrap_value_error("nope")
#   output: raises TypeError("Expected numeric string")


# 28. Manual validation and raise ValueError
#
#   def require_positive(number):
#       ...if number is not positive, raise ValueError with clear message...
#       return f"{number} is positive"
#
#   call:   require_positive(-1)
#   output: raises ValueError("number must be positive")


# 29. Use raise to signal unsupported operation
#
#   def only_even(number):
#       ...if number is odd, raise ValueError with message "Only even numbers allowed"...
#       return f"{number} is even"
#
#   call:   only_even(3)
#   output: raises ValueError("Only even numbers allowed")


# 30. Transform missing key into custom message using raise
#
#   def get_required_key(data, key):
#       try:
#           ...access data[key]...
#       except KeyError as e:
#           ...raise KeyError with custom message f"Required key {key} missing"...
#       return value
#
#   call:   get_required_key({}, 'id')
#   output: raises KeyError("Required key id missing")


# 31. Using assert for basic argument validation
#
#   def assert_positive(number):
#       ...use assert to ensure number > 0 with message "number must be > 0"...
#       return f"Got {number}"
#
#   call:   assert_positive(-5)
#   output: AssertionError with message "number must be > 0"


# 32. Asserting non-empty string
#
#   def assert_non_empty(name):
#       ...assert that name is truthy with message "name cannot be empty"...
#       return f"Hello, {name}"
#
#   call:   assert_non_empty("")
#   output: AssertionError("name cannot be empty")


# 33. Assertion combined with try/except catching AssertionError
#
#   def safe_assert_positive(number):
#       try:
#           ...assert number > 0 with message...
#       except AssertionError as e:
#           ...return f"Assertion failed: {e}"...
#       return "OK"
#
#   call:   safe_assert_positive(0)
#   output: "Assertion failed: number must be > 0"


# 34. Assert list is not empty before accessing first element
#
#   def first_student_name():
#       ...assert students is not empty with clear message...
#       ...on success, return the 'name' of the first student...
#
#   call:   first_student_name()
#   output: name of first student from students


# 35. Assert that product prices are positive for first product
#
#   def validate_first_product_price():
#       ...access first product price...
#       ...assert price > 0 with message "price must be positive"...
#       return True
#
#   call:   validate_first_product_price()
#   output: True or AssertionError("price must be positive")


# 36. Using assert inside loop over numbers
#
#   def ensure_all_numbers_positive():
#       ...iterate over numbers list...
#       ...assert each n >= 0 with message "found negative number"...
#       return "All non-negative"
#
#   call:   ensure_all_numbers_positive()
#   output: "All non-negative" or AssertionError("found negative number")


# 37. Introduce basic custom exception class
#
#   class DataValidationError(Exception):
#       ...simple subclass with no extra behavior...
#
#   def validate_id(user_dict):
#       ...if 'id' not in user_dict, raise DataValidationError with message...
#       return "OK"
#
#   call:   validate_id({'name': 'Test'})
#   output: raises DataValidationError("Missing id")


# 38. Custom exception with extra attribute
#
#   class TooManyItemsError(Exception):
#       ...accept count in __init__ and store as attribute...
#
#   def check_order_item_count(count):
#       ...if count > 10, raise TooManyItemsError with appropriate message...
#       return "Item count OK"
#
#   call:   check_order_item_count(20)
#   output: raises TooManyItemsError("Too many items: 20")


# 39. Catching a custom exception specifically
#
#   def handle_validation(user_dict):
#       try:
#           ...call validate_id(user_dict) which may raise DataValidationError...
#       except DataValidationError as e:
#           ...return f"Validation failed: {e}"...
#       return "Validation passed"
#
#   call:   handle_validation({'name': 'Bob'})
#   output: "Validation failed: Missing id"


# 40. Raising custom exception from inside except block
#
#   class ParseError(Exception):
#       ...simple subclass...
#
#   def parse_int_strict(value):
#       try:
#           ...attempt int(value)...
#       except ValueError as e:
#           ...raise ParseError(f"Could not parse '{value}'") from e...
#       return parsed_int
#
#   call:   parse_int_strict("oops")
#   output: raises ParseError("Could not parse 'oops'")


# 41. Using raise from to preserve original traceback
#
#   def wrap_zero_division(a, b):
#       try:
#           ...attempt a / b...
#       except ZeroDivisionError as e:
#           ...raise ValueError("Invalid divisor") from e...
#       return result
#
#   call:   wrap_zero_division(1, 0)
#   output: raises ValueError("Invalid divisor") with chained exception


# 42. Validate order has required fields, raise custom DataValidationError
#
#   def validate_order(order):
#       ...if 'id' or 'total' missing, raise DataValidationError with message...
#       return "Order valid"
#
#   call:   validate_order({'id': 1})
#   output: raises DataValidationError("Missing total")


# 43. Catching multiple exception types in one except tuple
#
#   def safe_access_user(user_index, field):
#       try:
#           ...access users[user_index][field]...
#       except (IndexError, KeyError) as e:
#           ...return "Not found"...
#       return value_or_message
#
#   call:   safe_access_user(999, 'name')
#   output: "Not found"


# 44. Use try/except to provide fallback default for missing student grade
#
#   def get_student_grade(student_dict):
#       try:
#           ...return student_dict['grade']...
#       except KeyError as e:
#           ...return "N/A"...
#
#   call:   get_student_grade({'name': 'Sam'})
#   output: "N/A"


# 45. Mix assertion and manual raise for advanced validation
#
#   def validate_product(product):
#       ...assert 'id' in product...
#       ...if 'price' not in product, raise DataValidationError("Missing price")...
#       return "Valid product"
#
#   call:   validate_product({'id': 1})
#   output: raises DataValidationError("Missing price")


# 46. Using try/except to continue processing list despite errors
#
#   def parse_numbers(values):
#       ...iterate over values list...
#       ...for each, try int(value), catch ValueError and skip that item...
#       ...return list of successfully parsed ints...
#
#   call:   parse_numbers(["1", "x", "2"])
#   output: [1, 2]


# 47. try/except/else for conditional logging
#
#   def divide_and_flag(a, b):
#       try:
#           ...attempt a / b...
#       except ZeroDivisionError as e:
#           ...return ("error", None)...
#       else:
#           ...return ("ok", result)...
#
#   call:   divide_and_flag(4, 2)
#   output: ("ok", 2.0)


# 48. Validate that a product has numeric price using try/except
#
#   def cast_product_price(product):
#       try:
#           ...convert product['price'] to float...
#       except (KeyError, ValueError, TypeError) as e:
#           ...return None...
#       return float_price
#
#   call:   cast_product_price({'id': 1, 'price': 'not-number'})
#   output: None


# 49. Use finally to guarantee closing-like behavior (simulated)
#
#   def fake_open_and_close(should_fail):
#       try:
#           ...simulate opening a resource...
#           ...if should_fail, raise ValueError("failed")...
#       except ValueError as e:
#           ...set message to "operation failed"...
#       else:
#           ...set message to "operation succeeded"...
#       finally:
#           ...append " | resource closed" to message and return...
#
#   call:   fake_open_and_close(True)
#   output: "operation failed | resource closed"


# 50. Using assertions to check consistency between two values
#
#   def assert_matching_totals(expected, actual):
#       ...assert expected == actual with message "totals do not match"...
#       return "Totals match"
#
#   call:   assert_matching_totals(100, 90)
#   output: AssertionError("totals do not match")


# 51. Validating a user dictionary with multiple required keys
#
#   def validate_user(user_dict):
#       ...if any of ['id', 'name', 'email'] missing, raise DataValidationError...
#       return "User valid"
#
#   call:   validate_user({'id': 1, 'name': 'Ana'})
#   output: raises DataValidationError("Missing email")


# 52. Custom exception for not found user
#
#   class UserNotFoundError(Exception):
#       ...store user_id in the instance...
#
#   def find_user_by_id(user_id):
#       ...search users list for matching id...
#       ...if not found, raise UserNotFoundError(f"User {user_id} not found")...
#       return user_dict
#
#   call:   find_user_by_id(-1)
#   output: raises UserNotFoundError("User -1 not found")


# 53. Handle custom UserNotFoundError and return fallback
#
#   def get_user_name_or_unknown(user_id):
#       try:
#           ...call find_user_by_id(user_id)...
#       except UserNotFoundError as e:
#           ...return "Unknown"...
#       return user_name
#
#   call:   get_user_name_or_unknown(-1)
#   output: "Unknown"


# 54. Use assertions inside custom exception __init__
#
#   class NonEmptyStringError(Exception):
#       ...__init__ asserts that message is non-empty string...
#
#   def fail_with_custom_assertion():
#       ...attempt to create NonEmptyStringError with empty message to trigger AssertionError...
#
#   call:   fail_with_custom_assertion()
#   output: AssertionError raised inside NonEmptyStringError __init__


# 55. Re-raising after partial handling (logging-style) in except
#
#   def log_then_raise(value):
#       try:
#           ...attempt int(value)...
#       except ValueError as e:
#           ...create a log_message string, then raise again...
#
#   call:   log_then_raise("bad")
#   output: ValueError propagated to caller


# 56. Convert any exception from parsing order total into 0
#
#   def safe_order_total(order):
#       try:
#           ...return float(order['total'])...
#       except Exception as e:
#           ...return 0.0...
#
#   call:   safe_order_total({'id': 1, 'total': 'not-a-number'})
#   output: 0.0


# 57. Assert that numbers list is sorted ascending
#
#   def assert_numbers_sorted():
#       ...assert numbers == sorted(numbers) with message "numbers not sorted"...
#       return True
#
#   call:   assert_numbers_sorted()
#   output: True or AssertionError("numbers not sorted")


# 58. Use try/except inside a comprehension-like loop (expanded manually)
#
#   def safe_parse_list(values):
#       ...iterate over values...
#       ...for each, try to int(value), on ValueError append None...
#       ...return resulting list of ints and Nones...
#
#   call:   safe_parse_list(["1", "x", "3"])
#   output: [1, None, 3]


# 59. Validate that all students have 'name' field using raise
#
#   def ensure_students_have_names():
#       ...iterate over students...
#       ...if any student missing 'name', raise DataValidationError...
#       return "All students have names"
#
#   call:   ensure_students_have_names()
#   output: "All students have names" or DataValidationError


# 60. try/except around complex nested access with multiple keys
#
#   def get_order_customer_name(order):
#       try:
#           ...access order['customer']['name']...
#       except (KeyError, TypeError) as e:
#           ...return "Unknown customer"...
#       return name_or_message
#
#   call:   get_order_customer_name({'id': 1})
#   output: "Unknown customer"


# 61. Assert relationship between two fields in product
#
#   def validate_discount(product):
#       ...assert product['discount'] <= product['price']...
#       ...raise AssertionError with message if violated...
#       return "Discount valid"
#
#   call:   validate_discount({'price': 10, 'discount': 20})
#   output: AssertionError


# 62. Use raise to enforce type on function argument
#
#   def ensure_int(value):
#       ...if not isinstance(value, int), raise TypeError("value must be int")...
#       return value
#
#   call:   ensure_int("5")
#   output: raises TypeError("value must be int")


# 63. Custom exception for invalid grade
#
#   class InvalidGradeError(Exception):
#       ...store grade in instance...
#
#   def validate_grade(grade):
#       ...if grade not between 0 and 100, raise InvalidGradeError...
#       return "Grade OK"
#
#   call:   validate_grade(150)
#   output: raises InvalidGradeError


# 64. Handle InvalidGradeError and fall back to 0
#
#   def safe_grade(grade):
#       try:
#           ...call validate_grade(grade)...
#       except InvalidGradeError as e:
#           ...return 0...
#       return grade
#
#   call:   safe_grade(150)
#   output: 0


# 65. Combining assert and custom exception in one function
#
#   def guarded_divide(a, b):
#       ...assert isinstance(a, (int, float))...
#       ...if b == 0, raise ZeroDivisionError("b cannot be zero")...
#       return a / b
#
#   call:   guarded_divide("10", 2)
#   output: AssertionError


# 66. Using try/except/else/finally to track control flow flags
#
#   def trace_division(a, b):
#       ...use variables like tried, succeeded, cleaned...
#       ...in try, set tried and attempt division...
#       ...in except, set succeeded flag False and set message...
#       ...in else, set succeeded True and message with result...
#       ...in finally, set cleaned True and return a dict with these flags...
#
#   call:   trace_division(1, 0)
#   output: {'tried': True, 'succeeded': False, 'cleaned': True, 'message': 'division by zero'}


# 67. Raise from custom validation that uses multiple conditions
#
#   def validate_user_age(user_dict):
#       ...if 'age' missing, raise DataValidationError("Missing age")...
#       ...if age < 0, raise DataValidationError("Invalid age")...
#       return "Age OK"
#
#   call:   validate_user_age({'name': 'Ana', 'age': -1})
#   output: raises DataValidationError("Invalid age")


# 68. catch errors while summing numbers, skipping bad entries
#
#   def sum_mixed(values):
#       ...iterate over values, try to convert each to float...
#       ...on error, skip that entry...
#       ...return total sum of valid entries...
#
#   call:   sum_mixed([1, "2", "x", 3])
#   output: 6.0


# 69. Use assert to ensure users list is not empty before access
#
#   def first_user_safe():
#       ...assert users is not empty with message "no users"...
#       return users[0]
#
#   call:   first_user_safe()
#   output: first user dict or AssertionError("no users")


# 70. Custom exception hierarchy (base and subclass)
#
#   class AppError(Exception):
#       ...base custom exception...
#
#   class ConfigError(AppError):
#       ...subclass representing configuration errors...
#
#   def load_config(config):
#       ...if 'host' missing, raise ConfigError("Missing host")...
#       return "Config loaded"
#
#   call:   load_config({})
#   output: raises ConfigError("Missing host")


# 71. Catching base AppError for multiple custom types
#
#   def safe_load_config(config):
#       try:
#           ...call load_config(config)...
#       except AppError as e:
#           ...return f"Config failure: {e}"...
#       return "OK"
#
#   call:   safe_load_config({})
#   output: "Config failure: Missing host"


# 72. Using raise to enforce minimum order total
#
#   def enforce_minimum_total(order, minimum):
#       ...if order['total'] < minimum, raise DataValidationError...
#       return "Meets minimum"
#
#   call:   enforce_minimum_total({'id': 1, 'total': 5}, 10)
#   output: raises DataValidationError("Order total below minimum")


# 73. try/except converting student scores and computing average
#
#   def average_scores(scores):
#       ...attempt to convert each to float, skipping invalid with try/except...
#       ...if no valid scores, raise ValueError("no valid scores")...
#       return average
#
#   call:   average_scores(["A", "B"])
#   output: raises ValueError("no valid scores")


# 74. Assertion on relationship of two fields in user object
#
#   def assert_name_longer_than_username(user_dict):
#       ...assert len(name) > len(username) with message...
#       return True
#
#   call:   assert_name_longer_than_username({'name': 'Bo', 'username': 'longusername'})
#   output: AssertionError


# 75. Using custom exception for duplicate IDs
#
#   class DuplicateIdError(Exception):
#       ...store the duplicate id...
#
#   def ensure_unique_ids(items):
#       ...iterate items, track seen ids, raise DuplicateIdError on duplicate...
#       return "All ids unique"
#
#   call:   ensure_unique_ids([{'id': 1}, {'id': 1}])
#   output: raises DuplicateIdError


# 76. Handle DuplicateIdError and return index of duplicate
#
#   def find_duplicate_index(items):
#       try:
#           ...call ensure_unique_ids(items)...
#       except DuplicateIdError as e:
#           ...return index of the second occurrence (simulated or precomputed)...
#       return -1
#
#   call:   find_duplicate_index([{'id': 1}, {'id': 1}])
#   output: 1


# 77. Use finally to reset a global-like flag after error
#
#   busy = False
#
#   def do_work(may_fail):
#       ...set busy True at start...
#       try:
#           ...if may_fail, raise RuntimeError("failed")...
#       except RuntimeError as e:
#           ...set message to "error"...
#       else:
#           ...set message to "success"...
#       finally:
#           ...set busy False and return (message, busy)...
#
#   call:   do_work(True)
#   output: ("error", False)


# 78. Combine assertion and try/except when processing users
#
#   def process_first_user():
#       ...assert users not empty...
#       try:
#           ...access users[0]['email']...
#       except KeyError as e:
#           ...return "Missing email"...
#       return email
#
#   call:   process_first_user()
#   output: email string or "Missing email"


# 79. Using raise within loop when invalid data encountered
#
#   def validate_all_orders(orders_list):
#       ...for each order, if 'total' missing or <= 0, raise DataValidationError...
#       return "All orders valid"
#
#   call:   validate_all_orders([{'id': 1, 'total': 0}])
#   output: raises DataValidationError


# 80. try/except collecting all errors into list of messages
#
#   def validate_products(products_list):
#       ...for each product, try to ensure 'id' and 'price' exist...
#       ...on error, catch and append message to errors list...
#       ...return errors list (may be empty)...
#
#   call:   validate_products([{'id': 1}, {'price': 10}])
#   output: list with two error message strings


# 81. Complex assertion involving multiple fields and conditions
#
#   def assert_valid_student(student):
#       ...assert 'name' in student and 'age' in student and age >= 0...
#       ...use a single assert with compound condition and message...
#       return True
#
#   call:   assert_valid_student({'name': 'Ana'})
#   output: AssertionError


# 82. Nested try/except (inner handles one error, outer handles another)
#
#   def nested_risky(a, b, value):
#       try:
#           try:
#               ...attempt a / b...
#           except ZeroDivisionError as e:
#               ...return "inner division error"...
#           ...attempt int(value) which may raise ValueError handled by outer...
#       except ValueError as e:
#           ...return "outer parse error"...
#       return "all good"
#
#   call:   nested_risky(1, 1, "bad")
#   output: "outer parse error"


# 83. Use raise to abort early when invalid configuration detected
#
#   def init_app(config):
#       ...if 'debug' not in config, raise ConfigError("Missing debug")...
#       ...if 'database' not in config, raise ConfigError("Missing database")...
#       return "App initialized"
#
#   call:   init_app({'debug': True})
#   output: raises ConfigError("Missing database")


# 84. try/except/else to distinguish between parse failure and negative value
#
#   def parse_and_check_positive(value):
#       try:
#           ...attempt int(value)...
#       except ValueError as e:
#           ...return "not a number"...
#       else:
#           ...if parsed <= 0, return "non-positive"...
#           ...otherwise return "ok"...
#
#   call:   parse_and_check_positive("-1")
#   output: "non-positive"


# 85. Use assertion in combination with custom exception in catch
#
#   def assert_and_convert(value):
#       ...assert value is not None with message...
#       try:
#           ...convert to int...
#       except ValueError as e:
#           ...raise ParseError("Conversion failed")...
#       return int_value
#
#   call:   assert_and_convert("bad")
#   output: raises ParseError("Conversion failed")


# 86. try/except on accessing nested product field with default fallback
#
#   def get_product_category(product):
#       try:
#           ...return product['metadata']['category']...
#       except (KeyError, TypeError) as e:
#           ...return "general"...
#
#   call:   get_product_category({'id': 1})
#   output: "general"


# 87. Raise when numeric constraint violated across entire list
#
#   def ensure_all_nonzero(values):
#       ...if any value is 0, raise DataValidationError("zero found")...
#       return "no zeros"
#
#   call:   ensure_all_nonzero([1, 0, 2])
#   output: raises DataValidationError("zero found")


# 88. Custom exception combining multiple error messages
#
#   class AggregateError(Exception):
#       ...accept list of messages and join into one message...
#
#   def validate_students_list(students_list):
#       ...collect per-student errors into a list...
#       ...if any, raise AggregateError with all messages...
#       return "All students valid"
#
#   call:   validate_students_list([{}, {'name': 'Ana'}])
#   output: raises AggregateError with combined messages


# 89. Use try/except to keep track of success and failure counts
#
#   def parse_with_stats(values):
#       ...for each value, try int conversion...
#       ...count successes and failures...
#       ...return dict with {'success': X, 'failure': Y}...
#
#   call:   parse_with_stats(["1", "x", "2", "bad"])
#   output: {'success': 2, 'failure': 2}


# 90. Assertion checking invariants after transformation
#
#   def double_numbers(nums):
#       ...create new list with each number doubled...
#       ...assert len(new_list) == len(nums) with message...
#       return new_list
#
#   call:   double_numbers([1, 2, 3])
#   output: [2, 4, 6]


# 91. Use finally to clear a temporary cache even on exceptions
#
#   temp_cache = {}
#
#   def compute_with_cache(key, value, fail=False):
#       ...store value in temp_cache under key...
#       try:
#           ...if fail, raise RuntimeError...
#           ...otherwise return value...
#       except RuntimeError as e:
#           ...set result to None...
#       finally:
#           ...remove key from temp_cache and return result...
#
#   call:   compute_with_cache("a", 10, fail=True)
#   output: None and temp_cache does not contain "a"


# 92. Custom exception for invalid product combination
#
#   class InvalidProductComboError(Exception):
#       ...accept two product ids and build message...
#
#   def combine_products(p1, p2):
#       ...if p1['id'] == p2['id'], raise InvalidProductComboError...
#       return "Combined"
#
#   call:   combine_products({'id': 1}, {'id': 1})
#   output: raises InvalidProductComboError


# 93. Handle multiple custom exceptions in one place
#
#   def robust_combine(p1, p2):
#       try:
#           ...call combine_products(p1, p2)...
#       except (InvalidProductComboError, DataValidationError) as e:
#           ...return f"combine failed: {e}"...
#       return "combine succeeded"
#
#   call:   robust_combine({'id': 1}, {'id': 1})
#   output: "combine failed: ..." with appropriate message


# 94. Use assertions for preconditions and raises for postconditions
#
#   def transform_and_validate(value):
#       ...assert isinstance(value, int)...
#       ...compute result = value * 2...
#       ...if result > 100, raise DataValidationError("too large")...
#       return result
#
#   call:   transform_and_validate(60)
#   output: raises DataValidationError("too large")


# 95. try/except/else/finally for full pipeline: parse, validate, finalize
#
#   def pipeline_step(raw_value):
#       try:
#           ...parse raw_value as int...
#           ...if negative, raise ValueError("negative not allowed")...
#       except ValueError as e:
#           ...set status to "error" and detail to message...
#       else:
#           ...set status to "ok" and detail to parsed value...
#       finally:
#           ...return dict with {'status': status, 'detail': detail}...
#
#   call:   pipeline_step("-5")
#   output: {'status': 'error', 'detail': 'negative not allowed'}


# 96. Complex validation using custom exceptions and assertions together
#
#   def validate_user_record(user):
#       ...assert user is a dict...
#       ...if 'id' missing, raise DataValidationError...
#       ...if 'name' empty string, raise DataValidationError...
#       return "record valid"
#
#   call:   validate_user_record({'id': 1, 'name': ''})
#   output: raises DataValidationError


# 97. Implement retry-like behavior on transient error
#
#   class TransientError(Exception):
#       ...simple subclass...
#
#   def do_unstable(attempts_before_success, current_attempt):
#       ...if current_attempt < attempts_before_success, raise TransientError...
#       ...otherwise return "ok"...
#
#   def retry_unstable(attempts_before_success, max_retries):
#       ...loop up to max_retries, calling do_unstable with attempt counter...
#       ...catch TransientError, continue loop...
#       ...on success, return "success on attempt X"...
#       ...if still failing after retries, return "failed after X retries"...
#
#   call:   retry_unstable(3, 2)
#   output: "failed after 2 retries"


# 98. Aggregate multiple validation errors into AggregateError
#
#   def validate_order_record(order):
#       ...collect problems such as missing 'id', missing 'total', non-positive total...
#       ...if no problems, return "ok"...
#       ...if problems exist, raise AggregateError with problem messages...
#
#   call:   validate_order_record({'total': -1})
#   output: raises AggregateError with messages about missing id and non-positive total


# 99. Exception-aware data processing pipeline with fallback defaults
#
#   def safe_process_user(user):
#       ...try to extract id (int), name (str), and age (int)...
#       ...use try/except for each to fall back to defaults (id=-1, name='Unknown', age=0)...
#       ...return normalized dict with these fields...
#
#   call:   safe_process_user({'name': 'Bob', 'age': 'bad'})
#   output: {'id': -1, 'name': 'Bob', 'age': 0}


# 100. The Boss Drill: Combine multiple exception patterns with data processing
#
#   def process_orders_with_exceptions(orders_list, min_total):
#       #   Overall goal:
#       #   - iterate over orders_list (list of dicts)
#       #   - for each order:
#       #       * safely read 'id' (if missing, raise DataValidationError)
#       #       * safely convert 'total' to float with try/except (if invalid, treat as 0.0)
#       #       * enforce that total >= min_total (if not, raise DataValidationError)
#       #   - collect all valid orders into a new list
#       #   - use try/except to catch DataValidationError per-order and skip bad ones
#       #   - use assertions to ensure result list length <= original length
#       #   - if, after processing, result list is empty, raise AggregateError with messages
#       #   - otherwise return:
#       #       { 'count': <number of valid orders>, 'totals': <list of valid totals> }
#       #
#       #   You MUST use:
#       #       - try/except with specific exceptions (ValueError, KeyError)
#       #       - custom exception DataValidationError
#       #       - raising exceptions manually with raise
#       #       - at least one assert about the result
#       #       - optionally finally for any cleanup or final check
#
#   call:   process_orders_with_exceptions(
#              [{'id': 1, 'total': '5.0'}, {'id': 2, 'total': 'bad'}, {'total': 20}],
#              min_total=10.0
#          )
#   output: {'count': 1, 'totals': [5.0]}
