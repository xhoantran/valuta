from functools import partialmethod
from typing import Union, List, Tuple, Optional, Set, Callable

from django.db import models
from django.db.models import (
    IntegerField,
    BigIntegerField,
    SmallIntegerField,
    FloatField,
)
from django.conf import settings

from ...registry import Registry
from ...utils import get_currency_choices

__all__ = ("CurrencyField",)


class CurrencyField(models.CharField):
    """Currency field.

    Consists of two database fields:
    - amount: `BigIntegerField`
    - currency: `CharField` with choices.
    """

    def __init__(
        self,
        amount_fields: Optional[
            Union[List[str], Tuple[str, ...], Set[str]]
        ] = None,
        limit_choices_to: Optional[
            Union[List[str], Tuple[str, ...], Set[str]]
        ] = None,
        cast_to: Optional[Callable] = None,
        *args,
        **kwargs,
    ):
        self.amount_fields = amount_fields
        self.cast_to = cast_to
        kwargs["max_length"] = 10
        if limit_choices_to is None:
            settings_limit_choices_to = getattr(
                settings, "VALUTA_FIELD_LIMIT_CHOICES_TO", None
            )
            if settings_limit_choices_to:
                limit_choices_to = settings_limit_choices_to

        kwargs["choices"] = get_currency_choices(limit_choices_to)
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)
        if not self.null:
            setattr(
                cls,
                f"get_currency_cls",
                partialmethod(self.__class__._get_currency_cls, field=self),
            )
            if self.amount_fields:
                for amount_field in self.amount_fields:
                    setattr(
                        cls,
                        f"{amount_field}_in_currency_units",
                        partialmethod(
                            self.__class__._convert_to_currency_units,
                            field=self,
                            amount_field=amount_field,
                        ),
                    )

    def _get_currency_cls(
        self,
        field: Union[
            IntegerField, BigIntegerField, SmallIntegerField, FloatField
        ],
        **kwargs,
    ):
        key = getattr(self, field.name)
        return Registry.get(key)

    def _convert_to_currency_units(
        self,
        field: Union[
            IntegerField, BigIntegerField, SmallIntegerField, FloatField
        ],
        amount_field: str,
        **kwargs,
    ):
        key = getattr(self, field.name)
        currency_cls = Registry.get(key)
        amount_in_fractional_units = getattr(self, amount_field)
        value = currency_cls.convert_to_currency_units(
            amount_in_fractional_units
        )
        if field.cast_to:
            return field.cast_to(value)
        return value
