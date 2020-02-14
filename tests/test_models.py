from danger_python.models import DangerDSLJSONType, GitHubReviewState


def test_github_dsl_handles_correct_review_states():
    """
    Test that GitHub DSL handles correct review states.
    """
    dsl_json = {
        "github": {
            "reviews": [
                {"state": "APPROVED"},
                {"state": "CHANGES_REQUESTED"},
                {"state": "COMMENTED"},
                {"state": "PENDING"},
                {"state": "DISMISSED"},
            ]
        }
    }

    dsl = DangerDSLJSONType(**dsl_json)

    assert len(dsl.github.reviews) == 5
    assert dsl.github.reviews[0].state == GitHubReviewState.APPROVED
    assert dsl.github.reviews[1].state == GitHubReviewState.CHANGES_REQUESTED
    assert dsl.github.reviews[2].state == GitHubReviewState.COMMENTED
    assert dsl.github.reviews[3].state == GitHubReviewState.PENDING
    assert dsl.github.reviews[4].state == GitHubReviewState.DISMISSED
