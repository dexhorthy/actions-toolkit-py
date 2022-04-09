from unittest import TestCase
from github_project import move_card_to_column


class TestGitHubProject(TestCase):
    def test_nothing(self):
        move_card_to_column(
            owner="replicated-collab",
            repo="superci-replicated",
            issue_content_url="https://api.github.com/repos/replicated-collab/superci-replicated/issues/102",
            project="Inbound Escalations",
            column="Pending"
        )

        self.assertEqual(1, 1)
