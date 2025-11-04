# addiction_rules.py
# ---------------------------------------------------
# This file defines the rule-based logic (AI part)
# to classify user's social media addiction level
# based on average screen time and productivity hours.
# ---------------------------------------------------

def get_addiction_level(avg_social, avg_productivity):
    """
    Determines the addiction level based on rule-based logic.

    Parameters:
        avg_social (float): Average daily hours on social media.
        avg_productivity (float): Average daily productive hours.

    Returns:
        addiction_level (str): 'Low', 'Moderate', or 'High'
        message (str): AI feedback message for the user.
    """

    # --- Simple Rule-Based Logic ---
    if avg_social > 5 and avg_productivity < 3:
        addiction_level = "High"
        message = (
            "Your screen time is quite high and productivity is low.\n"
            "Try taking a digital detox — set app limits or reduce usage before sleep."
        )

    elif 3 <= avg_social <= 5:
        addiction_level = "Moderate"
        message = (
            "You're managing fairly well but could use your time more efficiently.\n"
            "Try balancing your study/work hours and screen time."
        )

    else:
        addiction_level = "Low"
        message = (
            "Great job! You have healthy social media habits.\n"
            "Keep focusing on productivity and maintain your routine!"
        )

    return addiction_level, message
