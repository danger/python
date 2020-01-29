from danger_python.models import GitHubDSL


def test_that_github_model_is_parsed_correctly():
    """
    Test that Github model is parsed correctly.
    """
    github_json = {"pr": {"title": "Tie-tle"}}

    dsl = GitHubDSL(**github_json)

    assert dsl.pr.title == "Tie-tle"
