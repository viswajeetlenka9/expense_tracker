from django.db import models as django_models
from base.db.models import BaseModel
from base.db.validators import BlankValidator

class CategoryType(django_models.IntegerChoices):
    EXPENSE = 1, 'Expense'
    INCOME = 2, 'Income'

class Category(BaseModel):
    """
    Expense Category Model
    """
    name = django_models.CharField(
        null=False,
        blank=False,
        verbose_name="Category Name",
        max_length=50,
        unique=True,
        help_text="This is the expense category name.",
        validators=[
            BlankValidator(
                message="Category name must not be blank",
                code="invalid_category_name",
            )
        ],
        error_messages={
            "unique": "A category with that name already exists!"
        }
    )
    description = django_models.CharField(
        null=False,
        blank=False,
        verbose_name="Category Description",
        max_length=250,
        help_text="This is the expense category description.",
    )
    type = django_models.IntegerField(
        null=False,
        default=CategoryType.EXPENSE,
        choices=CategoryType.choices,
        verbose_name="Category Type",
        help_text="This is the category type"
    )

    class Meta:
        """
        Meta
        """

        db_table = "category"
        indexes = [
            django_models.Index(fields=["created_at"]),
            django_models.Index(fields=["updated_at"])
        ]