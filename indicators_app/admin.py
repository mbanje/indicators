from django.contrib import admin
from indicators_app.models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
	pass

@admin.register(Output)
class OutputAdmin(ImportExportModelAdmin):
	pass

@admin.register(Partner)
class PartnerAdmin(ImportExportModelAdmin):
	pass

@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin):
	pass

@admin.register(Frequency)
class FrequencyAdmin(ImportExportModelAdmin):
	pass

@admin.register(CPD)
class CPDAdmin(ImportExportModelAdmin):
	pass

@admin.register(Indicator)
class IndicatorAdmin(ImportExportModelAdmin):
	pass

@admin.register(InvolvedPartner)
class InvolvedPartnerAdmin(ImportExportModelAdmin):
	pass

@admin.register(ConcernedReport)
class ConcernedReportAdmin(ImportExportModelAdmin):
	pass

@admin.register(Measurement)
class MeasurementAdmin(ImportExportModelAdmin):
	pass