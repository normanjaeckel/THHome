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

    description = models.TextField(
        'Beschreibung',
        help_text='Absätze sind durch Leerzeilen zu trennen. Die ersten 20 '
                  'Wörter sind der Anrisstext auf der Startseite. Dieser ist '
                  'in nur einem Absatz formatiert.')

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

    when_free = models.CharField(
        'Verfügbar ab',
        max_length=255,
        default='sofort')

    netto = models.FloatField(
        'Kaltmiete',
        help_text='Angabe in Euro.')

    extra_costs_cold = models.FloatField(
        'Kalte Betriebskosten',
        help_text='Angabe in Euro.')

    extra_costs_heating = models.FloatField(
        'Heizkosten',
        help_text='Angabe in Euro.')

    split_extra_costs = models.BooleanField(
        'Getrennte Ausweisung der Betriebskosten',
        blank=True,
        help_text='Ist dieses Feld aktiviert, werden kalte Betriebskosten und '
                  'Heizkosten getrennt ausgewiesen. Ansonsten wird die Summe '
                  'gebildet.')

    deposit = models.CharField(
        'Kaution',
        max_length=255,
        default='Nach Vereinbarung')

    details = models.CharField(
        'Details',
        max_length=255,
        blank=True,
        help_text='Details mit Kommas trennen, zum Beispiel: '
                  'Fußbodenheizung,Kamin,WG geeignet,Badewanne')

    energy_certificate = models.CharField(
        'Energieausweis',
        max_length=255,
        help_text='Angaben mit Kommas trennen, zum Beispiel: '
                  'Verbrauchsausweis,100 kWH/(m²*a),Erdgas,1980,B')

    class Meta:
        verbose_name = 'Wohnung/Grundstück'
        verbose_name_plural = 'Wohnungen/Grundstücke'

    def __str__(self):
        return self.title

    @property
    def extra_costs(self):
        """
        Returns all extra costs.
        """
        return self.extra_costs_cold + self.extra_costs_heating

    @property
    def brutto(self):
        """
        Returns the total rent.
        """
        return self.netto + self.extra_costs

    @property
    def detail_list(self):
        """
        Returns an iterable of all details of this real estate.
        """
        return self.details.split(',')

    @property
    def energy_certificate_dict(self):
        """
        Returns a dictionary with the required data from the energy
        certificate.
        """
        e = self.energy_certificate.split(',') + 5 * ['']
        return {
            'type': e[0],
            'value': e[1],
            'source': e[2],
            'year': e[3],
            'efficiency_class': e[4]
        }


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

    weight = models.IntegerField(
        'Gewichtung',
        default=100,
        help_text='Bestimmt die Reihenfolge der Elemente. Elemente mit '
                  'größeren Zahlen erscheinen weiter unten beziehungsweise '
                  'hinten. Das erste Bild erscheint auf der Startseite.')

    class Meta:
        ordering = ('realestate', 'weight')
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
        'Exposé-Datei')

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

    short_text = models.TextField(
        'Kurzer Text',
        help_text='Kurzer Anrisstext zur Bescheibung der Aktion.')

    details = models.TextField(
        'Details',
        help_text='Längerer Text zur Bescheibung der Aktion, der erst nach '
                  'Klick auf den Details-Button erscheint.')

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


class About(models.Model):
    """
    Model for elements in the about section.
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
        verbose_name = 'Vorteil der Wohnanlage'
        verbose_name_plural = 'Vorteile der Wohnanlage'

    def __str__(self):
        return 'Vorteil der Wohnanlage: {}'.format(self.title)


class Impression(models.Model):
    """
    Model for images for global impressions.
    """
    image = models.FileField(
        'Bild',
        help_text='Bildformat 650 x 350')

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
