class CreatePostPageConsts:
    # Create Post
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    BODY_FIELD_XPATH = ".//textarea[@id='post-body']"
    POST_CHECKBOX_XPATH = ".//input[@type='checkbox']"
    CREATE_POST_BUTTON_XPATH = ".//button[contains(text(),'Save New Post')]"
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
    DELETE_POST_BUTTON_XPATH = ".//button[@class='delete-post-button text-danger']"
    DELETE_MESSAGE_XPATH = ".//div[contains(text(),'Post successfully deleted')]"
    DELETE_MESSAGE_TEXT = "Post successfully deleted"
    EDIT_POST_BUTTON_XPATH = ".//a[@class='text-primary mr-2']"
    EDIT_MESSAGE_XPATH = ".//div[contains(text(),'Post successfully updated.')]"
    EDIT_MESSAGE_TEXT = "Post successfully updated."
    UNIQUE_MESSAGE_YES_XPATH = ".//p[contains(text(),'Is this post unique? : yes')]"
    UNIQUE_MESSAGE_YES_TEXT = "Is this post unique? : yes"
    UNIQUE_MESSAGE_NO_XPATH = ".//p[contains(text(),'Is this post unique? : no')]"
    UNIQUE_MESSAGE_NO_TEXT = "Is this post unique? : no"

    # Update Post
    UPDATE_POST_BUTTON_XPATH = ".//button[contains(text(),'Save Updates')]"
    UPDATE_POST_TITLE_TEXT = "Title is updated"
    UPDATE_POST_BODY_TEXT = "Body content is updated"

    # Saved post verification
    POST_TITLE_INPUT = "Test post title"
    POST_BODY_INPUT = "Test post body content"
    SAVED_POST_TITLE_XPATH = ".//div[@class='d-flex justify-content-between']/h2"
    SAVED_POST_BODY_XPATH = ".//div[@class='body-content'][2]/p"
