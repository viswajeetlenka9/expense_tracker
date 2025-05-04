from django.db.models import Model, DateTimeField


class BaseModel(Model):
    created_at = DateTimeField(
        name="created_at",
        null=False,
        verbose_name="Create Date",
        auto_now_add=True,
        help_text="The date this record was created.",
    )
    updated_at = DateTimeField(
        name="updated_at",
        null=False,
        verbose_name="Update Date",
        auto_now=True,
        help_text="The date this record was updated.",
    )

    class Meta:
        """
        Define outer class as abstract
        """

        abstract = True
