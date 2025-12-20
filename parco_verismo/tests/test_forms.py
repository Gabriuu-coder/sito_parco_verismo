from django.test import TestCase
from parco_verismo.forms.richiesta import RichiestaForm


class RichiestaFormTests(TestCase):
    def test_valid_form(self):
        data = {
            "nome": "Mario",
            "cognome": "Rossi",
            "email": "mario@example.com",
            "oggetto": "Informazioni",
            "messaggio": "Vorrei informazioni sulle visite guidate.",
        }
        form = RichiestaForm(data)
        self.assertTrue(form.is_valid())

    def test_message_too_long(self):
        data = {
            "nome": "Mario",
            "cognome": "Rossi",
            "email": "mario@example.com",
            "oggetto": "Info",
            "messaggio": "x" * 1001,
        }
        form = RichiestaForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("messaggio", form.errors)

    def test_message_all_uppercase_rejected(self):
        data = {
            "nome": "Mario",
            "cognome": "Rossi",
            "email": "mario@example.com",
            "oggetto": "Info",
            "messaggio": "THIS IS A LOUD MESSAGE AND SHOULD BE REJECTED" * 2,
        }
        form = RichiestaForm(data)
        self.assertFalse(form.is_valid())
        # clean() raises a non-field error for uppercase messages
        self.assertIn("__all__", form.errors)

    def test_too_many_links_rejected(self):
        mess = """Link1: http://a.com Link2: http://b.com Link3: http://c.com Link4: http://d.com"""
        data = {
            "nome": "Mario",
            "cognome": "Rossi",
            "email": "mario@example.com",
            "oggetto": "Info",
            "messaggio": mess,
        }
        form = RichiestaForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)

    def test_temporary_email_blocked(self):
        data = {
            "nome": "Mario",
            "cognome": "Rossi",
            "email": "foo@tempmail.com",
            "oggetto": "Info",
            "messaggio": "Ciao",
        }
        form = RichiestaForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
