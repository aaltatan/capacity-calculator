from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .managers import FacultyManager


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    students_count = models.PositiveIntegerField(default=0)
    teacher_to_student_ratio = models.PositiveIntegerField(
        default=35, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    objects = FacultyManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Faculty")
        verbose_name_plural = _("Faculties")


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_specialist = models.BooleanField(default=False)
    faculties = models.ManyToManyField(Faculty, related_name="specializations")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    class JobType(models.TextChoices):
        FULLTIME = "Fulltime", _("Fulltime")
        PARTTIME = "Parttime", _("Parttime")

    class DegreeType(models.TextChoices):
        MASTER = "Master", _("Master")
        DOCTORATE = "Doctorate", _("Doctorate")

    name = models.CharField(max_length=100, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="staff")
    specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, related_name="staff"
    )
    degree = models.CharField(
        max_length=100, choices=DegreeType.choices, default=DegreeType.DOCTORATE
    )
    is_local = models.BooleanField(default=False)
    job_type = models.CharField(
        max_length=100, choices=JobType.choices, default=JobType.FULLTIME
    )
    is_calculated = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = (
            "faculty__name",
            "is_calculated",
            "job_type",
            "-specialization__is_specialist",
            "is_local",
            "degree",
        )
        verbose_name = _("Staff")
        verbose_name_plural = _("Staff")


def staff_pre_save(sender, instance: Staff, **kwargs):
    if instance.job_type == Staff.JobType.PARTTIME:
        instance.is_local = False


def slugify_pre_save(sender, instance: Staff, **kwargs):
    instance.slug = slugify(instance.name, allow_unicode=True)


pre_save.connect(staff_pre_save, sender=Staff)
pre_save.connect(slugify_pre_save, sender=Staff)
pre_save.connect(slugify_pre_save, sender=Specialization)
pre_save.connect(slugify_pre_save, sender=Faculty)
