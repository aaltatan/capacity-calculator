from django.contrib import admin

from . import models


class StaffInline(admin.TabularInline):
    model = models.Staff
    extra = 1
    fields = (
        "name",
        "faculty",
        "specialization",
        "is_calculated",
        "degree",
        "is_local",
        "job_type",
    )


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "students_count", "teacher_to_student_ratio")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = (StaffInline,)


@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_specialist")
    search_fields = ("name",)
    list_filter = ("is_specialist",)
    inlines = (StaffInline,)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    raw_id_fields = ("specialization",)
    list_display = (
        "name",
        "faculty",
        "specialization",
        "specialization__is_specialist",
        "is_calculated",
        "degree",
        "is_local",
        "job_type",
    )
    search_fields = ("name", "faculty__name", "specialization__name")
    list_filter = (
        "faculty",
        "specialization",
        "specialization__is_specialist",
        "is_calculated",
        "degree",
        "is_local",
        "job_type",
    )
    list_per_page = 20
    prepopulated_fields = {"slug": ("name",)}
