from django.test import TestCase
from encuesta.forms import ChoiceForm, AstronomerForm


class Setup_Class_Choice(TestCase):
    def setUp(self):
        self.choice = ChoiceForm.objects.create(
            usuario="user", imagen="Image_name", voto="A"
        )


class Choice_Form_Test(TestCase):
    def test_ChoiceForm_valid(self):
        # Crea un voto válido (con una imágen vacía)
        form = ChoiceForm(data={"usuario": "user", "imagen": "", "voto": "A"})
        self.assertTrue(form.is_valid())

    def test_ChoiceForm_invalid_vote(self):
        # Prueba que el voto no puede tener más de 20 caracteres
        voto = 21 * "x"
        form = ChoiceForm(data={"usuario": "user", "imagen": "", "voto": voto})
        self.assertFalse(form.is_valid())

    def test_ChoiceForm_invalid_vote2(self):
        # Prueba que el voto no puede estar vacío
        form = ChoiceForm(data={"usuario": "user", "imagen": "", "voto": ""})
        self.assertFalse(form.is_valid())


class Setup_Class_Astronomer(TestCase):
    def setUp(self):
        self.astronomer = AstronomerForm.objects.create(
            username="user",
            email="user@mp.com",
            password1="user",
            password2="user",
        )


class Astronomer_Form_Test(TestCase):
    def test_AstronomerForm_valid(self):
        # Crea un usuario válido
        form = AstronomerForm(
            data={
                "username": "user",
                "email": "user@mp.com",
                "password1": "user1234",
                "password2": "user1234",
            }
        )
        self.assertTrue(form.is_valid())

    def test_AstronomerForm_invalid_password(self):
        # Usuario inválido por contraseña débil
        form = AstronomerForm(
            data={
                "username": "user",
                "email": "user@mp.com",
                "password1": "1234",
                "password2": "1234",
            }
        )
        self.assertFalse(form.is_valid())

    def test_AstronomerForm_invalid_password2(self):
        # Usuario inválido por contraseñas diferentes
        form = AstronomerForm(
            data={
                "username": "user",
                "email": "user@mp.com",
                "password1": "user1234",
                "password2": "user5678",
            }
        )
        self.assertFalse(form.is_valid())

    def test_AstronomerForm_invalid_user(self):
        # Usuario inválido por nombre en blanco
        form = AstronomerForm(
            data={
                "username": "",
                "email": "user@mp.com",
                "password1": "user1234",
                "password2": "user1234",
            }
        )
        self.assertFalse(form.is_valid())

    def test_AstronomerForm_invalid_mail(self):
        # Usuario inválido por mail en blanco
        form = AstronomerForm(
            data={
                "username": "user",
                "email": "",
                "password1": "user1234",
                "password2": "user1234",
            }
        )
        self.assertFalse(form.is_valid())
