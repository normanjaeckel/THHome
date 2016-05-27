from django.db import models


class RealEstate(models.Model):
    """
    Model for appartments, houses and other real estate.
    """
    ROOMS_CHOICES = (
        ('1', '1 Zimmer'),
        ('2', '2 Zimmer'),
        ('3', '3 Zimmer'),
        ('4', '4 Zimmer'),
        ('5+', '5 oder mehr Zimmer'))

    online = models.BooleanField(
        'Online',
        default=True,
        blank=True,
        help_text='Dieses Feld kann benutzt werden, um eine Wohnung erst '
                  'später freizuschalten.')

    title = models.CharField(
        'Titel',
        max_length=255)

    rooms = models.PositiveIntegerField(
        'Zimmer',
        default=4)

    size = models.PositiveIntegerField(
        'Größe',
        help_text='Angabe in m²')

    floor = models.CharField(
        'Etage',
        max_length=255,
        blank=True)

    balcony = models.BooleanField(
        'Balkon/Terrasse',
        blank=True)

    elevator = models.BooleanField(
        'Aufzug',
        blank=True)

    netto = models.FloatField(
        'Kaltmiete',
        help_text='Angabe in Euro.')

    extra_costs = models.FloatField(
        'Betriebskosten',
        help_text='Angabe in Euro. Die Position enthält auch die Heizkosten. '
                  'Der Heizkostenanteil kann in der Beschreibung erwähnt '
                  'werden.')

    deposit = models.CharField(
        'Kaution',
        max_length=255,
        default='Nach Vereinbarung')

    description = models.TextField(
        'Beschreibung',
        help_text='Absätze sind durch Leerzeilen zu trennen. Die ersten 20 '
                  'Wörter sind der Anrisstext auf der Startseite. Dieser ist '
                  'in nur einem Absatz formatiert.')

    class Meta:
        verbose_name = 'Wohnung/Grundstück'
        verbose_name_plural = 'Wohnungen/Grundstücke'

    def __str__(self):
        return self.title

    @property
    def brutto(self):
        """
        Returns the total rent.
        """
        return self.netto + self.extra_costs


class Image(models.Model):
    """
    Model for images for real estate.
    """
    realestate = models.ForeignKey(
        RealEstate,
        verbose_name='Wohnung/Grundstück')

    image = models.FileField(
        'Bild')

    short_description = models.CharField(
        'Kurzbeschreibung/Schlagwort',
        max_length=255,
        help_text='Die Kurzbeschreibung erscheint als Titel im Bild.')

    long_description = models.TextField(
        'Längere Beschreibung',
        blank=True,
        help_text='Die längere Beschreibung erscheint im Bild unter der '
                  'Kurzbeschreibung. Keinen zu langen Text verwenden.')

    class Meta:
        ordering = ('realestate',)
        verbose_name = 'Bild für Wohnung/Grundstück'
        verbose_name_plural = 'Bilder für Wohnungen/Grundstücke'

    def __str__(self):
        return 'Bild zu Wohnung/Grundstück {id}: {description}'.format(
            id=self.realestate.pk,
            description=self.description)

    @property
    def description(self):
        """
        Returns a combination of short and long description.
        """
        description = self.short_description
        if self.long_description:
            description += ' ({})'.format(self.long_description)
        return description


class Expose(models.Model):
    """
    Model for Exposés for real estate.
    """
    realestate = models.OneToOneField(
        RealEstate,
        verbose_name='Wohnung/Grundstück')

    pdf = models.FileField(
        'Bild')

    class Meta:
        ordering = ('realestate',)
        verbose_name = 'Exposé'
        verbose_name_plural = 'Exposés'

    def __str__(self):
        return 'Exposé zu {}'.format(self.realestate)


class Deal(models.Model):
    """
    Model for special deals and news.
    """
    title = models.CharField(
        'Titel',
        max_length=255)

    text = models.TextField(
        'Text')

    icon = models.CharField(
        'Icon',
        max_length=255,
        default='star',
        help_text='Siehe http://fontawesome.io/icons/.')

    weight = models.IntegerField(
        'Gewichtung',
        default=100,
        help_text='Bestimmt die Reihenfolge der Elemente. Elemente mit '
                  'größeren Zahlen erscheinen weiter unten beziehungsweise '
                  'hinten.')

    class Meta:
        ordering = ('weight',)
        verbose_name = 'Sonderaktion'
        verbose_name_plural = 'Sonderaktionen'

    def __str__(self):
        return 'Sonderaktion: {}'.format(self.title)


class Impression(models.Model):
    """
    Model for images for global impressions.
    """
    image = models.FileField(
        'Bild')

    short_description = models.CharField(
        'Kurzbeschreibung/Schlagwort',
        max_length=255,
        help_text='Die Kurzbeschreibung erscheint als Titel im Bild.')

    long_description = models.TextField(
        'Längere Beschreibung',
        blank=True,
        help_text='Die längere Beschreibung erscheint im Bild unter der '
                  'Kurzbeschreibung. Keinen zu langen Text verwenden.')

    weight = models.IntegerField(
        'Gewichtung',
        default=100,
        help_text='Bestimmt die Reihenfolge der Elemente. Elemente mit '
                  'größeren Zahlen erscheinen weiter unten beziehungsweise '
                  'hinten.')

    class Meta:
        ordering = ('weight',)
        verbose_name = 'Bild für Impression'
        verbose_name_plural = 'Bilder für Impressionen'

    def __str__(self):
        return 'Bild für Impression: {description}'.format(
            description=self.description)

    @property
    def description(self):
        """
        Returns a combination of short and long description.
        """
        description = self.short_description
        if self.long_description:
            description += ' ({})'.format(self.long_description)
        return description
