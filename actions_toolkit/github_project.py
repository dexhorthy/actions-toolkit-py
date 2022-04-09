import logging

logger = logging.getLogger(__file__)


def move_card_to_column(owner, repo, issue_content_url, project, column):
    logger.info(
        "moving card to column: %s",
        " | ".join([owner, repo, issue_content_url, project, column]),
    )
