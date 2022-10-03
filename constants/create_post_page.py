class CreatePostPageConsts:
    # Create Post
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    BODY_FIELD_XPATH = ".//textarea[@id='post-body']"
    POST_CHECKBOX_XPATH = ".//input[@type='checkbox']"
    CREATE_POST_BUTTON_XPATH = ".//button[contains(text(),'Save New Post')]"
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
    DELETE_POST_BUTTON_XPATH = ".//button[@class='delete-post-button text-danger']"
    DELETE_MESSAGE_TEXT = "Post successfully deleted"
    DELETE_MESSAGE_XPATH = f".//div[contains(text(),'{DELETE_MESSAGE_TEXT}')]"
    EDIT_POST_BUTTON_XPATH = ".//a[@class='text-primary mr-2']"
    EDIT_MESSAGE_TEXT = "Post successfully updated."
    EDIT_MESSAGE_XPATH = f".//div[contains(text(),'{EDIT_MESSAGE_TEXT}')]"
    UNIQUE_MESSAGE_YES_TEXT = "Is this post unique? : yes"
    UNIQUE_MESSAGE_YES_XPATH = f".//p[contains(text(),'{UNIQUE_MESSAGE_YES_TEXT}')]"
    UNIQUE_MESSAGE_NO_TEXT = "Is this post unique? : no"
    UNIQUE_MESSAGE_NO_XPATH = f".//p[contains(text(),'{UNIQUE_MESSAGE_NO_TEXT}')]"
    PUBLIC_MESSAGE_TEXT = "All Users"
    PUBLIC_MESSAGE_XPATH = f".//u[contains(text(),'{PUBLIC_MESSAGE_TEXT}')]"
    PRIVATE_MESSAGE_TEXT = "One Person"
    PRIVATE_MESSAGE_XPATH = f".//u[contains(text(),'{PRIVATE_MESSAGE_TEXT}')]"
    GROUP_MESSAGE_TEXT = "Group Message"
    GROUP_MESSAGE_XPATH = f".//u[contains(text(),'{GROUP_MESSAGE_TEXT}')]"

    # Select
    POST_SELECT_XPATH = ".//select[@id='select1']"

    # Update Post
    UPDATE_POST_BUTTON_XPATH = ".//button[contains(text(),'Save Updates')]"
    UPDATE_POST_TITLE_TEXT = "Title is updated"
    UPDATE_POST_BODY_TEXT = "Body content is updated"

    # Saved post verification
    POST_TITLE_INPUT = "Test post title"
    POST_BODY_INPUT = "Test post body content"
    SAVED_POST_TITLE_XPATH = ".//div[@class='d-flex justify-content-between']/h2"
    SAVED_POST_BODY_XPATH = ".//div[@class='body-content'][2]/p"
