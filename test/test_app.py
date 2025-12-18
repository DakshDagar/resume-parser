import io
from app import app


def test_home_page_loads():
    """
    Test that the home page loads correctly.
    """
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_resume_upload_endpoint_accepts_file():
    """
    Test that /process accepts a file upload
    without crashing.
    """

    client = app.test_client()

    # Fake text resume file
    fake_resume = io.BytesIO(b"John Doe\nPython Developer\njohn@example.com")

    data = {
        "pdf_doc": (fake_resume, "resume.txt")
    }

    response = client.post(
        "/process",
        data=data,
        content_type="multipart/form-data"
    )

    # We don't assert content because AI output varies
    assert response.status_code == 200
