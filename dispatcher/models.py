from django.db import models

from django.core.validators import RegexValidator


class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=17,
                                    blank=True,
                                    unique=True
                                    )  # Validators should be a list


class act(models.Model):
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    adress = models.CharField(max_length=200)
    act_type = models.CharField(max_length=20)
    text = models.TextField()
