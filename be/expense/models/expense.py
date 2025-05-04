from django.db import models as django_models
from django.contrib.postgres import fields as postgres_fields
from base.db.models import BaseModel
from base.db.validators import BlankValidator
from category.models.category import Category

class SourceChoice(django_models.IntegerChoices):
    OFFLINE = 0, 'Offline'
    ONLINE = 1, 'Online'

class Expense(BaseModel):
    """
    Expense Model
    """
    name = django_models.CharField(
        null=False,
        blank=False,
        verbose_name="Expense Name",
        max_length=50,
        help_text="This is the expense name.",
        validators=[
            BlankValidator(
                message="Expense name must not be blank",
                code="invalid_expense_name",
            )
        ]
    )
    description = django_models.CharField(
        null=False,
        blank=False,
        verbose_name="Expense Description",
        max_length=250,
        help_text="This is the expense description.",
    )
    date = django_models.DateField(
        name="date",
        null=False,
        verbose_name="Expense Date",
        help_text="This is expense date"
    )
    amount = django_models.DecimalField(
        name="amount",
        verbose_name="Expense Amount",
        help_text="This is the expense amount",
        max_digits=12,
        decimal_places=2,
        blank=False,
        null=False,
        validators=[
            BlankValidator(
                message="Expense Amount must not be blank",
                code="invalid_expense_amount",
            )
        ]
    )
    source = django_models.IntegerField(
        null=False,
        blank=False,
        default=SourceChoice.ONLINE,
        choices=SourceChoice.choices,
        verbose_name="Expense Source",
        help_text="This is the source of the expense"
    )
    category = django_models.ForeignKey(
        to=Category,
        on_delete=django_models.PROTECT,
        related_name='expense',
        null=False,
        blank=False,
        help_text="The type of category this expense is."
    )
    tags = postgres_fields.ArrayField(
        base_field=django_models.CharField(
            max_length=128,
            null=False,
            blank=False,
            validators=[
                BlankValidator(),
            ],
        ),
        verbose_name="Expense Tags",
        null=True,
        default=None
    )

    class Meta:
        """
        Meta
        """

        db_table = "expense"
        indexes = [
            django_models.Index(fields=["created_at"]),
            django_models.Index(fields=["updated_at"])
        ]