class HeaderBeforeSignInConsts:
    # Sign In
    SIGN_IN_LOGIN_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASS_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"
    SIGN_IN_BUTTON_TEXT = "Sign In"
    SIGN_IN_INVALID_DATA_MESSAGE_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_INVALID_DATA_MESSAGE_TEXT = "Invalid username / pasword"
    SIGN_IN_CORRECT_LOGIN_INPUT = "nicewarthog"
    SIGN_IN_CORRECT_PASS_INPUT = "nicewarthogpass"
    SIGN_OUT_BUTTON_XPATH = ".//button[contains(text(),'Sign Out')]"

    # # Create Post
    ACCOUNT_NAME_XPATH = ".//span[@class='text-white mr-2']"
