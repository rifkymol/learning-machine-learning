# 🔍 Exercise Validation Helper
# This file contains helper functions for validating exercises

def check_answer(condition, success_msg="✅ Correct! Great job!", error_msg="❌ Not quite right. Try again!"):
    """
    Check if condition is True and print appropriate feedback
    """
    if condition:
        print(success_msg)
        return True
    else:
        print(error_msg)
        return False

def check_type(variable, expected_type, var_name="variable"):
    """
    Check if variable has the expected type
    """
    if isinstance(variable, expected_type):
        print(f"✅ {var_name} has correct type: {expected_type.__name__}")
        return True
    else:
        print(f"❌ {var_name} should be {expected_type.__name__}, but got {type(variable).__name__}")
        return False

def check_value(actual, expected, var_name="value"):
    """
    Check if actual value matches expected value
    """
    if actual == expected:
        print(f"✅ {var_name} is correct: {expected}")
        return True
    else:
        print(f"❌ {var_name} should be {expected}, but got {actual}")
        return False

def check_range(value, min_val, max_val, var_name="value"):
    """
    Check if value is within range
    """
    if min_val <= value <= max_val:
        print(f"✅ {var_name} ({value}) is within expected range [{min_val}, {max_val}]")
        return True
    else:
        print(f"❌ {var_name} ({value}) should be between {min_val} and {max_val}")
        return False

def validate_all(checks):
    """
    Run multiple validation checks
    checks: list of tuples (condition, success_msg, error_msg)
    """
    all_passed = True
    for check in checks:
        condition, success_msg, error_msg = check
        if not check_answer(condition, success_msg, error_msg):
            all_passed = False
    
    if all_passed:
        print("\n🎉 All checks passed! You can move to the next exercise.")
    else:
        print("\n💡 Some checks failed. Review your code and try again.")
    
    return all_passed
