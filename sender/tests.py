
from django.core import mail
from django.test import TestCase, override_settings


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"
)
class EmailSenderTests(TestCase):
    def test_homepage_displays_email_form(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django Email Sender")
        self.assertContains(response, "Recipient email")

    def test_valid_form_sends_email(self):
        response = self.client.post(
            "/",
            {
                "recipient_email": "test@example.com",
                "subject": "Test subject",
                "message": "Hello from Django",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email prepared successfully!")
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            "Test subject",
        )
        self.assertEqual(
            mail.outbox[0].to,
            ["test@example.com"],
        )

    def test_invalid_email_does_not_send_email(self):
        response = self.client.post(
            "/",
            {
                "recipient_email": "not-an-email",
                "subject": "Test subject",
                "message": "Hello",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)
