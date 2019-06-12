from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
import datetime


class Section(models.Model):
    section_designation = models.CharField(max_length=200)


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.section_designation

class Output(models.Model):
    output_designation = models.CharField(max_length=500)
    output_description = models.CharField(max_length=500, null=True)
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.output_designation, self.output_description, self.section)

class Partner(models.Model):
    partner_designation = models.CharField(max_length=200)


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.partner_designation


class Report(models.Model):
    report_designation = models.CharField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.report_designation


class Frequency(models.Model):
    frequency_designation = models.CharField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.frequency_designation


class CPD(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return "{0} - {1}".format(self.start_date, self.end_date)


class Indicator(models.Model):
    cpd = models.ForeignKey(
        CPD,
        on_delete=models.CASCADE
        )
    output = models.ForeignKey(
        Output,
        on_delete=models.CASCADE
        )
    indicator_name = models.CharField(max_length=500)
    frequency = models.ForeignKey(
        Frequency,
        on_delete=models.CASCADE
        )


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.cpd, self.output, self.indicator_name, self.frequency)



class InvolvedPartner(models.Model):
    indicator = models.ForeignKey(
        Indicator,
        on_delete=models.CASCADE
        )
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return "{0} - {1}".format(self.indicator, self.partner)


class ConcernedReport(models.Model):
    indicator = models.ForeignKey(
        Indicator,
        on_delete=models.CASCADE
        )
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return "{0} - {1}".format(self.indicator, self.report)



class Measurement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    expected_value = models.FloatField()
    value = models.FloatField()
    indicator = models.ForeignKey(
        Indicator,
        on_delete=models.CASCADE
        )
    

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return "{0} - {1} - {2} - {3} - {4}".format(self.indicator, self.start_date, self.end_date, self.expected_value, self.value)

