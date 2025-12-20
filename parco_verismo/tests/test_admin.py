from django.test import TestCase, override_settings
from parco_verismo.admin.richieste import RichiestaAdmin
from parco_verismo.admin_richieste import RichiestaCustomAdmin
from parco_verismo.services import email_service
from parco_verismo.models import Richiesta
from django.core import mail


class AdminFieldTests(TestCase):
    def test_richieste_admin_fields(self):
        ld = RichiestaAdmin.list_display
        self.assertNotIn("telefono", ld)
        self.assertNotIn("luogo", ld)
        self.assertNotIn("itinerario", ld)
        self.assertIn("email_link", ld)
        self.assertIn("data_completamento", ld)

    def test_custom_admin_fields(self):
        ld = RichiestaCustomAdmin.list_display
        self.assertNotIn("telefono", ld)
        self.assertNotIn("luogo", ld)
        self.assertNotIn("numero_partecipanti", ld)
        self.assertIn("badge_ritardo", ld)
        self.assertIn("data_completamento", ld)


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    DEFAULT_FROM_EMAIL="test@example.com",
    ADMIN_EMAIL="admin@example.com",
)
class EmailServiceTests(TestCase):
    def test_send_confirmation(self):
        r = Richiesta.objects.create(
            nome="Mario",
            cognome="Rossi",
            email="mario@example.com",
            oggetto="Info",
            messaggio="Ciao",
        )
        mail.outbox = []
        ok = email_service.invia_email_richiesta_confermata(r)
        self.assertTrue(ok)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Richiesta ricevuta", mail.outbox[0].subject)

    def test_send_admin_notification(self):
        r = Richiesta.objects.create(
            nome="Mario",
            cognome="Rossi",
            email="mario@example.com",
            oggetto="Info",
            messaggio="Ciao",
        )
        mail.outbox = []
        ok = email_service.invia_notifica_admin_nuova_richiesta(r)
        self.assertTrue(ok)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Nuova richiesta", mail.outbox[0].subject)
