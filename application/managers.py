from django.db import models
from django.db.models import Count, Q

from .controllers import Capacity


class FacultyManager(models.Manager):
    def get_capacity(self, locality_percentage: float = 0.5) -> list[Capacity]:
        return [
            Capacity(**faculty_kwargs, locality_percentage=locality_percentage)
            for faculty_kwargs in self._get_capacity_kwargs()
        ]

    def _get_capacity_kwargs(self) -> dict[str, str | int]:
        return (
            self.get_queryset()
            .values(
                "name",
                "students_count",
                "teacher_to_student_ratio",
            )
            .annotate(
                local_fulltime_specialist_count=Count(
                    "staff",
                    filter=Q(
                        staff__job_type="Fulltime",
                        staff__degree="Doctorate",
                        staff__is_local=True,
                        staff__specialization__is_specialist=True,
                        staff__is_calculated=True,
                    ),
                ),
                local_fulltime_supportive_count=Count(
                    "staff",
                    filter=Q(
                        staff__job_type="Fulltime",
                        staff__degree="Doctorate",
                        staff__is_local=True,
                        staff__specialization__is_specialist=False,
                        staff__is_calculated=True,
                    ),
                ),
                foreign_fulltime_specialist_count=Count(
                    "staff",
                    filter=Q(
                        staff__job_type="Fulltime",
                        staff__degree="Doctorate",
                        staff__is_local=False,
                        staff__specialization__is_specialist=True,
                        staff__is_calculated=True,
                    ),
                ),
                foreign_fulltime_supportive_count=Count(
                    "staff",
                    filter=Q(
                        staff__job_type="Fulltime",
                        staff__degree="Doctorate",
                        staff__is_local=False,
                        staff__specialization__is_specialist=False,
                        staff__is_calculated=True,
                    ),
                ),
                parttime_specialist_count=Count(
                    "staff",
                    filter=Q(
                        staff__job_type="Parttime",
                        staff__degree="Doctorate",
                        staff__specialization__is_specialist=True,
                        staff__is_calculated=True,
                    ),
                ),
                parttime_supportive_count=Count(
                    "staff",
                    filter=Q(
                        staff__job_type="Parttime",
                        staff__degree="Doctorate",
                        staff__specialization__is_specialist=False,
                        staff__is_calculated=True,
                    ),
                ),
                master_count=Count(
                    "staff",
                    filter=Q(
                        staff__degree="Master",
                        staff__is_calculated=True,
                    ),
                ),
            )
        )
