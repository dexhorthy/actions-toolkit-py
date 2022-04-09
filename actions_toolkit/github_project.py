
def move_card_to_column(owner, repo, issue_content_url, project, column):
    print(
        "moving card to column: %s" %
        " | ".join([owner, repo, issue_content_url, project, column]),
    )
